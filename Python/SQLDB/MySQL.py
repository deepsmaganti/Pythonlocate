import mysql.connector
conn = mysql.connector.connect (user='root',password='letmein',host='localhost')
mycursor=conn.cursor()
mycursor.execute("create database test_python")
mycursor.execute("use test_python")
mycursor.execute("""create table customer
                 (
                 id int primary key,
                 name varchar (30),
                 email varchar (25),
                 age int,
                 gender char (1),
                 last_visit date)""")
mycursor.close()