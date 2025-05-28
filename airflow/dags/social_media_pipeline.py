from airflow import DAG
from airflow.operators.bash import BashOperator
from datetime import datetime

#fsl is short hand of Financial Sanctions List
with DAG('fsl_ingestion',
         start_date=datetime(1990, 3, 5),
         schedule_interval='@daily',
         catchup=False) as dag:

    download_fsl = BashOperator(
        task_id='download_fsl',
        bash_command='curl -o /tmp/fsl.csv https://tfs.fic.gov.za/Pages/DownLoadList'
    )

    upload_to_minio = BashOperator(
        task_id='upload_to_minio',
        bash_command='mc alias set local http://minio:9000 minioadmin minioadmin && mc cp /tmp/fsl.csv local/raw/fsl.csv'
    )

    download_fsl >> upload_to_minio