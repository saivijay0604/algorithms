import pyodbc
import os
from numpy import *
import pandas as pd

data = pd.read_csv("Weather_Linear_Regression_Model.csv")  #read csv data
df = pd.DataFrame(data, columns= ['ID_Num',
                                  'Outlook',
                                  'Temperature',
                                  'Humidity',
                                  'Windy',
                                  'Play'])
conn = pyodbc.connect('Driver={ODBC Driver 17 for SQL Server};' #DB connection start
                      'Server=127.0.0.1;'
                      'port=1433;'
                      'Database=dbPractice2;'
                      'Trusted_Connection=yes;')
cursor = conn.cursor()   #DB connection end

"""cursor.execute('CREATE TABLE weatherInfo '
               '(ID_Num int,'
               'Outlook nvarchar(20),'
               'Temperature int,'
               'Humidity int,'
               'Windy nvarchar(20),'
               'Play nvarchar(20))')  #create table

for row in df.itertuples():
    cursor.execute('''
                INSERT INTO dbPractice2.dbo.weatherInfo (ID_Num, Outlook, Temperature,Humidity,Windy,Play)
                VALUES (?,?,?,?,?,?)
                ''',
                row.ID_Num,
                row.Outlook,
                row.Temperature,
                row.Humidity,
                row.Windy,
                row.Play
                )"""  #insert csv data into the table

cursor.execute('select * from dbPractice2.dbo.weatherInfo') #print table
for row in cursor:
    print(row)

conn.commit()