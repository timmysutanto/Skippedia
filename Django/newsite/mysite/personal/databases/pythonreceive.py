import mysql.connector
from mysql.connector import Error
try:
    mySQLconnection = mysql.connector.connect(host='localhost',
                                database='pythontest',
                                user='root',
                                password='')
    sql_select_Query = "select * from data"
    cursor = mySQLconnection .cursor()
    cursor.execute(sql_select_Query)
    records = cursor.fetchall()
    print("Total number of rows in data is - ", cursor.rowcount)
    print ("Printing each row's column values i.e.  developer record")
    for row in records:
        print("Id = ", row[0], )
        print("Name = ", row[1])
    cursor.close()
    
except Error as e :
    print ("Error while connecting to MySQL", e)
# finally:
    #closing database connection.
    # if(mySQLconnection.is_connected()):
    #     mySQLconnection.close()
    #     print("MySQL connection is closed")