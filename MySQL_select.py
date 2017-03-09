#Create generic function to perform select operations that works for db.
#You can try to implement it by your understanding, just remember one function should support all db's and tables

import mysql.connector

conn = None

class DB_Queries:
    def __init__(self, user, pwd, host, dbname):
        self.user = user
        self.pwd = pwd
        self.host = host
        self.dbname = dbname
        for i in range(5):
            try:
                global conn
                conn = mysql.connector.connect(user=user, password=pwd, host=host, database=dbname)
                if conn:
                    break
            except mysql.connector.errors as err:
                print 'Something went wrong... Retrying'
                raise err
        return

class select:
    def __init__(self, tablename, columns):
        query = "select " + columns + " from " + tablename
        print '\n'+query+'\n'
        mycursor.execute(query)
        mylist = mycursor.fetchall()
        for i in mylist:
            print(i)

class select_where:
    def __init__(self, tablename, columns, condition):
        self.condition = condition
        query = "select " + columns + " from " + tablename + " where " + condition
        print '\n'+query+'\n'
        mycursor.execute(query)
        mylist = mycursor.fetchall()
        for i in mylist:
            print(i)

class select_where_group:
    def __init__(self, tablename, columns, condition, coln):
        self.condition = condition
        query = "select " + columns + " from " + tablename + " where " + condition + " group by " + coln
        print '\n'+query+'\n'
        mycursor.execute(query)
        mylist = mycursor.fetchall()
        for i in mylist:
            print(i)

class select_where_group_order:
    def __init__(self, tablename, columns, condition, coln, order):
        self.condition = condition
        query = "select " + columns + " from " + tablename + " where " + condition + " group by " + coln + " order by " + order
        print '\n'+query+'\n'
        mycursor.execute(query)
        mylist = mycursor.fetchall()
        for i in mylist:
            print(i)

