import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db

def add_artwork_to_db(artist_name, artwork_name, artwork_price, sold_or_availble):

    try:
        with sqlite3.connect(db) as conn:
            conn.execute('INSERT INTO artwork VALUES (?,?,?) WHERE ArtistName like ?', (artwork_name, artwork_price, sold_or_availble, artist_name))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False
 
def add_artwork_to_db_test(artist_name, artwork_name, artwork_price, sold_or_availble):

    try:
        with sqlite3.connect(test_db) as conn:
            conn.execute('INSERT INTO artwork VALUES (?,?,?) WHERE ArtistName like ?', (artwork_name, artwork_price, sold_or_availble, artist_name))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False