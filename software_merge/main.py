from jobs import * 
from dbms_connection import *

if __name__ == '__main__':
    #run_jobs()
    connection = connect()
    
    cur = connection.cursor()

    # cur.execute("SELECT * FROM TandP;")
    # rows = cur.fetchall()
    # headers = [col[0] for col in cur.description]
    # fp = open('test.csv', 'w')
    # myFile = csv.writer(fp)
    # myFile.writerow(headers)
    # myFile.writerows(rows)
    # fp.close()


    # cur.execute("SELECT * FROM TandP WHERE time = 10;")
    # cur.fetchone()

    #cur.execute("INSERT INTO Main_TBL(date,time,longitude,latitude,voltage)  VALUES ('8-28-2019'," + str(2.5) + "," + str(6.9) + "," + str(.69) + "," + str(69.69) + ");")
    #cur.execute("INSERT INTO Main_TBL(date,time,longitude,latitude,voltage) VALUES('18',350.0,23.0,24.0,0.0);")
    #print(cur.fetchone())
    print(cur.execute("SELECT * FROM Main_TBL;")
    #print(cur.execute("SELECT * FROM Main_TBL;").fetchall())
    connection.commit()
    cur.close()

