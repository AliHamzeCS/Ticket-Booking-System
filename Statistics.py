from Movies import Movies
from Utils import decorator_func
from CustomersHistory import Load_Customers
from BookingsHistory import Load_Bookings
import SettingsHistory

settings = SettingsHistory.Load_Settings()

Currency = settings['Currency']


# Movies Statistics
@decorator_func("Movies Statistics")
def movies_statistics():
    total_movies = len(Movies)

    if total_movies == 0:
        print("❌ No movies found")
        return

    highest_rated = 0
    lowest_rated = 10
    rate_movies = 0
    price_movies = 0

    genres = []

    for index in Movies:
        rate_movies += Movies[index]['Rating']
        price_movies += Movies[index]['Price']

        if Movies[index]['Rating'] > highest_rated:
            highest_rated = Movies[index]['Rating']

        if Movies[index]['Rating'] < lowest_rated:
            lowest_rated = Movies[index]['Rating']

        genre = Movies[index]['Genre']

        if '/' in genre:
            genre_list = genre.split(' / ')
            genres.extend(genre_list)

        else:
            genres.append(genre)

    average_rate = rate_movies / total_movies
    average_price = price_movies / total_movies

    genres = set(genres)

    print("\n📊 MOVIES STATISTICS")
    print("=" * 25)
    print(f"\n🎞️ Total Movies : {total_movies}")
    print(f"🎭 Total Genres : {len(genres)}")
    print(f"⭐ Average Rating : {average_rate}")
    print(f"🏆 Highest Rating : {highest_rated}")
    print(f"📉 Lowest Rating : {lowest_rated}")
    print(f"💰 Average Price : {average_price}{Currency}\n")
    print("=" * 25)


# Customers Statistics
@decorator_func("Customers Statistics")
def customers_statistics():
    customers = Load_Customers()
    Bookings = Load_Bookings()

    total_cust = len(customers)

    customers_id = []

    for cust_id in customers:
        for index in Bookings:
            if cust_id == Bookings[index]['Customer ID']:
                customers_id.append(cust_id)

    customers_id = set(customers_id)

    cust_with_bookings = len(customers_id)

    cust_without_bookings = total_cust - cust_with_bookings

    print('=' * 25)
    print('📊 CUSTOMERS STATISTICS\n')
    print(f"👤 Total Customers            : {total_cust}")
    print(f"🎟️ Customers With Bookings    : {cust_with_bookings}")
    print(f"🚫 Customers Without Bookings : {cust_without_bookings}\n")
    print('=' * 25)


# Bookings Statistics
@decorator_func("Bookings Statistics")
def bookings_statistics():
    Bookings = Load_Bookings()

    total_bookings = len(Bookings)
    confirmid_bookings = 0
    cancelled_bookings = 0

    for index in Bookings:
        if Bookings[index]['Status'] == 'Confirmed':
            confirmid_bookings += 1

        elif Bookings[index]['Status'] == 'Cancelled':
            cancelled_bookings += 1

        else:
            pass

    print('📊 BOOKINGS STATISTICS')
    print('=' * 25)
    print(f"\n🎟️ Total Bookings    : {total_bookings}")
    print(f"✅ Confirmed Bookings : {confirmid_bookings}")
    print(f"❌ Cancelled Bookings : {cancelled_bookings}\n")
    print('=' * 25)


# Seats Statistics
@decorator_func("Seats Statistics")
def seats_statistics():
    total_seats = 0
    available_seats = 0
    booked_seats = 0

    for movie in Movies:
        for showtime in Movies[movie]['Showtimes']:
            for seat in Movies[movie]['Showtimes'][showtime]:

                total_seats += 1

                if Movies[movie]['Showtimes'][showtime][seat] == 'Available':
                    available_seats += 1

                elif Movies[movie]['Showtimes'][showtime][seat] == 'Booked':
                    booked_seats += 1

    print('=' * 25)
    print('📊 SEATS STATISTICS')
    print('=' * 25)

    print(f'\n💺 Total Seats     : {total_seats}')
    print(f'🟢 Available Seats : {available_seats}')
    print(f'🔴 Booked Seats    : {booked_seats}\n')

    print('=' * 25)


# Revenue Statistics
@decorator_func("Revenue Statistics")
def revenue_statistics():

    Bookings = Load_Bookings()

    total_revenue = 0
    confirmed_tickets = 0

    for ID in Bookings:

        if Bookings[ID]['Status'] == 'Confirmed':

            total_revenue += Bookings[ID]['Price']
            confirmed_tickets += 1

    if confirmed_tickets > 0:
        average_price = total_revenue / confirmed_tickets

    else:
        average_price = 0

    print('=' * 25)
    print('💰 REVENUE STATISTICS')
    print('=' * 25)

    print(f'\n💰 Total Revenue     : {Currency}{total_revenue}')
    print(f'🎟️ Confirmed Tickets : {confirmed_tickets}')
    print(f'💵 Average Price     : {Currency}{average_price:.2f}\n')

    print('=' * 25)


# Popular Movie Statistics
@decorator_func("Popular Movie Statistics")
def popular_movie():
    Bookings = Load_Bookings()

    if not Bookings:
        print("❌ No bookings found.")
        return

    movies_bookings = {}

    for ID in Bookings:

        if Bookings[ID]['Status'] == 'Confirmed':

            movie_name = Bookings[ID]['Movie Name']

            if movie_name in movies_bookings:
                movies_bookings[movie_name] += 1

            else:
                movies_bookings[movie_name] = 1

    if not movies_bookings:
        print("❌ No confirmed bookings found.")
        return

    popular = max(movies_bookings, key=movies_bookings.get)

    print('=' * 25)
    print('🏆 POPULAR MOVIE')
    print('=' * 25)

    print(f'\n🏆 Most Popular Movie : {popular}')
    print(f'🎟️  Total Bookings     : {movies_bookings[popular]}\n')

    print('=' * 25)