import sqlite3
from databaseurl import db
from databaseurl import test_db




def add_artist(artist):

        

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO artistinfo VALUES (?, ?)', (artist.name, artist.email))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False

def add_artist_test(artist):

    artist.name = artist.name.title().strip()



    try:
        with sqlite3.connect(test_db) as conn:
            conn.execute('INSERT INTO artistinfo VALUES (?, ?)', (artist.name, artist.email))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(e)
        return False