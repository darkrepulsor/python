import pyodbc
import pandas as pd
import numpy as np

conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};'
                      'Server=DESKTOP-URL1JGV;'
                      'Database=testeReg;'
                      'Trusted_Connection=yes;')


csv_file = r'C:\Users\abraa\Documents\DataLab\F1\circuits.csv'

df = pd.read_csv(csv_file, 
                dtype={'lat': str, 'lng': str}
                ,sep=',')

df['location'] = df['location'].str.replace('&','"&"')

df = df.apply(pd.to_numeric, errors='coerce')
df = df.where(pd.notnull(df),None)

table_name = 'F1_CIRCUITS'

columns = [col for col in df.columns if col not in ['lat','lng']]
placeholders = ','.join(['?' for _ in df.columns])
query = f'INSERT INTO {table_name} ({",".join(columns)}) VALUES ({placeholders});'

cursor = conn.cursor()
for row in df.itertuples(index=False):
    cursor.execute(query,row)
conn.commit()

conn.close()
