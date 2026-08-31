from Bookings import Bookings
from Utils import decorator_func
from colorama import Fore, Style, init
init()
from Movies import Movies
import SettingsHistory
  
settings = SettingsHistory.Load_Settings()

Delay = settings['Screen Delay']
Currency = settings['Currency']

# Show All Bookings
@decorator_func('Show All Bookings')
def Show_All_Bookings():

    print(f'{Fore.CYAN}📋 ALL BOOKINGS{Style.RESET_ALL}\n')

    if not Bookings:
        print('❌ No bookings found.')
        return

    for booking_id, booking in Bookings.items():

        print(f'🎫 Booking ID : {booking["Booking ID"]}')
        print(f'🎬 Movie      : {booking["Movie Name"]}')
        print(f'⏰ Showtime   : {booking["Showtime"]}')
        print(f'💺 Seat       : {booking["Seat"]}')
        print(f'👤 Customer   : {booking["Customer Name"]}')
        print(f'📱 Phone      : {booking["Phone"]}')
        print(f'💰 Price      : {booking["Price"]}{Currency}')
        print(f'📌 Status     : {booking["Status"]}')

        print('-' * 35)
        
        
# Show My Bookings
@decorator_func('Show My Bookings')        
def Show_My_Bookings():

    print(f'{Fore.CYAN}📋 MY BOOKINGS{Style.RESET_ALL}\n')

    if not Bookings:
        print('❌ No bookings found.')
        return

    phone = input('Enter your phone number: ')

    found = False

    for booking_id, booking in Bookings.items():

        if booking['Phone'] == phone:

            found = True

            print(f'\n🎫 Booking ID : {booking["Booking ID"]}')
            print(f'🎬 Movie      : {booking["Movie Name"]}')
            print(f'⏰ Showtime   : {booking["Showtime"]}')
            print(f'💺 Seat       : {booking["Seat"]}')
            print(f'👤 Customer   : {booking["Customer Name"]}')
            print(f'📱 Phone      : {booking["Phone"]}')
            print(f'💰 Price      : {booking["Price"]}{Currency}')
            print(f'📌 Status     : {booking["Status"]}')

            print('-' * 35)

    if not found:
        print(f'\n❌ No bookings found for phone number: {phone}')
        
        
# Booking Details 
@decorator_func('Booking Details')   
def Booking_Details():

    print(f'{Fore.CYAN}📋 BOOKING DETAILS{Style.RESET_ALL}\n')

    if not Bookings:
        print('❌ No bookings found.')
        return

    try:
        booking_id = int(input('Enter Booking ID: '))

    except ValueError:
        print('❌ Enter numbers only.')
        return

    if booking_id not in Bookings:
        print('❌ Booking ID not found.')
        return

    booking = Bookings[booking_id]

    print('\n' + '=' * 35)
    print('BOOKING DETAILS')
    print('=' * 35)

    print(f'🎫 Booking ID : {booking["Booking ID"]}')
    print(f'🎬 Movie      : {booking["Movie Name"]}')
    print(f'⏰ Showtime   : {booking["Showtime"]}')
    print(f'💺 Seat       : {booking["Seat"]}')
    print(f'👤 Customer   : {booking["Customer Name"]}')
    print(f'📱 Phone      : {booking["Phone"]}')
    print(f'💰 Price      : {booking["Price"]}{Currency}')
    print(f'📌 Status     : {booking["Status"]}')

    print('=' * 35)
    

# Cancel Booking
@decorator_func('Cancel Booking')
def Cancel_Booking():

    print(f'{Fore.CYAN}❌ CANCEL BOOKING{Style.RESET_ALL}\n')

    if not Bookings:
        print('❌ No bookings found.')
        return

    try:
        booking_id = int(input('Enter Booking ID: '))

    except ValueError:
        print('❌ Enter numbers only.')
        return

    if booking_id not in Bookings:
        print('❌ Booking ID not found.')
        return

    booking = Bookings[booking_id]

    print('\n' + '=' * 35)
    print('BOOKING INFORMATION')
    print('=' * 35)

    print(f'🎫 Booking ID : {booking["Booking ID"]}')
    print(f'🎬 Movie      : {booking["Movie Name"]}')
    print(f'⏰ Showtime   : {booking["Showtime"]}')
    print(f'💺 Seat       : {booking["Seat"]}')
    print(f'👤 Customer   : {booking["Customer Name"]}')
    print(f'📱 Phone      : {booking["Phone"]}')
    print(f'💰 Price      : {booking["Price"]}{Currency}')
    print(f'📌 Status     : {booking["Status"]}')

    print('=' * 35)

    confirm = input('\nCancel this booking? (Y/N): ').lower()

    if confirm != 'y':
        print('\n❌ Cancellation cancelled.')
        return

    booking['Status'] = 'Cancelled'
    movie_id = booking['Movie ID']
    showtime = booking['Showtime']
    seat = booking['Seat']

    Movies[movie_id]['Showtimes'][showtime][seat] = 'Available'

    print('\n✅ Booking cancelled successfully.')
    
    
    
