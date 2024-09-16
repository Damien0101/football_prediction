from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from datetime import datetime

def hello():
    print("Hello World ! test")
    pass

default_args = {
    'start_date':datetime(2024,9,16)
}

with DAG('test1',
         default_args=default_args,
         schedule=None) as dag:
    hello_task = PythonOperator('hello', python_callable=hello)