from Utils import decorator_func
from colorama import Fore, Style, init
init()
import os
import time

Movies = {
    1: {
        'ID': 1,
        'Name': 'Interstellar',
        'Genre': 'Sci-Fi',
        'Duration': '2h 49m',
        'Rating': 8.7,
        'Price': 10,
        'Language': 'English',
        'Age Rating': 'PG-13',

        'Showtimes': {
            '14:00': {
                'A1': 'Booked', 'A2': 'Available', 'A3': 'Available',
                'A4': 'Booked', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Booked', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Booked',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Booked', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Booked',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Booked', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '17:00': {
                'A1': 'Available', 'A2': 'Available', 'A3': 'Booked',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Booked', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Booked', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Booked', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Booked', 'D6': 'Available',
                'E1': 'Booked', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '20:00': {
                'A1': 'Available', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Booked', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Booked',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Booked', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Booked',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Booked', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Booked',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            }
        }
    },

    2: {
        'ID': 2,
        'Name': 'Inception',
        'Genre': 'Sci-Fi / Thriller',
        'Duration': '2h 28m',
        'Rating': 8.8,
        'Price': 9,
        'Language': 'English',
        'Age Rating': 'PG-13',

        'Showtimes': {
            '13:00': {
                'A1': 'Booked', 'A2': 'Available', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Booked', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Booked',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Booked', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Booked', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Booked',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Booked', 'E5': 'Available', 'E6': 'Available'
            },

            '16:00': {
                'A1': 'Available', 'A2': 'Available', 'A3': 'Available',
                'A4': 'Booked', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Booked', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Booked', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Booked', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Booked', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Booked',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '21:00': {
                'A1': 'Booked', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Booked', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Booked',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Booked', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Booked',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Booked', 'E6': 'Available'
            }
        }
    },

    3: {
        'ID': 3,
        'Name': 'The Dark Knight',
        'Genre': 'Action / Crime',
        'Duration': '2h 32m',
        'Rating': 9.0,
        'Price': 11,
        'Language': 'English',
        'Age Rating': 'PG-13',

        'Showtimes': {
            '14:00': {
                'A1': 'Available', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Booked', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Booked',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Booked', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Booked',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Booked', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Booked', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '18:00': {
                'A1': 'Booked', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Booked',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Booked', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Booked',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Booked', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Booked',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '21:00': {
                'A1': 'Available', 'A2': 'Available', 'A3': 'Booked',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Booked', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Booked', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Booked', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Booked',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Booked', 'D5': 'Booked', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Booked', 'E5': 'Available', 'E6': 'Available'
            }
        }
    },

    4: {
        'ID': 4,
        'Name': 'Avatar',
        'Genre': 'Sci-Fi / Adventure',
        'Duration': '2h 42m',
        'Rating': 7.8,
        'Price': 12,
        'Language': 'English',
        'Age Rating': 'PG-13',

        'Showtimes': {
            '13:30': {
                'A1': 'Available', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Booked',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Booked', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Booked', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Booked', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Booked', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Booked',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '16:00': {
                'A1': 'Booked', 'A2': 'Available', 'A3': 'Available',
                'A4': 'Booked', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Booked', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Booked',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Booked', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Booked',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Booked', 'E5': 'Available', 'E6': 'Available'
            },

            '20:00': {
                'A1': 'Available', 'A2': 'Available', 'A3': 'Booked',
                'A4': 'Available', 'A5': 'Booked', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Booked', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Booked', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Booked',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Booked', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Booked', 'E6': 'Available'
            }
        }
    },

    5: {
        'ID': 5,
        'Name': 'The Matrix',
        'Genre': 'Sci-Fi / Action',
        'Duration': '2h 16m',
        'Rating': 8.7,
        'Price': 9,
        'Language': 'English',
        'Age Rating': 'R',

        'Showtimes': {
            '13:30': {
                'A1': 'Booked', 'A2': 'Available', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Booked', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Booked', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Available', 'B6': 'Booked',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Booked', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Booked',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Booked', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '17:30': {
                'A1': 'Available', 'A2': 'Booked', 'A3': 'Available',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Booked',
                'B1': 'Booked', 'B2': 'Available', 'B3': 'Available',
                'B4': 'Available', 'B5': 'Booked', 'B6': 'Available',
                'C1': 'Available', 'C2': 'Available', 'C3': 'Booked',
                'C4': 'Available', 'C5': 'Available', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Booked', 'D3': 'Available',
                'D4': 'Available', 'D5': 'Available', 'D6': 'Available',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Booked',
                'E4': 'Available', 'E5': 'Available', 'E6': 'Available'
            },

            '22:00': {
                'A1': 'Available', 'A2': 'Available', 'A3': 'Booked',
                'A4': 'Available', 'A5': 'Available', 'A6': 'Available',
                'B1': 'Available', 'B2': 'Available', 'B3': 'Booked',
                'B4': 'Booked', 'B5': 'Available', 'B6': 'Available',
                'C1': 'Booked', 'C2': 'Available', 'C3': 'Available',
                'C4': 'Available', 'C5': 'Booked', 'C6': 'Available',
                'D1': 'Available', 'D2': 'Available', 'D3': 'Available',
                'D4': 'Booked', 'D5': 'Available', 'D6': 'Booked',
                'E1': 'Available', 'E2': 'Available', 'E3': 'Available',
                'E4': 'Available', 'E5': 'Booked', 'E6': 'Available'
            }
        }
    }
}


# Show Seat Map
@decorator_func('Show Seat Map')
def Show_Seat_Map():
    try:
        ID = int(input('\nEnter Movie ID : '))
        print()

    except ValueError:
        print('❌ Enter only movie ID.')
        return

    found = False

    for index in Movies:
        if ID == Movies[index]['ID']:
            found = True

            print(f"🎬 {Movies[index]['Name']}\n")
            print('⏰ Showtimes:\n')

            index_2 = 1

            for timee in Movies[index]['Showtimes']:
                print(f'{index_2}. {timee}')
                index_2 += 1

            break

    if not found:
        print('❌ Movie ID not found.')
        return

    try:
        choice = int(input('\nEnter Showtime number : '))
        print()

    except ValueError:
        print('❌ Enter a number only.')
        return

    if choice < 1 or choice > len(Movies[index]['Showtimes']):
        print('❌ Invalid Showtime choice.')
        return

    selected_time = list(Movies[index]['Showtimes'])[choice - 1]

    os.system('clear')
    time.sleep(1)

    print(f"\n🎬 {Movies[index]['Name']}")
    print(f"⏰ Showtime: {selected_time}\n")

    print(f"           {Fore.RED}SCREEN{Style.RESET_ALL}")
    print( '-' * 30)
    print()

    index_of_seat = 0

    for seat, status in Movies[index]['Showtimes'][selected_time].items():

        if status == 'Available':
            print(
                f'{Fore.GREEN}{seat}{Style.RESET_ALL}',
                end='   '
            )

        elif status == 'Booked':
            print(
                f'{Fore.RED}{seat}{Style.RESET_ALL}',
                end='   '
            )

        index_of_seat += 1

        if index_of_seat == 6:
            print()
            index_of_seat = 0

    print()
    print(f'\n{Fore.GREEN}🟢 Available{Style.RESET_ALL}')
    print(f'{Fore.RED}🔴 Booked{Style.RESET_ALL}')
			
# Show Available Seat
@decorator_func('Show Available Seat')	
def Show_Available_Seat():
    try:
        ID = int(input('\nEnter Movie ID : '))
        print()

    except ValueError:
        print('❌ Enter only movie ID.')
        return

    found = False

    for index in Movies:
        if ID == Movies[index]['ID']:
            found = True

            print(f"🎬 {Movies[index]['Name']}\n")
            print('⏰ Showtimes:\n')

            index_2 = 1

            for timee in Movies[index]['Showtimes']:
                print(f'{index_2}. {timee}')
                index_2 += 1

            break

    if not found:
        print('❌ Movie ID not found.')
        return

    try:
        choice = int(input('\nEnter Showtime number : '))
        print()

    except ValueError:
        print('❌ Enter a number only.')
        return

    if choice < 1 or choice > len(Movies[index]['Showtimes']):
        print('❌ Invalid Showtime choice.')
        return

    selected_time = list(Movies[index]['Showtimes'])[choice - 1]

    os.system('clear')
    time.sleep(1)

    print(f"\n🎬 {Movies[index]['Name']}")
    print(f"⏰ Showtime: {selected_time}\n")
    
    

    print(f"           {Fore.RED}SCREEN{Style.RESET_ALL}")
    print('-' * 30)
    print()

    index_of_seat = 0
    seat_found = False

    for seat, status in Movies[index]['Showtimes'][selected_time].items():

        if status == 'Available':
            seat_found = True
            print(f'{Fore.GREEN}{seat}{Style.RESET_ALL}', end=' ')

        elif status == 'Booked':
            
            
            print('  ', end=' ')
            

        index_of_seat += 1

        if index_of_seat == 6:
            print()
            index_of_seat = 0
            
            
    if not seat_found:
    	print('❌ No available seats for this showtime.')
	


# Select Seat	
@decorator_func('Select Seat')
def Select_Seat():
    try:
        ID = int(input('\nEnter Movie ID : '))
        print()

    except ValueError:
        print('❌ Enter only movie ID.')
        return

    found = False

    for index in Movies:
        if ID == Movies[index]['ID']:
            found = True

            print(f"🎬 {Movies[index]['Name']}\n")
            print('⏰ Showtimes:\n')

            index_2 = 1

            for timee in Movies[index]['Showtimes']:
                print(f'{index_2}. {timee}')
                index_2 += 1

            break

    if not found:
        print('❌ Movie ID not found.')
        return

    try:
        choice = int(input('\nEnter Showtime number : '))
        print()

    except ValueError:
        print('❌ Enter a number only.')
        return

    if choice < 1 or choice > len(Movies[index]['Showtimes']):
        print('❌ Invalid Showtime choice.')
        return

    selected_time = list(Movies[index]['Showtimes'])[choice - 1]

    os.system('clear')
    time.sleep(1)

    print(f"\n🎬 {Movies[index]['Name']}")
    print(f"⏰ Showtime: {selected_time}\n")
    
    

    print(f"           {Fore.RED}SCREEN{Style.RESET_ALL}")
    print('-' * 30)
    print()

    index_of_seat = 0
    seat_found = False

    for seat, status in Movies[index]['Showtimes'][selected_time].items():

        if status == 'Available':
            seat_found = True
            print(f'{Fore.GREEN}{seat}{Style.RESET_ALL}', end='  ')

        elif status == 'Booked':
            
            print(f'{Fore.RED}{seat}{Style.RESET_ALL}', end='   ')

        index_of_seat += 1

        if index_of_seat == 6:
            print()
            index_of_seat = 0

    print()
    print(f'\n{Fore.GREEN}🟢 Available{Style.RESET_ALL}')
    print(f'{Fore.RED}🔴 Booked{Style.RESET_ALL}')
            
            
    if not seat_found:
            print('❌ No available seats for this showtime.')
            return
    	
    	
    seat_ID = input('Enter Seat ID : ').upper()
    	
    found_seat_ID = False 
    if seat_ID in Movies[index]['Showtimes'][selected_time]:
        found_seat_ID =True
    		
    if not found_seat_ID :
        print('❌ Invalid seat ID')
        return 
    		
    if Movies[index]['Showtimes'][selected_time][seat_ID] == 'Available' :
        print(f'✅ Seat {seat_ID} is available.')
    		
      
    else :
    	print(f'❌ Seat {seat_ID} is already booked.')


# Show Booked Seat
@decorator_func('Show Booked Seat')
def Show_Booked_Seat():
    try:
        ID = int(input('\nEnter Movie ID : '))
        print()

    except ValueError:
        print('❌ Enter only movie ID.')
        return

    found = False

    for index in Movies:
        if ID == Movies[index]['ID']:
            found = True

            print(f"🎬 {Movies[index]['Name']}\n")
            print('⏰ Showtimes:\n')

            index_2 = 1

            for timee in Movies[index]['Showtimes']:
                print(f'{index_2}. {timee}')
                index_2 += 1

            break

    if not found:
        print('❌ Movie ID not found.')
        return

    try:
        choice = int(input('\nEnter Showtime number : '))
        print()

    except ValueError:
        print('❌ Enter a number only.')
        return

    if choice < 1 or choice > len(Movies[index]['Showtimes']):
        print('❌ Invalid Showtime choice.')
        return

    selected_time = list(Movies[index]['Showtimes'])[choice - 1]

    os.system('clear')
    time.sleep(1)

    print(f"\n🎬 {Movies[index]['Name']}")
    print(f"⏰ Showtime: {selected_time}\n")

    print(f"           {Fore.RED}SCREEN{Style.RESET_ALL}")
    print('-' * 30)
    print()

    index_of_seat = 0
    seat_found = False

    for seat, status in Movies[index]['Showtimes'][selected_time].items():

        if status == 'Available':
            print('  ', end='  ')

        elif status == 'Booked':
            seat_found = True
            print(
                f'{Fore.RED}{seat}{Style.RESET_ALL}',
                end='  '
            )

        index_of_seat += 1

        if index_of_seat == 6:
            print()
            index_of_seat = 0

    print()

    if not seat_found:
        print('❌ No booked seats for this showtime.')
        
# Check_Seat
@decorator_func('Check_Seat')        
def Check_Seat():
    try:
        ID = int(input('\nEnter Movie ID : '))
        print()

    except ValueError:
        print('❌ Enter only movie ID.')
        return

    found = False

    for index in Movies:
        if ID == Movies[index]['ID']:
            found = True

            print(f"🎬 {Movies[index]['Name']}\n")
            print('⏰ Showtimes:\n')

            index_2 = 1

            for timee in Movies[index]['Showtimes']:
                print(f'{index_2}. {timee}')
                index_2 += 1

            break

    if not found:
        print('❌ Movie ID not found.')
        return

    try:
        Showtime_number = int(input('\nEnter Showtime number : '))
        print()

    except ValueError:
        print('❌ Enter a number only.')
        return
    
    if Showtime_number < 1 or Showtime_number > len(Movies[index]['Showtimes']):
        print('\n❌ Invalid Showtime choice.')
        return
    
    selected_time = list(Movies[index]['Showtimes'])[Showtime_number - 1]
    seat_id = input('\nEnter Seat ID : ').upper()
    
    if seat_id not in Movies[index]['Showtimes'][selected_time]:
        print('\n❌ Invalid Seat ID.')
        return
    
    
    print(f"\n🎬  {Movies[index]['Name']}")
    print(f'⏰  Showtimes : {selected_time}')
    print(f'💺  Seat : {seat_id}')
    
    
    if  Movies[index]['Showtimes'][selected_time][seat_id] == 'Available' :
        print(f'\n🟢 Seat {seat_id} is Available.')
        
    else :
        print(f'\n🔴 Seat {seat_id} is Booked.')
    

  
    