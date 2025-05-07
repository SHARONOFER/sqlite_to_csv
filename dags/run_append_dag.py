from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import sys
sys.path.append('/opt/airflow/scripts')

from append_row import append_latest_user

default_args = {
    'owner': 'sharon',
    'retries': 1,
    'retry_delay': timedelta(minutes=1),
}

with DAG(
    dag_id='append_sqlite_row_to_csv',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',  # or change to None if you only want to run manually
    catchup=False,
    default_args=default_args,
    description='Appends the latest row from SQLite to a CSV file',
) as dag:

    append_row = PythonOperator(
        task_id='append_latest_user_row',
        python_callable=append_latest_user
    )
