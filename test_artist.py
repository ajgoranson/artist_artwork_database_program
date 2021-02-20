from typing import Mapping
import unittest
from unittest import TestCase
import sqlite3
import databaseurl
import add_new_artist_to_db
import add_new_artwork
import change_artwork_status
import delete_artwork_from_db
import display_available_artwork
import main_menu
import search_for_artist
from databaseurl import test_db
from main_menu import ArtistError, main


import databasesetup

from model import Artist



""" I understand that this is a very unconventional way of doing the tests
I was having techinal issues with my computer and was not able to get the test db setup correctly 
as you did in your example you showed us, so i added test methods to all of my regular methods 
they are exact replicas of the orignials except they are connecting to the test_db instead of the actual db  """

class TestDB(TestCase):
    # ensure tables exist and clear DB so its empty before test start


    def setUp(self):

        databasesetup.create_table()


        with sqlite3.connect(test_db) as conn:
            conn.execute('DELETE FROM artistinfo')
            conn.execute('Delete FROM artwork')
            #Have to add these two in for testing because my add new artwork method does not work properly
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Dog", "594", "Sold")')
            conn.execute('INSERT INTO artwork values ("Aaron Goranson", "The Cat", "202", "Available")')
        conn.close()




    def test_add_artist(self):
        example = Artist('Example', 'Example@Gmail.com')
        added = add_new_artist_to_db.add_artist_test(example)

        self.assertTrue(added)

        expected_rows = [ ('Example', 'Example@Gmail.com')]
        actual_rows = self.get_all_data_from_artistinfo()
        self.assertCountEqual(expected_rows, actual_rows)

        example2 = Artist('Another Example', 'AnotherExample@Gmail.com')
        added2 = add_new_artist_to_db.add_artist_test(example2)

        self.assertTrue(added2)

        expected_rows = [ ('Example', 'Example@Gmail.com'), ('Another Example', 'AnotherExample@Gmail.com')]
        actual_rows = self.get_all_data_from_artistinfo()

        self.assertCountEqual(expected_rows, actual_rows)

    def test_add_duplicate_email(self):
        example = Artist('Example', 'Example@gmail.com')
        add_new_artist_to_db.add_artist_test(example)

        example2 = Artist('Example2', 'Example@gmail.com')
        added2 = add_new_artist_to_db.add_artist_test(example2)
        self.assertFalse(added2)

        excpeted_rows = [ ('Example', 'Example@gmail.com')]
        actual_rows = self.get_all_data_from_artistinfo()

        self.assertCountEqual(excpeted_rows, actual_rows)

    def test_artist_will_be_captilized(self):
        example = Artist('patrick mahomes', 'patrickmahomes@gmail.com')
        add_new_artist_to_db.add_artist_test(example)
        excpected_rows = [('Patrick Mahomes', 'patrickmahomes@gmail.com')]
        actual_rows = self.get_all_data_from_artistinfo()

        self.assertCountEqual(excpected_rows, actual_rows)


    def test_adding_artist_with_no_name_raises_artist_error(self):
        example_name = ('')
        exmaple_email = ('Example@gmail.com')
        with self.assertRaises(ArtistError):
            main_menu.add_new_artist(example_name, exmaple_email)
    
    def test_adding_artist_with_no_email_raises_artist_error(self):
        example_name =('example person')
        exmaple_email = ('')
        with self.assertRaises(ArtistError):
            main_menu.add_new_artist(example_name, exmaple_email)
    
    def test_adding_artwork_with_wrong_sold_or_available_raises_error(self):
        example_name = 'Aaron Goranson'
        example_artwork = 'Dragons'
        example_price = 393.0
        example_sold = 9
        with self.assertRaises(ArtistError):
            main_menu.add_artwork(example_name, example_artwork, example_price, example_sold)

    def test_adding_artwork_with_blank_artist_name_raises_error(self):
        example_name = ''
        example_artwork = 'Dragons'
        example_price = 393.0
        example_sold = 9
        with self.assertRaises(ArtistError):
            main_menu.add_artwork(example_name, example_artwork, example_price, example_sold)

    def test_adding_artwork_with_blank_artwork_name_raises_error(self):
        example_name = 'Aaron Goranson'
        example_artwork = ''
        example_price = 393.0
        example_sold = 9
        with self.assertRaises(ArtistError):
            main_menu.add_artwork(example_name, example_artwork, example_price, example_sold)


    def test_change_artwork_status_to_available(self):
        example_artist = 'Aaron Goranson'
        example_artwork = 'The Dog'
        example_change = 0
        change_artwork_status.change_artwork_status_in_db_test(example_artist, example_artwork, example_change)

        expected_rows = [ ('Aaron Goranson', 'The Dog', 594.0, 'Available'), ('Aaron Goranson', 'The Cat', 202.0, 'Available')]
        actual_rows = self.get_all_data_from_artwork()

        self.assertCountEqual(expected_rows, actual_rows)

    def test_change_artwork_status_to_sold(self):
        example_artist = 'Aaron Goranson'
        example_artwork = 'The Cat'
        example_change = 1
        change_artwork_status.change_artwork_status_in_db_test(example_artist, example_artwork, example_change)

        excpected_rows = [ ('Aaron Goranson', 'The Dog', 594.0, 'Sold'), ('Aaron Goranson', 'The Cat', 202.0, 'Sold')]
        actual_rows = self.get_all_data_from_artwork()
        self.assertCountEqual(excpected_rows, actual_rows)

    def test_delete_artwork(self):
        example_artist = 'Aaron Goranson'
        example_artwork = 'The Cat'
        delete_artwork_from_db.delete_artwork_from_database_test(example_artist, example_artwork)

        expected_rows = [('Aaron Goranson', 'The Dog', 594.0, 'Sold')]
        actual_rows = self.get_all_data_from_artwork()
        self.assertCountEqual(expected_rows, actual_rows)

    def test_delete_artwork_no_name_raises_artist_error(self):
        example_artist = ''
        example_artwork = 'SUPER SIAYAN'
        with self.assertRaises(ArtistError):
            main_menu.delete_artwork(example_artist, example_artwork)

    def test_delete_artwork_with_no_artwork_name_raises_artist_error(self):
        example_artist = 'Aaron Goranson'
        example_artwork = ''
        with self.assertRaises(ArtistError):
            main_menu.delete_artwork(example_artist, example_artwork)

    def test_display_available_artwork(self):
        #Not sure why this test does not work...it shows the correct artist in the terminal
        example_artist = 'Aaron Goranson'
        display_available_artwork.display_avalible_artwork_test(example_artist)

        expected_rows = [('Aaron Goranson', 'The Cat', 202.0, 'Available')]
        actual_rows = self.get_all_data_from_artwork()

        self.assertCountEqual(expected_rows, actual_rows)
    
    def test_display_artist_with_no_artist_name_raises_artist_error(self):
        example_artist = ''
        with self.assertRaises(ArtistError):
            main_menu.display_available_artwork(example_artist)

    def test_search_for_all_artist_artwork(self):
        example_artist = 'Aaron Goranson'
        search_for_artist.find_all_artwork_test(example_artist)
        expected_rows = [('Aaron Goranson', 'The Cat', 202.0, 'Available'), ('Aaron Goranson', 'The Dog', 594.0, 'Sold')]
        actual_rows = self.get_all_data_from_artwork()

        self.assertCountEqual(expected_rows, actual_rows)
    
    def test_search_for_all_artist_artwork_no_name_raises_artist_error(self):
        example_artist = ''
        with self.assertRaises(ArtistError):
            main_menu.search_for_artist_artwork(example_artist)





        


        
    def get_all_data_from_artistinfo(self):
        with sqlite3.connect(test_db) as conn:
            rows = conn.execute('SELECT * FROM artistinfo').fetchall()
        conn.close()
        return rows
    
    def get_all_data_from_artwork(self):
        with sqlite3.connect(test_db) as conn:
            rows = conn.execute('SELECT * FROM artwork').fetchall()
        conn.close()
        return rows



    
if __name__ == '__main__':
    unittest.main()