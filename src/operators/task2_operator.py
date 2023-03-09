import json
from google.oauth2 import service_account
from google.cloud import bigquery

def load_bq_bq(**context):

    json_file_path = 'path/to/credentials.json'

    with open(json_file_path, 'r') as f:
        json_data = json.load(f)

    creds = service_account.Credentials.from_service_account_info(json_data)

    client = bigquery.Client(credentials=creds)

    if     context['params'].get('first_load'):
        query = '''DELETE FROM mart_data.marketing_account
        WHERE Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)'''
        query_job = client.query(query)
        query_job.result()
    query = """
        SELECT COALESCE(ga.`Account Name`, yd.`Account Name`, cd.`Account Name`) AS `Account Name`,
       ga.Cost AS `Google Ads Cost`,
       yd.Cost AS `Yandex Direct Cost`,
       cd.`Stage of lead`
FROM raw_data.google_ads AS ga
FULL OUTER JOIN raw_data.yandex_direct AS yd
  ON ga.`Account Name` = yd.`Account Name` AND ga.`Date` = yd.`Date`
FULL OUTER JOIN raw_data.crm_deals AS cd
  ON (ga.`Account Name` = cd.`Account Name` OR yd.`Account Name` = cd.`Account Name`)
     AND ga.`Date Create` = cd.`Date Create`
ORDER BY `Account Name`;
    """

    if     context['params'].get('first_load'):
        query = '''CREATE TABLE mart_data.marketing_account AS ''' + query

        time_partitioning = None

    else:
        query = query + 'WHERE  Date >= DATE_SUB(CURRENT_DATE(), INTERVAL 7 DAY)'

        time_partitioning = bigquery.table.TimePartitioning(field="Date")
    project_id = "ProjectID"
    dataset_id = "Dataset"
    table_id = "marketing_account"
    table_ref = project_id + "." + dataset_id + "." + table_id
    job_config = bigquery.QueryJobConfig(schema="mart_data",destination=table_ref, write_disposition='WRITE_TRUNCATE',time_partitioning=time_partitioning)
    query_job = client.query(query, job_config=job_config)

    query_job.result()