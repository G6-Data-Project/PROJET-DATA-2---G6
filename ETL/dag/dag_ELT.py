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
# upload le fichier dans le s3
def upload_csv_to_s3():
    # Remplacez ces valeurs par vos propres informations d'identification AWS
    aws_conn = BaseHook.get_connection('aws_default')
    aws_access_key_id = aws_conn.login
    aws_secret_access_key = aws_conn.password

    # Remplacez ces valeurs par le nom de votre bucket S3 et le chemin du fichier local
    bucket_name = 'foot-data-g6'
    file_path = './fichier/products.csv'
    object_key = 'dossier_optionnelles/nom_du_fichier.csv'

    # Créer une session AWS
    session = boto3.Session(
        aws_access_key_id=aws_access_key_id,
        aws_secret_access_key=aws_secret_access_key
    )

    # Créer un client S3
    s3_client = session.client('s3')

    # Envoyer le fichier vers S3
    try:
        s3_client.upload_file(file_path, bucket_name, object_key)
        print(f"Le fichier {file_path} a été envoyé avec succès vers {bucket_name}/{object_key}")
    except Exception as e:
        print("Une erreur s'est produite:", e)

generate_csv_task = PythonOperator(
    task_id='upload_csv_to_s3',
    python_callable=upload_csv_to_s3,
    dag=dag,
)

generate_csv_task
