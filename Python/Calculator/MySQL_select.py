#Create generic function to perform select operations that works for db.
#You can try to implement it by your understanding, just remember one function should support all db's and tables

import mysql.connector
import ConfigParser
import logging

conn = None

class DB_Queries:
    def __init__(self):
        self.configfilename = configfilename
        config = ConfigParser.SafeConfigParser()
        config.read('config.ini')
        user = config.get('mysqlconfig', 'user')
        host = config.get('mysqlconfig', 'host')
        pwd = config.get('mysqlconfig', 'password')
        dbname = config.get('mysqlconfig', 'dbname')
        #connection_attempts = config.getint('MySQLConfig', 'conectionAttempts')
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

#DB_Queries('root', 'letmein', 'localhost', 'classicmodels')
DB_Queries()
mycursor = conn.cursor()
select('employees', 'firstName, lastName, jobTitle')
select_where('employees', 'firstName, jobTitle', 'employeeNumber > 1100')
select_where_group('employees', 'firstName, employeeNumber, sum(officeCode)', 'employeeNumber > 1300', 'employeeNumber')
select_where_group_order('employees', 'lastName, employeeNumber, count(reportsTo)', 'employeeNumber > 1300', 'employeeNumber', 'lastName DESC')
mycursor.close()
