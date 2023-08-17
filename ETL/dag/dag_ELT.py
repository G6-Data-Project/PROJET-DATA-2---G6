from datetime import datetime, timedelta
from airflow import DAG
from airflow.providers.amazon.aws.transfers.local_to_s3 import LocalFilesystemToS3Operator
from airflow.operators.python import PythonOperator
from airflow.hooks.base_hook import BaseHook
import os
import csv
import boto3

default_args = {
    'owner': 'G6_data_test_3',
    'start_date': datetime.now(), #le DAG commence à s'exécuter dès que vous l'activez
    'depends_on_past': False, #cela signifie que les exécutions futures du DAG ne dépendront pas du succès de l'exécution précédente
    'retries': 1, #signifie que la tâche sera réexécutée une fois en cas d'échec initial
    'retry_delay': timedelta(minutes=5), #signifie que si la tâche échoue, Airflow attendra 5 minutes avant de la réexécuter
}

dag = DAG(
    'test_3_dag',
    default_args=default_args,
    schedule_interval=timedelta(days=90),  # Exécution tous les 3 mois
    catchup=False,#Cela signifie que seules les exécutions futures seront planifiées en fonction du schedule_interval.
)
