from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime
from src.operators.testOperator import load_bq_bq

default_args = {
    'depends_on_past': False,
    'start_date': datetime(2023, 3, 7, 3, 0), # 3 часа ночи по серверному времени
    'email_on_failure': False,
    'email_on_retry': False,
    'execution_timeout': timedelta(hours=1) # ограничение времени выполнения в 1 час
}

with DAG('join_data_bq', default_args=default_args, schedule_interval='0 3 * * *') as dag:
	join_data_bq_ti = PythonOperator(
    task_id='join_data_bq_task',
    python_callable=load_bq_bq,
    dag=dag,
	  params={'first_load':False}
)