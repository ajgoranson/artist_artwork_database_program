import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db

def find_all_artwork(artist):


    try:
        conn = sqlite3.connect(db)
        results = conn.execute('SELECT * FROM artwork WHERE ArtistName like ?', (artist, ))
        record_found = results.fetchall()
        if record_found:
            print(f'Here is all the artwork for {artist}: ')
            print(record_found)
            return True
        else:
            print('Artist not found please try again')
            return False
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()

def find_all_artwork_test(artist):


    try:
        conn = sqlite3.connect(test_db)
        results = conn.execute('SELECT * FROM artwork WHERE ArtistName like ?', (artist, ))
        record_found = results.fetchall()
        if record_found:
            print(f'Here is all the artwork for {artist}: ')
            print(record_found)
            return True
        else:
            print('Artist not found please try again')
            return False
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()