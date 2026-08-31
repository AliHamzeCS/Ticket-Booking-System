from colorama import Fore, Style, init
init()

import os 
import time 
import Movies
import Seats
import Bookings
import BookingManager
import Customer
import Search
import Statistics
import Settings
import SettingsHistory
import Help
  
settings = SettingsHistory.Load_Settings()

Delay = settings['Screen Delay']
Currency = settings['Currency']

# Sleep Function
def sleep():
    time.sleep(Delay)

# Clear Screen Function    
def clear_screen():
    os.system('clear')
    
def clear__and_sleap():
    clear_screen()
    sleep()

# Back Function    
def reset_screen():
    clear_screen()
    sleep()
    
# Options Function    
def View_Options(*options):
    index = 1
    for option in options:
        print(f'{Fore.CYAN}{index}{Style.RESET_ALL}. {option}')
        index += 1
    
clear_screen()

# Main While
while True:
    #TICKET BOOKING SYSTEM 
    TBS = '🎟️  TICKET BOOKING SYSTEM'
    print('='*40)
    print(TBS.center(40,' '))
    print('='*40, end = '\n\n')
    
    View_Options(
        'Show Movies',
        'Available Seats',
        'Book Ticket',
        'Manage Bookings',
        'Search Booking',
        'Customer',
        'Statistics',
        'Settings',
        'Help',
        'Exit'
    )
    
    try:
        choice = int(input('\nChoice : '))
        
    except ValueError:
        print('\nError: Please enter a number.')
        sleep()
        clear_screen()
        continue
    
    if choice == 1:
        
        clear_screen()  
        sleep()
        
        while True:
            
            print(f'{Fore.WHITE}-Show Movies-{Style.RESET_ALL}\n')
            
            View_Options(
                'Show All Movies',
                'Search Movies',
                'Movie Details',
                'Show Movie Schedule',
                'Filter Movies',
                'Back'
            )
            
            try:
                m_choice = int(input('\nChoice : '))
            
            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue
                
            if  m_choice == 1 :
                
                clear__and_sleap()
                Movies.Show_All_Movies()
                clear__and_sleap()
                	
            elif m_choice == 2 :
                clear__and_sleap()
                Movies.Search_Movies()
                clear__and_sleap()
                
            elif m_choice == 3 :
                clear__and_sleap()
                Movies.Movie_Details()
                clear__and_sleap()
                	
            elif m_choice == 4 :
                clear__and_sleap()
                Movies.Show_Movie_Schedule()
                clear__and_sleap()
                	
            elif m_choice == 5 :
                
                clear_screen()
                sleep()
                
                while True:
                            
                    print(f'{Fore.LIGHTBLUE_EX}-Filter Movies-{Style.RESET_ALL}\n')
                            
                    View_Options(
                                'Filter By Genre',
                                'Filter By Rating',
                                'Filter By Price',
                                'Filter By Language',
                                'Back'
                            )
                            
                    try:
                        fm_choice = int(input('\nChoice : '))
                            
                    except ValueError:
                        print('\nError: Please enter a number.')
                        sleep()
                        clear_screen()
                        continue
                    
                    if fm_choice == 1:
                        
                        clear__and_sleap()
                        Movies.Filter_By_Genre()
                        clear__and_sleap()
                        
                    elif fm_choice == 2:
                        
                        clear__and_sleap()
                        Movies.Filter_By_Rating()
                        clear__and_sleap()
                        
                    elif fm_choice == 3:
                        
                        clear__and_sleap()
                        Movies.Filter_By_Price()
                        clear__and_sleap()
                        
                    elif fm_choice == 4:
                        
                        clear__and_sleap()
                        Movies.Filter_By_Language()
                        clear__and_sleap()
                        
                    elif fm_choice == 5:
                        reset_screen()
                        break
                        
                	
            elif m_choice == 6 :
                reset_screen()
                break
                
    elif choice == 2:
        clear_screen()  
        sleep()
                
        while True:
                    
            print(f'{Fore.WHITE}-Seats-{Style.RESET_ALL}\n')
                    
            View_Options(
                        'All Seats',
                        'Available Seats',
                        'Booked Seats',
                        'Select Seat',
                        'Check Seat',
                        'Back'
                    )
            
            try:
                s_choice = int(input('\nChoice : '))
                        
            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue
            
            if s_choice == 1:
                clear__and_sleap()
                Seats.Show_Seat_Map()              
                clear__and_sleap()
            
            elif s_choice == 2:
                clear__and_sleap()
                Seats.Show_Available_Seat()           
                clear__and_sleap()
            
            elif s_choice == 3:
                clear__and_sleap()
                Seats.Show_Booked_Seat()            
                clear__and_sleap() 
            
            elif s_choice == 4:
                clear__and_sleap()
                Seats.Select_Seat()              
                clear__and_sleap()
            
            elif s_choice == 5:
                clear__and_sleap()
                Seats.Check_Seat()            
                clear__and_sleap() 
            
            elif s_choice == 6:
                reset_screen()
                break
            
            else:
                print('❌ Invalid choice.')
                    
            
        
    elif choice == 3:
        
        clear__and_sleap()
        Bookings.New_Booking()           
        clear__and_sleap() 
                       
    elif choice == 4:

        clear_screen()
        sleep()

        while True:

            print(f'{Fore.WHITE}-Manage Bookings-{Style.RESET_ALL}\n')

            View_Options(
                'All Bookings',
                'My Bookings',
                'Booking Details',
                'Cancel',
                'Modify',
                'Back'
            )

            try:
                b_choice = int(input('\nChoice : '))

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue

            if b_choice == 1:

                clear__and_sleap()
                BookingManager.Show_All_Bookings()
                clear__and_sleap()

            elif b_choice == 2:

                clear__and_sleap()
                BookingManager.Show_My_Bookings()
                clear__and_sleap()

            elif b_choice == 3:
                clear__and_sleap()
                BookingManager.Booking_Details()
                clear__and_sleap()
                

            elif b_choice == 4:
                
                clear__and_sleap()
                BookingManager.Cancel_Booking()
                clear__and_sleap()
                                
            elif b_choice == 5:
                clear__and_sleap()
                BookingManager.Modify_Booking()
                clear__and_sleap()

            elif b_choice == 6:
                reset_screen()
                break

            else:
                print('❌ Invalid choice.')
        
        
    elif choice == 5:

        clear_screen()
        sleep()

        while True:

            print(f'{Fore.WHITE}-Search Booking-{Style.RESET_ALL}\n')

            View_Options(
                'Search Movie',
                'Search Booking',
                'Search Booking ID',
                'Search Phone',
                'Back'
            )

            try:
                sb_choice = int(input('\nChoice : '))

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue

            if sb_choice == 1:

                clear__and_sleap()
                Search.search_movie()
                clear__and_sleap()

            elif sb_choice == 2:

                clear__and_sleap()
                Search.search_bookings()
                clear__and_sleap()

            elif sb_choice == 3:

                clear__and_sleap()
                Search.search_by_booking_id()
                clear__and_sleap()

            elif sb_choice == 4:

                clear__and_sleap()
                Search.search_by_phone()
                clear__and_sleap()

            elif sb_choice == 5:

                reset_screen()
                break

            else:
                print('❌ Invalid choice.')
        
    elif choice == 6:

        clear_screen()
        sleep()

        while True:

            print(f'{Fore.WHITE}-Customer-{Style.RESET_ALL}\n')

            View_Options(
                'Add Customer',
                'Show Customers',
                'Update Customer',
                'Delete Customer',
                'Customer Bookings',
                'Back'
            )

            try:
                c_choice = int(input('\nChoice : '))

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue

            if c_choice == 1:

                clear__and_sleap()
                Customer.add_customer()
                clear__and_sleap()

            elif c_choice == 2:

                clear__and_sleap()
                Customer.show_customers()
                clear__and_sleap()

            elif c_choice == 3:

                clear__and_sleap()
                Customer.update_customers()
                clear__and_sleap()

            elif c_choice == 4:

                clear__and_sleap()
                Customer.delete_customer()
                clear__and_sleap()

            elif c_choice == 5:

                clear__and_sleap()
                Customer.Customer_Bookings()
                clear__and_sleap()

            elif c_choice == 6:

                reset_screen()
                break

            else:
                print('❌ Invalid choice.')
    
    elif choice == 7:

        clear_screen()
        sleep()

        while True:

            print(f'{Fore.WHITE}-Statistics-{Style.RESET_ALL}\n')

            View_Options(
                'Movies',
                'Customers',
                'Bookings',
                'Seats',
                'Revenue',
                'Popular Movie',
                'Back'
            )

            try:
                st_choice = int(input('\nChoice : '))

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue

            if st_choice == 1:

                clear__and_sleap()
                Statistics.movies_statistics()
                clear__and_sleap()

            elif st_choice == 2:

                clear__and_sleap()
                Statistics.customers_statistics()
                clear__and_sleap()

            elif st_choice == 3:

                clear__and_sleap()
                Statistics.bookings_statistics()
                clear__and_sleap()

            elif st_choice == 4:

                clear__and_sleap()
                Statistics.seats_statistics()
                clear__and_sleap()

            elif st_choice == 5:

                clear__and_sleap()
                Statistics.revenue_statistics()
                clear__and_sleap()

            elif st_choice == 6:

                clear__and_sleap()
                Statistics.popular_movie()
                clear__and_sleap()

            elif st_choice == 7:

                reset_screen()
                break

            else:
                print('❌ Invalid choice.') 
            
    elif choice == 8:

        clear_screen()
        sleep()

        while True:

            print(f'{Fore.WHITE}-Settings-{Style.RESET_ALL}\n')

            View_Options(
                'Change Currency',
                'Change Screen Delay',
                'Show Current Settings',
                'Reset Settings',
                'Back'
            )

            try:
                settings_choice = int(input('\nChoice : '))

            except ValueError:
                print('\nError: Please enter a number.')
                sleep()
                clear_screen()
                continue

            if settings_choice == 1:

                clear__and_sleap()
                Settings.change_currency()
                clear__and_sleap()

            elif settings_choice == 2:

                clear__and_sleap()
                Settings.change_screen_delay()
                clear__and_sleap()

            elif settings_choice == 3:

                clear__and_sleap()
                Settings.show_settings()
                clear__and_sleap()

            elif settings_choice == 4:

                clear__and_sleap()
                Settings.reset_settings()
                clear__and_sleap()

            elif settings_choice == 5:

                reset_screen()
                break

            else:
                print('❌ Invalid choice.')
        
    elif choice == 9:
        clear__and_sleap()
        Help.help_system()
        clear__and_sleap()
        
    elif choice == 10:
        reset_screen()
        print('Thank you for using our system !')
        print('Goodbye !')
        break
    
    else :
        print('❌ Invalid choice.')