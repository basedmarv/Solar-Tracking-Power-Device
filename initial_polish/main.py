from dbms_connection import *

if __name__ == '__main__':
    connection = connect()
    
    cur = connection.cursor()
    cur.execute("SELECT NOW();")
    print(cur.fetchone())

    cur.close()