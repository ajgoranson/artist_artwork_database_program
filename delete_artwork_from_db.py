import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db


def delete_artwork_from_database(artist_name, artwork_name):
    

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('DELETE from artwork WHERE ArtistName = ? AND NameOfArtwork = ?', (artist_name, artwork_name))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False

def delete_artwork_from_database_test(artist_name, artwork_name):
    

    try:
        with sqlite3.connect(test_db) as conn:
            conn.execute('DELETE from artwork WHERE ArtistName = ? AND NameOfArtwork = ?', (artist_name, artwork_name))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False
        

