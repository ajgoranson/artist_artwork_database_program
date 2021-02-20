import sqlite3
from databaseurl import db
from databaseurl import test_db



sql_error = 'SQL Error please try again'

class ArtistError(Exception):
    pass

def create_table():
    try:

        with sqlite3.connect(db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artistinfo (Name TEXT, Email TEXT UNIQUE)')
            conn.execute('CREATE TABLE IF NOT EXISTS artwork (ArtistName TEXT, NameOfArtwork TEXT UNIQUE, Price REAL, Sold TEXT, FOREIGN KEY(ArtistName) REFERENCES artistinfo(Name))')
        conn.close()    
    except sqlite3.Error as e:
        print(sql_error + e)

def create_test_table():
    try:
        with sqlite3.connect(test_db) as conn:
            conn.execute('CREATE TABLE IF NOT EXISTS artistinfo (Name TEXT, Email TEXT UNIQUE)')
            conn.execute('CREATE TABLE IF NOT EXISTS artwork (ArtistName TEXT, NameOfArtwork TEXT UNIQUE, Price REAL, Sold TEXT, FOREIGN KEY(ArtistName) REFERENCES artistinfo(Name))')
        conn.close()    
    except sqlite3.Error as e:
        print(sql_error + e)

        
