import sqlite3
from databaseurl import db
from databasesetup import sql_error
from databaseurl import test_db



def change_artwork_status_in_db(artist, artwork, change):



    artist = artist.strip().title()
    artwork = artwork.strip().title()

    if change == 0:
        change = 'Available'
    if change == 1:
        change = 'Sold'


    try:
        with sqlite3.connect(db) as conn:
            conn.execute('UPDATE artwork SET Sold = ? WHERE ArtistName = ? AND NameOfArtwork = ? ', (change, artist, artwork))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False

def change_artwork_status_in_db_test(artist, artwork, change):


    artist = artist.strip().title()
    artwork = artwork.strip().title()
    if change == 0:
        change = 'Available'
    if change == 1:
        change = 'Sold'


    try:
        with sqlite3.connect(test_db) as conn:
            conn.execute('UPDATE artwork SET Sold = ? WHERE ArtistName = ? AND NameOfArtwork = ? ', (change, artist, artwork))
        conn.close()
        return True
    except sqlite3.Error as e:
        print(sql_error + e)
        return False
