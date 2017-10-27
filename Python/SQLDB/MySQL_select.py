#Create generic function to perform select operations that works for db.
#You can try to implement it by your understanding, just remember one function should support all db's and tables

import mysql.connector
import ConfigParser
import time
import logging
import datetime

class DB_Queries:
    def __init__(self):
        logging.basicConfig(filename=str(datetime.date.today())+'logfile.log', level=logging.DEBUG)
        config = ConfigParser.ConfigParser()
        config.read('config.ini')
        user = config.get('mysqlconfig', 'user')
        host = config.get('mysqlconfig', 'host')
        pwd = config.get('mysqlconfig', 'password')
        dbname = config.get('mysqlconfig', 'dbname')
        conn_attempts = config.get('mysqlconfig', 'connection_Attempts')
        for i in range(int(conn_attempts)):
            try:
                logging.info('Connecting to the MySQL database')
                self.conn = mysql.connector.connect(user=user, password=pwd, host=host, database=dbname)
                if self.conn:
                    logging.info('Connection Successful')
                    break
            except mysql.connector.Error as err:
                logging.warning(str(err))
                print 'Something went wrong... Retrying'
                time.sleep(3)
        return

    def select(self, tablename, columns, cond, ao):
        self.cond = cond
        mycursor = self.conn.cursor()
        try:
            if cond == {}:
                query = "select " + columns + " from " + tablename
            else:
                query = "select " + columns + " from " + tablename + " where " + self.where_str(cond, ao)
            logging.info(' SQL Query Executed: ' + query)
            mycursor.execute(query)
            mylist = mycursor.fetchall()
            logging.info('SQL query data fetched')
            for i in mylist:
                print i
            return mylist
        except mysql.connector.Error as err:
            logging.error(str(err))
        finally:
            mycursor.close()
            self.conn.close()

    def where_str(self, cond, ao):
        string = ""
        for i in (range(len(cond.keys()) - 1)):
            if (ao == 'AND' or ao == 'and'):
                if type(cond.values()[i]) == int:
                    string = string + cond.keys()[i] + " = " + str(cond.values()[i]) + " and "
                elif type(cond.values()[i]) == str:
                    string = string + cond.keys()[i] + " = '" + str(cond.values()[i]) + "' and "
            if (ao == 'OR' or ao == 'or'):
                if type(cond.values()[i]) == int:
                    string = string + cond.keys()[i] + " = " + str(cond.values()[i]) + " or "
                elif type(cond.values()[i]) == str:
                    string = string + cond.keys()[i] + " = '" + str(cond.values()[i]) + "' or "
        if type(cond.values()[len(cond.keys()) - 1]) == int:
            string_l = string + cond.keys()[len(cond.keys()) - 1] + " = " + str(cond.values()[len(cond.keys()) - 1]) + ""
        elif type(cond.values()[len(cond.keys()) - 1]) == str:
            string_l = string + cond.keys()[len(cond.keys()) - 1] + " = '" + str(cond.values()[len(cond.keys()) - 1]) + "'"
        return string_l

    def insert(self, tablename, namesvalues):
        self.tablename = tablename
        self.namesvalues = namesvalues
        mycursor = self.conn.cursor()
        try:
            columns = ','.join("%s" % i for i in namesvalues.keys())
            values = []
            for i in range(len(namesvalues.values())):
                if type(namesvalues.values()[i]) == str:
                    values.append("'" + str(namesvalues.values()[i]) + "'")
                elif type(namesvalues.values()[i]) == int:
                    values.append(namesvalues.values()[i])
            valuesjoin = ','.join("%s" % i for i in values)
            query = "insert into %s (%s) values (%s)" % (tablename, columns, valuesjoin)
            logging.info(' SQL Query Executed: ' + query)
            mycursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            logging.error(str(err))
        finally:
            mycursor.close()
            self.conn.close()

    def update(self, tablename, update, cond):
        self.tablename = tablename
        self.update = update
        self.cond = cond
        mycursor = self.conn.cursor()
        try:
            string = ''
            for i in range(len(update.values())-1):
                if type(update.values()) == str:
                    string = update.keys() + " = '" + str(update.values()) + "' , "
                    print string
                elif type(update.values()) == int:
                    string = update.keys() + " = " + update.values() + ", "
                    print string
            if type(update.values()[len(update.keys()) - 1]) == int:
                string_l = string + update.keys()[len(update.keys()) - 1] + " = " + str(update.values()[len(update.keys()) - 1]) + ""
            elif type(update.values()[len(update.keys()) - 1]) == str:
                string_l = string + update.keys()[len(update.keys()) - 1] + " = '" + str(update.values()[len(cond.keys()) - 1]) + "'"
            query = "update {} set {} where {}".format(tablename, string_l, self.where_str(cond,'AND'))
            logging.info(' SQL Query Executed: ' + query)
            mycursor.execute(query)
            self.conn.commit()
        except mysql.connector.Error as err:
            logging.error(str(err))
        finally:
            mycursor.close()
            self.conn.close()

xyz = DB_Queries()
#xyz.select('employees', 'firstName, lastName, jobTitle',
           #{'lastName': 'Bad', 'employeeNumber': 1143, 'firstName': 'Bill'}, 'OR')
#xyz.insert('employees', {'employeeNumber': 999, 'firstName': 'Dipti', 'lastName': 'Mag', 'extension': 5388,
                         #'email' : 'dm@gmail.com', 'officeCode' : 1, 'reportsTo' : 1056, 'JobTitle' : 'PE'})
xyz.update('employees', {'employeeNumber': 1000, 'lastName' : 'Yar'}, {'firstName' : 'Dipti'})