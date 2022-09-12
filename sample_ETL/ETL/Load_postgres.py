import pandas as pd
from sqlalchemy import create_engine    
engine = create_engine("postgresql+psycopg2://postgres:thuydang@localhost:5432/exportreport")

def import_postgres():
    with pd.ExcelFile('../Airflow/dags/data/Table3.xlsx') as xls:
        df = pd.read_excel(xls)
        df.to_sql(name= 'export', con= engine, if_exists= 'append', index= False)
        print('Import Successfully!!')



