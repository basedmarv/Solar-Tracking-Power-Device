import mariadb
import sys
import os
import csv

from dotenv import load_dotenv, find_dotenv
import datetime

load_dotenv(find_dotenv())

def connect(): 
    try:
        conn = mariadb.connect(
            user = "roy",
            password = os.environ.get("PASSWORD"),
            host = os.environ.get("HOST"),
            port= int(os.environ.get("PORT")),
            database= os.environ.get("DATABASE")
        )
        
        return conn
    except mariadb.Error as e:
        print(f'Error connecting to MariaDB Platform: {e}')
        sys.exit(1)

def insert_data(time, latitude, longitude, voltage):
    connection = connect()
    cur = connection.cursor()

    date_today = datetime.datetime.today().strftime('%Y-%m-%d')
    cur.execute("INSERT INTO Main_TBL(date,time,longitude,latitude,voltage)  VALUES ('" + date_today + "'," + str(time) + "," + str(longitude) + "," + str(latitude) + "," + str(voltage) + ");")
    connection.commit()
    cur.close()


def extract_data():
    connection = connect()
    cur = connection.cursor()

    filename = 'data_spreadsheet.csv'
    cur.execute("SELECT time, latitude FROM Main_TBL;")
    rows = cur.fetchall()
    headers = [col[0] for col in cur.description]
    fp = open(filename, 'w')
    myFile = csv.writer(fp)
    myFile.writerow(headers)
    myFile.writerows(rows)
    fp.close()    
    return filename