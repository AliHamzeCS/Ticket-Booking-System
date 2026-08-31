from BookingsHistory import Load_Bookings
from Movies import Movies
from Utils import decorator_func
import SettingsHistory

settings = SettingsHistory.Load_Settings()

Currency = settings['Currency']


# Search Movie
@decorator_func('Search Movie')
def search_movie():

    movie_name = input("Enter Movie Name : ").title()

    found = False

    for index in Movies:
        if movie_name == Movies[index]['Name']:
            found = True

            print('=' * 25, end='\n\n')

            for key, value in Movies[index].items():
                if key == 'Showtimes':
                    break

                elif key == 'Price':
                    print(f"{key} : {value}{Currency}")

                else:
                    print(f"{key} : {value}")

            print('=' * 25, end='\n\n')

    if not found:
        print('Movie not found')


# Search Bookings
@decorator_func('Search Bookings')
def search_bookings():

    Bookings = Load_Bookings()

    input_user = input('Enter Customer OR Movie Name : ').title()

    found = False

    for ID in Bookings:
        if input_user == Bookings[ID]['Movie Name'] or input_user == Bookings[ID]['Customer Name']:
            found = True

            print('=' * 25, end='\n\n')

            for key, value in Bookings[ID].items():

                if key == 'Price':
                    print(f"{key} : {value}{Currency}")

                else:
                    print(f"{key} : {value}")

            print('=' * 25, end='\n\n')

    if not found:
        print('Bookings not found')


# Search By Booking ID
@decorator_func('Search By Booking ID')
def search_by_booking_id():

    Bookings = Load_Bookings()

    try:
        ID = int(input("Enter Booking ID : "))

    except ValueError:
        print("Enter only booking id")
        return

    if ID not in Bookings:
        print('❌ Booking ID not found.')

    else:
        print('=' * 25, end='\n\n')

        for key, value in Bookings[ID].items():

            if key == 'Price':
                print(f"{key} : {value}{Currency}")

            else:
                print(f"{key} : {value}")

        print('=' * 25, end='\n\n')


# Search By Phone
@decorator_func('Search By Phone')
def search_by_phone():

    Bookings = Load_Bookings()

    phone_number = input('Enter Phone Number : ')

    found = False

    for ID in Bookings:
        if phone_number == Bookings[ID]['Phone']:
            found = True

            print('=' * 25, end='\n\n')

            for key, value in Bookings[ID].items():

                if key == 'Price':
                    print(f"{key} : {value}{Currency}")

                else:
                    print(f"{key} : {value}")

            print('=' * 25, end='\n\n')

    if not found:
        print('Bookings not found')