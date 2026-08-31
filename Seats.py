from Utils import decorator_func
from colorama import Fore, Style, init
init()
import os
import time
import SettingsHistory
from Movies import Movies   
settings = SettingsHistory.Load_Settings()

Delay = settings['Screen Delay']
Currency = settings['Currency']


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
    time.sleep(Delay)

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
    time.sleep(Delay)

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
    time.sleep(Delay)

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
    time.sleep(Delay)

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
    

  
    