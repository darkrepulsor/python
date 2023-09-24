import sqlalchemy, pyodbc, os
import pandas as pd
import platform
import socket 

os.chdir(r"C:\Users\abraa\Documents\DataLab\F1")
os.getcwd()

os.listdir()

print(platform.node())
print(socket.gethostname())

print(pyodbc.drivers())

# How to make a connection
# ODBC Driver 17 for SQL Server

conn = sqlalchemy.create_engine('mssql+pyodbc://{socket.gethostname()}/testeReg?trusted_connection=yes&driver=ODBC Driver 17 for SQL Server')
for fl in os.listdir():
    df = pd.read_csv(fl)
    df.to_sql("testeReg",con = conn, if_exists = "append", index=False)






#  \circuits.csv