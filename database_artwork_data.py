import sqlite3
from databaseurl import db
from databaseurl import test_db
from databasesetup import sql_error

def insert_into_artwork():
    try:
        

        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Cat", "202", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Dog", "594", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Zebra", "500", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Lion", "984", "Sold")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "The Liger", "4931", "Available")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "Python", "999", "Sold")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "The Panda", "999999", "Available")')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def insert_into_test_db():
    try:
        

        with sqlite3.connect(test_db) as conn:
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Cat", "202", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Dog", "594", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Zebra", "500", "Available")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Lion", "984", "Sold")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "The Liger", "4931", "Available")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "Python", "999", "Sold")')
            conn.execute('INSERT INTO artwork values ("Tom Brady", "The Panda", "999999", "Available")')
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()




