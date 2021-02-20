from databasesetup import create_table
from databasesetup import create_test_table
from model import Artist
import add_new_artist_to_db
import search_for_artist
import display_available_artwork
import add_new_artwork
import delete_artwork_from_db
import change_artwork_status




class ArtistError(Exception):
    pass

def main():
    create_table()
    create_test_table()


    print('Welcome to the Artists Musume')

    while True:


        selection = int(input('Please select from one of the following options \n'
        + ' 1 = Add a new artist \n'
        + ' 2 = Search for artwork by an artist \n'
        + ' 3 = Display all avalible artwork by an artist \n'
        + ' 4 = Add a new artwork to an existing artist \n'
        + ' 5 = Delete an artwork \n'
        + ' 6 = Change the status of an artwork \n'
        + ' Press any other number to quit: '))

        if selection == 1:
            add_new_artist(new_name = input('Please enter the name of the artist: ').strip().title(), new_email = input('Please enter the email of the artist: '))
        elif selection == 2:
            search_for_artist_artwork(artist_name = input('Please enter the name of the artist you would like to view: '))
        elif selection == 3:
            find_avalible_artwork(artist_name = input('Please enter the artist name you are looking for: '))
        elif selection == 4:
            add_artwork(artist_name = input('Please enter the artist name to add artwork: ').strip().title(), artwork_name = input('Please enter the name of the artwork: ').strip().title(), artwork_price = float(input('Please enter the price of the artwork: ')), sold_or_available = int(input('Please enter 0 for "Available" if the artwork is availible or 1 for "Sold" if sold: ')))
        elif selection == 5:
            delete_artwork(artist_name = input('Please enter the name of the artist ').strip().title(), artwork_name = input('Please enter the name of the artwork to delete ').strip().title())
        elif selection == 6:
            change_status_of_artwork(artist_name = input('Please enter the artist name: '), artwork_name = input('Please enter the artwork name: '), change = int(input('Please enter 0 for availible or 1 for sold: ')))
        else:
            exit()


# This method works correctly as needed
def add_new_artist(new_name, new_email):


    new_name = new_name.title().strip()
    
    if new_name == '':
        raise ArtistError('You need to place information to add a new artist')
    
    if new_email == '':
        raise ArtistError('You need to place inforamtion to add a new artist')
        
    artist = Artist(new_name, new_email)
    added = add_new_artist_to_db.add_artist(artist)

    if added:
        print('Added Artist')
    else:
        raise ArtistError('Error adding artist')

# Only "Aaron Goranson", and "Tom Brady" are artists you can find artwork for
def search_for_artist_artwork(artist_name):

    artist_name.strip().title()

    if artist_name == '':
        raise ArtistError('You need to place information to view artwork')

    search = search_for_artist.find_all_artwork(artist_name)

    if search:
        print('Here is all of your information')
        print(search)
    else:
        raise ArtistError('Sorry there was an error searching for their artwork')

    

# Only "Aaron Goranson", and "Tom Brady" are artists you can find artwork for
def find_avalible_artwork(artist_name):

    artist_name = artist_name.strip().title()

    if artist_name == '':
        raise ArtistError('You need to place information to view artwork')

    find = display_available_artwork.display_avalible_artwork(artist_name)

    if find:
        print('Here is the avalible artwork')
        print(find)
    else:
        raise ArtistError('Cannot find any artwork availible')



# Does not work unfortunetly
def add_artwork(artist_name, artwork_name, artwork_price, sold_or_available):

    artist_name = artist_name.strip().title()
    artwork_name = artwork_name.strip().title()

    if artist_name == '':
        raise ArtistError('You must put a name to add artwork')

    if artwork_name == '':
        raise ArtistError('You must put an artwork name to add artwork')

    if sold_or_available == 1:
        sold_or_availible = 'Sold'
    elif sold_or_available == 0:
        sold_or_available = 'Available'
    else:
        raise ArtistError('You must place either 0 or 1')

    adding = add_new_artwork.add_artwork_to_db(artist_name, artwork_name, artwork_price, sold_or_availible)
    if adding:
        print('Added to the database')
    else:
        raise ArtistError('Cannot add artwork')

# Must look at the database to find what artwork is available to delete since adding artwork method does not work
def delete_artwork(artist_name, artwork_name):

    if artist_name == '':
        raise ArtistError('You need to place information to add a new artist')
    
    if artwork_name == '':
        raise ArtistError('You need to place inforamtion to add a new artist')

    delete = delete_artwork_from_db.delete_artwork_from_database(artist_name, artwork_name)

    if delete:
        print(f'Successfully Deleted {artwork_name}')
    else:
        raise ArtistError('Cannot delete artwork at this time')


# Must look at the database to find what the status of the artwork is and do the opposite for results
def change_status_of_artwork(artist_name, artwork_name, change):

    changed = change_artwork_status.change_artwork_status_in_db(artist_name, artwork_name, change)

    if change == 0:
        change = 'Availible'
    if change == 1:
        change = 'Sold'
    else:
        raise ArtistError('Please put the correct numbers 0 for availible 1 for sold')

    if changed:
        print(f' Successfully changed the {artwork_name} to {change} ')
    else:
        raise ArtistError('Cannot change artwork status at this time')
    

if __name__ == '__main__':
    main()

