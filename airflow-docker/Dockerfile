FROM apache/airflow:2.5.0

USER root

RUN apt-get update && \
    apt-get install -y gnupg2 && \
    echo "deb http://packages.cloud.google.com/apt cloud-sdk main" | tee -a /etc/apt/sources.list.d/google-cloud-sdk.list && \
    curl https://packages.cloud.google.com/apt/doc/apt-key.gpg | apt-key add - && \
    apt-get update && \
    apt-get install -y google-cloud-sdk && \
    apt-get clean && \
    apt-get install -y jq && \
    rm -rf /var/lib/apt/lists/*

COPY data.sql /data.sql
COPY basic_creds.json /basic_creds.json
COPY service_account_creds.json /service_account_creds.json

USER airflow
RUN gcloud auth activate-service-account --key-file=/service_account_creds.json && \
    gcloud config set project $(cat /basic_creds.json | jq -r .project_id) # && \
#    bq update-project --default_table_expiration 3600 --default_partition_expiration 0 --enable_all_users $(cat /basic_creds.json | jq -r .project_id) && \
#    bq mk raw_data
RUN bq query --use_legacy_sql=false </data.sql

