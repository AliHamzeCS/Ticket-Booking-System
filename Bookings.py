from Movies import Movies
from colorama import Fore, Style, init
init()
from Utils import decorator_func
import random
import os 
import time
import BookingsHistory
from random import randint
from CustomersHistory import Load_Customers
from CustomersHistory import Dump_Customers
import SettingsHistory

settings = SettingsHistory.Load_Settings()

Currency = settings['Currency']
Delay = settings['Screen Delay']


def reset_screen():
    os.system('clear')
    time.sleep(Delay)

Bookings = BookingsHistory.Load_Bookings()

# New Booking
@decorator_func('🎟️  New Booking')
def New_Booking():
    customers = Load_Customers()

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
            print(f"💰 Price : {Movies[index]['Price']}{Currency}")
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

    print('\n👤 CUSTOMER INFORMATION' , end="\n\n")

    
    print("1. Yes")
    print("2. No\n")  
    
    try :
        qs = int(input("Do you have a Customer ID? "))
    
    except ValueError :
        print("Enter only the number of choice")
        return
    
    if qs == 1:
        try :
            cust_id = int(input("Enter Customer ID: "))
            
        except ValueError :
            print("Enter only the Customer ID.")
            return
        
        customer_found = False
        if cust_id in customers:
            customer_found = True
            
        if not customer_found:
            print("❌ Customer ID not found.")
            return
        
        customer_name = customers[cust_id]['Customer Name']
        phone_number = customers[cust_id]['Customer Phone']
    
    elif qs == 2:
        
        cust_name = input("Enter Customer Name : ")
        cust_phone = input("Enter Customer Phone : ")
        cust_id = randint(999, 10000)
        
        while True:
            if cust_id not in customers:
                customers[cust_id] = {
                        'Customer Name': cust_name,
                        'Customer Phone': cust_phone
                    }
                Dump_Customers(customers)
                break
        
                
            else:
                cust_id = randint(999, 10000)
                
        print("✅ Customer created successfully!" , end="\n\n")
        
        print(f"🆔 Customer ID: {cust_id}")
        print(f"👤 Name: {cust_name}")
        print(f"📱 Phone: {cust_phone}")
    
    else :
        print("Enter only (1 or 2)")
        return
    
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
    print(f"💰 Price : {price}{Currency}\n")

    print('='*20, end = '\n\n')

    confirm_booking = input('Confirm Booking? (Y/N): ').lower()

    if confirm_booking == 'y':
        booking_data = {
            'Booking ID': booking_id,
            'Customer ID': cust_id,
            'Movie ID': movie_ID,
            'Movie Name': movie_name,
            'Showtime': selected_time,
            'Seat': seat_id,
            'Customer Name': customer_name,
            'Phone': phone_number,
            'Price': price,
            'Status': 'Confirmed'}
        BookingsHistory.Add_Booking(Bookings, booking_id, booking_data)
        Movies[indexx]['Showtimes'][selected_time][seat_id] = 'Booked'
        print(f'\n✅ Booking confirmed successfully!\n🎫 Booking ID: {booking_id}')
        

    else:
        print('\n❌ Booking cancelled.')
        
