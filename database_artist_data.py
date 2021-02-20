import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db


def insert_example_data():
    try:

        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO artistinfo values ("Aaron Goranson", "aj.goranson5@gmail.com")')
            conn.execute('INSERT INTO artistinfo values ("Tom Brady", "TomBrady@gmail.com")')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def insert_example_data_into_test():
    try:

        with sqlite3.connect(test_db) as conn:
            conn.execute('INSERT INTO artistinfo values ("Aaron Goranson", "aj.goranson5@gmail.com")')
            conn.execute('INSERT INTO artistinfo values ("Tom Brady", "TomBrady@gmail.com")')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

