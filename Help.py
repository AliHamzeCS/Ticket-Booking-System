from Utils import decorator_func


@decorator_func('Help')
def help_system():

    print('=' * 40)
    print('🆘 HELP')
    print('=' * 40)

    print('\n🎬 Movies')
    print('View, search, filter movies and show schedules.')

    print('\n💺 Seats')
    print('View available/booked seats and check or select a seat.')

    print('\n🎟️ Booking')
    print('Create a new booking by selecting a movie,')
    print('showtime, seat and customer.')

    print('\n📋 Manage Bookings')
    print('View, search, cancel and modify bookings.')

    print('\n🔎 Search')
    print('Search for movies or bookings.')

    print('\n👤 Customer')
    print('Add, view, update, delete customers')
    print('and view customer bookings.')

    print('\n📊 Statistics')
    print('View movies, customers, bookings, seats,')
    print('revenue and popular movie statistics.')

    print('\n⚙️ Settings')
    print('Change currency, screen delay and reset settings.')

    print('\n❌ Exit')
    print('Close the application.')

    print('\n' + '=' * 40)