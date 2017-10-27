import mysql.connector
conn = mysql.connector.connect (user='root',password='letmein',host='localhost',database='calc_database')
mycursor=conn.cursor()
mycursor.execute("select * from calc_values")
mylist = mycursor.fetchall()
for i in mylist:
    print(i)
