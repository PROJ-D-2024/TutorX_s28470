from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import kagglehub
import pandas as pd
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import json

def download_data():
    print("Starting download data task...")
    path = kagglehub.dataset_download("yasserh/wine-quality-dataset")
    print(f"Data downloaded successfully, path: {path}")
    return path

def read_data(path):
    print(f"Starting to read data from {path}...")
    wine_data_path = f"{path}/WineQT.csv"
    df = pd.read_csv(wine_data_path)
    print(f"Data read successfully, number of records: {len(df)}")
    return df.to_json(orient="records")

def upload_to_google_sheets(records_json):
    print(f"Starting to upload {len(json.loads(records_json))} records to Google Sheets...")
    records = json.loads(records_json)  
    df = pd.DataFrame(records)
    
    creds_file = './credentials.json'
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(creds_file, scope)
    client = gspread.authorize(creds)
    spreadsheet = client.open("Wine Quality Dataset")
    worksheet = spreadsheet.get_worksheet(0)
    
    print("Clearing existing data in Google Sheets...")
    worksheet.clear()
    
    print("Uploading new data to Google Sheets...")
    worksheet.update([df.columns.tolist()] + df.values.tolist())
    print("Data uploaded successfully to Google Sheets!")

default_args = {
    'owner': 'airflow',
    'start_date': datetime(2024, 12, 16),
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    'wine_quality_dag',
    default_args=default_args,
    description='DAG for downloading, reading, and uploading wine quality dataset',
    schedule_interval=None,  
)

download_task = PythonOperator(
    task_id='download_data',
    python_callable=download_data,
    dag=dag,
)

read_task = PythonOperator(
    task_id='read_data',
    python_callable=read_data,
    op_kwargs={'path': "{{ ti.xcom_pull(task_ids='download_data') }}"},
    dag=dag,
)

upload_task = PythonOperator(
    task_id='upload_to_google_sheets',
    python_callable=upload_to_google_sheets,
    op_kwargs={'records_json': "{{ ti.xcom_pull(task_ids='read_data') }}"},
    dag=dag,
)

download_task >> read_task >> upload_task