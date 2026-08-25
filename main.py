from colorama import Fore, Style, init
init()

import os 
import time 
import Movies
import Seats
import Bookings

# Sleep Function
def sleep():
    time.sleep(1)

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
        'Cancel Ticket',
        'Search Booking',
        'My Bookings',
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
            
        
    elif choice == 3:
        
        clear__and_sleap()
        Bookings.New_Booking()           
        clear__and_sleap() 
                       
    elif choice == 4:
        pass
        
    elif choice == 5:
        pass
        
    elif choice == 6:
        pass 
    
    elif choice == 7:
        pass 
        
    elif choice == 8:
        pass 
        
    elif choice == 9:
        pass 
        
    elif choice == 10:
        pass 
        
    elif choice == 11:
        reset_screen()
        print('Thank you for using our system !')
        print('Goodbye !')
        break
    
    else :
        print('❌ Invalid choice.')