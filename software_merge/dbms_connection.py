import mariadb
import sys
import os
import csv

from dotenv import load_dotenv, find_dotenv
from datetime import datetime

load_dotenv(find_dotenv())

def connect(): 
    try:
        print(f'user: {os.environ.get("USER")}')
        print(f'password: {os.environ.get("PASSWORD")}')
        print(f'host: {os.environ.get("HOST")}')
        

        conn = mariadb.connect(
            # user = os.environ.get("USER"),
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

    date_today = datetime.today().strftime('%Y-%m-%d')
    cur.execute(f'INSERT INTO Main_TBL(time,position)  VALUES ({date_today}, {time}, {latitude}, {longitude}, {voltage});')