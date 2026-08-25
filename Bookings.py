from Movies import Movies
from colorama import Fore, Style, init
init()
from Utils import decorator_func
import random
import os 
import time

def reset_screen():
    os.system('clear')
    time.sleep(1)

Bookings = {}


# New Booking
@decorator_func('🎟️  New Booking')
def New_Booking():
    

    try:
        movie_ID = int(input('\nEnter Movie ID: '))

    except ValueError:
        print('\nEnter the ID of movie ')
        return

    found = False

    for index in Movies:
        if movie_ID == Movies[index]['ID']:
            found = True
            print(f"\n🎬 Movie : {Movies[index]['Name']}")
            print(f"💰 Price : {Movies[index]['Price']}$")
            break

    if not found:
        print('\n❌ Movie ID not found ')
        return
    
    

    print(f"\n🎬 {Movies[index]['Name']}")
    print(f'\n⏰ Showtimes : \n')

    index_time = 1
    for index in Movies:
        if movie_ID == Movies[index]['ID']:
            indexx = index
            for times in Movies[index]['Showtimes']:
                print(f'{index_time}. {times}')
                index_time += 1

    movie_name = Movies[indexx]['Name']
    price = Movies[indexx]['Price']

    try:
        st_num = int(input('\nEnter Showtime Number: '))

    except ValueError:
        print('Select only one of three times ')
        return
    
    reset_screen()
        
    if st_num < 1 or st_num > len(Movies[indexx]['Showtimes']):
        print('\n❌ Invalid Showtime number.')
        return

    selected_time = list(Movies[indexx]['Showtimes'])[st_num-1]

    print(f"\n🎬 {Movies[indexx]['Name']}")
    print(f'⏰ Showtimes : {selected_time}\n')

    screen = 'Screen'
    print(screen.center(25,' '))
    print('-'*25, end = '\n\n')
    
    cut = 0
    for seat, status in Movies[indexx]['Showtimes'][selected_time].items():

        if cut == 6:
            print()
            cut = 0

        if status == 'Available':
            print(f'{Fore.GREEN}{seat}{Style.RESET_ALL}', end = ' ')

        if status == 'Booked':
            print(f'{Fore.RED}{seat}{Style.RESET_ALL}', end = ' ')

        cut += 1

    print(f'\n\n🟢 Available')
    print(f'🔴 Booked')

    seat_id = input('\nEnter seat ID: ').upper()

    if seat_id in Movies[indexx]['Showtimes'][selected_time]:
        if Movies[indexx]['Showtimes'][selected_time][seat_id] == 'Available':
            print(f'\n✅ seat {seat_id} is available')
        else:
            print(f'\n❌ seat {seat_id} is booked')
            return
    else:
        print(f'\n❌ {seat_id} is not founded')
        return
    
    reset_screen()

    print('\n👤 CUSTOMER INFORMATION')

    customer_name = input('\nEnter Customer Name: ').title()
    phone_number = input('Enter phone number: ')
    
    while True:
        booking_id = random.randint(1000, 100000)

        if booking_id not in Bookings:
            break

            
    reset_screen()
    
    print('='*20)
    print('BOOKING SUMMARY')
    print('='*20, end = '\n\n')

    print(f'🎫 Booking ID : {booking_id}\n')
    print(f"🎬 Movie : {movie_name}")
    print(f"⏰ Showtime : {selected_time}")
    print(f"💺 Seat : {seat_id}\n")
    print(f"👤 Customer : {customer_name}")
    print(f"📱 Phone : {phone_number}\n")
    print(f"💰 Price : {price}$\n")

    print('='*20, end = '\n\n')

    confirm_booking = input('Confirm Booking? (Y/N): ').lower()

    if confirm_booking == 'y':
        Bookings[booking_id] = {
            'Booking ID': booking_id,
            'Movie ID': movie_ID,
            'Movie Name': movie_name,
            'Showtime': selected_time,
            'Seat': seat_id,
            'Customer Name': customer_name,
            'Phone': phone_number,
            'Price': price,
            'Status': 'Confirmed'
        }
        Movies[indexx]['Showtimes'][selected_time][seat_id] = 'Booked'
        print(f'\n✅ Booking confirmed successfully!\n🎫 Booking ID: {booking_id}')
        

    else:
        print('\n❌ Booking cancelled.')
        
