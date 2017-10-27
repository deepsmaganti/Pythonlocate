import unittest
import MySQL_queries
import mysql.connector


class test_queries(unittest.TestCase):
    def test_one(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.create('new_table','id int not null, firstname varchar(20), lastname varchar(20), title varchar(10), primary key (id)')
        self.assertEqual(self.out, None)
    def test_two_0(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 0, 'firstname' : 'Hello', 'lastname' : 'World', 'title':'Head'})
        self.assertEqual(self.out, None)
    def test_two_1(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 1, 'firstname' : 'Dipti', 'lastname' : 'Mag', 'title':'Engineer'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 2)
    def test_two_2(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 2, 'firstname' : 'Deepthi', 'lastname' : 'Yar', 'title':'Lead'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 3)
    def test_two_3(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 3, 'firstname' : 'Saanvi', 'lastname' : 'Yar', 'title':'Child'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 4)
    def test_two_4(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 4, 'firstname' : 'Raghu', 'lastname' : 'Yar', 'title':'Manager'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 5)
    def test_two_5(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 5, 'firstname' : 'Monica', 'lastname' : 'Geller', 'title':'Actor'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 6)
    def test_two_6(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 6, 'firstname' : 'Racheal', 'lastname' : 'Green', 'title':'Actor'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 7)
    def test_two_7(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.insert('new_table', {'id' : 7, 'firstname' : 'Pheebs', 'lastname' : 'Buffay', 'title':'Actor'})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', '*',{}, None)
        self.assertEqual(len(self.out), 8)
    def test_three(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', 'firstname',{}, None)
        self.assertEqual(len(self.out), 8)
    def test_four(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', 'firstname', {'firstname': 'Dipti'}, None)
        self.assertEqual(len(self.out), 1)
    def test_five(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', 'lastname, title', {'lastname': 'Yar'}, None)
        self.assertEqual(len(self.out), 3)
    def test_six(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', 'firstname, lastname, title',{'title' : 'Actor'}, None)
        self.assertEqual(len(self.out), 3)
    def test_seven(self):
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.update('new_table', {'firstname': 'HELLO', 'lastname' : 'WORLD'}, {'id' : 0})
        self.config = MySQL_queries.DB_Queries('config_testfile.ini')
        self.out = self.config.select('new_table', 'firstname',{'firstname':'HELLO'}, None)
        self.assertEqual(len(self.out), 0)
    # def test_seven(self):
    #     self.config = MySQL_queries.DB_Queries('config_testfile.ini')
    #     self.out = self.config.select('employees', 'firstName, lastName, jobTitle',
    #                        {'lastName': 'Bad', 'employeeNumber': 1143, 'firstName': 'Bill'}, 'OR')
    #     self.assertEqual(len(self.out), 1)

if __name__ == '__main__':
    unittest.main()
