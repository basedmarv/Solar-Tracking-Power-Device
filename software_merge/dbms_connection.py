import mariadb
import psycopg2 as db
import sys
import os

from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

def connect(): 
    try:
        conn = mariadb.connect(
            user = os.environ.get("USER"),
            password = os.environ.get("PASSWORD"),
            host = os.environ.get("HOST"),
            port= os.environ.get("PORT"),
            database= os.environ.get("DATABASE")
        )
        
        return conn
    except mariadb.Error as e:
        print(f'Error connecting to MariaDB Platform: {e}')
        sys.exit(1)

