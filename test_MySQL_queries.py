import unittest
import MySQL_queries
import mysql.connector


class test_queries(unittest.TestCase):
    def test_one(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('employees', 'firstName, lastName, jobTitle',
                           {'lastName': 'Bad', 'employeeNumber': 1143, 'firstName': 'Bill'}, 'OR')
        self.assertEqual(len(self.out), 1)
    def test_two(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('employees', 'firstName',{}, 'or')
        self.assertEqual(len(self.out), 25)
    def test_three(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('employees', 'firstName',{'firstname' : 'Dipti'}, 'or')
        self.assertEqual(len(self.out), 2)
    def test_four(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('employees', 'reportsTo, jobTitle',{'reportsTo' : 1143, 'jobTitle' : 'Sales Rep'}, 'and')
        self.assertEqual(len(self.out), 6)
    def test_five(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('employees', '*',{}, 'and')
        self.assertEqual(len(self.out), 25)
    def test_six(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.update('employees', {'employeeNumber': 1000, 'lastName' : 'Yar'}, {'firstName' : 'Dipti'})
        self.assertEqual(self.out, None)

if __name__ == '__main__':
    unittest.main()
