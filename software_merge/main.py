from dbms_connection import *
from jobs import * 

if __name__ == '__main__':
    # run_jobs()
    connection = connect()
    
    cur = connection.cursor()

    cur.execute("SELECT * FROM TandP;")
    rows = cur.fetchall()
    headers = [col[0] for col in cur.description]
    fp = open('test.csv', 'w')
    myFile = csv.writer(fp)
    myFile.writerow(headers)
    myFile.writerows(rows)
    fp.close()


    # cur.execute("SELECT * FROM TandP WHERE time = 10;")
    # cur.fetchone()

    # cur.execute("INSERT INTO TandP(time,position)  VALUES (18, 350);")
    # print(cur.fetchone())
    
    # print(cur.execute("SELECT * FROM TandP;").fetchall())

    cur.close()

