# Module Imports
import mariadb
import sys

#Connect to MariaDB Platform
try:
     conn = mariadb.connect(
          user="roy",
          password="roy",
          host="192.168.1.69",
          port=3306,
          database="Solar_Database"
     )
except mariadb.Error as e:
     print("Error connecting to MariaDB Platform: {e}")
     sys.exit(1)

#Get Cursor
cur = conn.cursor()
cur.execute("SELECT NOW()")
print(cur.fetchone())
