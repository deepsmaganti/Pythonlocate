import mysql.connector
conn = mysql.connector.connect (user='root',password='letmein',host='localhost',database='calc_database')
mycursor=conn.cursor()
mycursor.execute("""insert into calc_values values
                (
                1, 21, 9
                )""")
mycursor.execute("""insert into calc_values values
                (
                2, 465, 234
                )""")
mycursor.execute("""insert into calc_values values
                (
                3, 64, 434
                )""")
mycursor.execute("""insert into calc_values values
                (
                4, 132, 77
                )""")
conn.commit()
mycursor.close()