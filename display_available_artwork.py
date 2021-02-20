import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db

def display_avalible_artwork(artist):
    availible = 'Available'


    try:

        conn = sqlite3.connect(db)
        results =conn.execute('SELECT * FROM artwork WHERE ArtistName like ? AND Sold = ?', (artist, availible))
        records_found = results.fetchall()
        if records_found:
            print(f'Here is the avalible artwork for {artist}')
            print(records_found)
            return True
        else:
            print('Artwork not found')
            return False
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()


def display_avalible_artwork_test(artist):
    availible = 'Available'


    try:

        conn = sqlite3.connect(test_db)
        results =conn.execute('SELECT * FROM artwork WHERE ArtistName like ? AND Sold = ?', (artist, availible))
        records_found = results.fetchall()
        if records_found:
            print(f'Here is the avalible artwork for {artist}')
            print(records_found)
            return True
        else:
            print('Artwork not found')
            return False
    except sqlite3.Error as e:
        print(sql_error + e)
    conn.close()