# Modify Booking
@decorator_func('Modify Booking')
def Modify_Booking():

    print('🔧 Modify Booking')

    try:
        booking_id = int(input('\nEnter Booking ID: '))

    except ValueError:
        print('❌ Enter numbers only.')
        return

    # Check Booking ID
    if booking_id not in Bookings:
        print('\n❌ Booking ID not found.')
        return

    booking = Bookings[booking_id]

    # Check Booking Status
    if booking['Status'] == 'Cancelled':
        print('\n❌ Cannot modify a cancelled booking.')
        return

    print('\n' + '=' * 30)
    print('CURRENT BOOKING')
    print('=' * 30)

    print(f"🎫 Booking ID : {booking['Booking ID']}")
    print(f"🎬 Movie      : {booking['Movie Name']}")
    print(f"⏰ Showtime   : {booking['Showtime']}")
    print(f"💺 Seat       : {booking['Seat']}")
    print(f"👤 Customer   : {booking['Customer Name']}")
    print(f"📱 Phone      : {booking['Phone']}")
    print(f"💰 Price      : {booking['Price']}{Currency}")
    print(f"📌 Status     : {booking['Status']}")

    print('\n' + '=' * 30)

    print('\n🔧 What do you want to modify?\n')

    print('1. Change Showtime')
    print('2. Change Seat')
    print('3. Change Customer Name')
    print('4. Change Phone')
    print('5. Back')

    try:
        choice = int(input('\nChoice: '))

    except ValueError:
        print('❌ Enter a number only.')
        return

    # Change Showtime
    if choice == 1:

        movie_id = booking['Movie ID']
        current_time = booking['Showtime']
        seat_id = booking['Seat']

        print('\n⏰ Available Showtimes:\n')

        showtimes = list(Movies[movie_id]['Showtimes'])

        for i, showtime in enumerate(showtimes, 1):
            print(f'{i}. {showtime}')

        try:
            time_choice = int(input('\nEnter Showtime Number: '))

        except ValueError:
            print('❌ Enter a number only.')
            return

        if time_choice < 1 or time_choice > len(showtimes):
            print('❌ Invalid Showtime number.')
            return

        new_time = showtimes[time_choice - 1]

        if new_time == current_time:
            print('\n❌ This is already your current showtime.')
            return

        # Check same seat in new showtime
        new_seat_status = Movies[movie_id]['Showtimes'][new_time][seat_id]

        if new_seat_status == 'Booked':
            print(
                f'\n❌ Seat {seat_id} is already booked '
                f'for {new_time}.'
            )
            return

        # Release old seat
        Movies[movie_id]['Showtimes'][current_time][seat_id] = 'Available'

        # Book same seat in new showtime
        Movies[movie_id]['Showtimes'][new_time][seat_id] = 'Booked'

        # Update Booking
        booking['Showtime'] = new_time

        print('\n✅ Showtime modified successfully.')

    # Change Seat
    elif choice == 2:

        movie_id = booking['Movie ID']
        current_time = booking['Showtime']
        current_seat = booking['Seat']

        print(f'\n🎬 Movie: {booking["Movie Name"]}')
        print(f'⏰ Showtime: {current_time}\n')

        print('💺 Seats:\n')

        for seat, status in Movies[movie_id]['Showtimes'][current_time].items():

            if status == 'Available':
                print(
                    f'{Fore.GREEN}{seat}{Style.RESET_ALL}',
                    end='  '
                )

            else:
                print(
                    f'{Fore.RED}{seat}{Style.RESET_ALL}',
                    end='  '
                )

        print('\n')

        new_seat = input('Enter New Seat ID: ').upper()

        if new_seat not in Movies[movie_id]['Showtimes'][current_time]:
            print('\n❌ Invalid Seat ID.')
            return

        if new_seat == current_seat:
            print('\n❌ This is already your current seat.')
            return

        if Movies[movie_id]['Showtimes'][current_time][new_seat] == 'Booked':
            print(f'\n❌ Seat {new_seat} is already booked.')
            return

        # Release old seat
        Movies[movie_id]['Showtimes'][current_time][current_seat] = 'Available'

        # Book new seat
        Movies[movie_id]['Showtimes'][current_time][new_seat] = 'Booked'

        # Update Booking
        booking['Seat'] = new_seat

        print('\n✅ Seat modified successfully.')

    # Change Customer Name
    elif choice == 3:

        new_name = input('\nEnter New Customer Name: ').title()

        if new_name == '':
            print('\n❌ Name cannot be empty.')
            return

        booking['Customer Name'] = new_name

        print('\n✅ Customer name modified successfully.')

    # Change Phone
    elif choice == 4:

        new_phone = input('\nEnter New Phone Number: ')

        if new_phone == '':
            print('\n❌ Phone number cannot be empty.')
            return

        booking['Phone'] = new_phone

        print('\n✅ Phone number modified successfully.')

    # Back
    elif choice == 5:

        print('\n↩️ Returning...')

    else:

        print('\n❌ Invalid choice.')