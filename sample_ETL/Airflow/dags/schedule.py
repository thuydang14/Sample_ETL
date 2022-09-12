import pandas as pd
from airflow import DAG
from airflow.utils.dates import days_ago
from airflow.operators.python_operator import PythonOperator
from sqlalchemy import create_engine
import os
file_import = f'{os.getcwd()}/dags/data/Table3.xlsx'
engine = create_engine("postgresql+psycopg2://postgres:thuydang@host.docker.internal:5432/exportreport")
def import_postgres():
    with pd.ExcelFile(file_import) as xls:
        df = pd.read_excel(xls)
        df.to_sql(name= 'export', con= engine, if_exists= 'append', index= False)
        print('Import Successfully!!')


args = {
    'owner': 'ThuyDang',
    'start_date': days_ago(1)
}

#defining the dag object
dag = DAG(
    dag_id='first_dag',
    default_args=args,
    schedule_interval= '*/2 * * * *'
)

with dag: 
    import_task = PythonOperator(
        task_id = 'import_to_export',
        python_callable=import_postgres
    )
