import mysql.connector
conn = mysql.connector.connect (user='root',password='letmein',host='localhost',database = 'hello')
mycursor=conn.cursor()
mycursor.execute("create database calc_database")
mycursor.execute("use calc_database")
mycursor.execute("""create table calc_values
                (
                id int primary key,
                value1 int,
                value2 int
                )""")
mycursor.close()