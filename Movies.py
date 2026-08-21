from Utils import decorator_func

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
        'Showtimes': ['14:00', '17:00', '20:00']
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
        'Showtimes': ['13:00', '16:00', '21:00']
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
        'Showtimes': ['14:00', '18:00', '21:00']
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
        'Showtimes': ['13:30', '16:00', '20:00']
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
        'Showtimes': ['13:30', '17:30', '22:00']
    }
}

@decorator_func('Show All Movies')
# Show All Movies
def Show_All_Movies():
    Shapes = ['🆔', '🎞️', '🎭', '⏱️', '⭐', '💰', '🌐', '🔞']

    for index in Movies:
        print(f'\n🎬 Movie #{index}')
        print('-' * 30)

        for shape, key in zip(Shapes, Movies[index]):
            if key == 'Showtimes':
                continue

            print(f'{shape} {key} : {Movies[index][key]}')

        print('-' * 30)


@decorator_func('Search Movies')
# Search Movies
def Search_Movies():
    movie_name = input('Enter movie name : ').title()

    found = False

    for index_movie in Movies:
        if movie_name in Movies[index_movie]['Name']:

            if not found:
                print('\n✅ Movie Found!\n')
                found = True

            Shapes = ['🆔', '🎞️', '🎭', '⏱️', '⭐', '💰', '🌐', '🔞']

            for shape, key in zip(Shapes, Movies[index_movie]):
                if key == 'Showtimes':
                    continue

                print(f'{shape} {key} : {Movies[index_movie][key]}')

            print()

    if not found:
        print('❌ No movie found matching your search.')

@decorator_func('Movie Details')
# Movie Details
def Movie_Details():
    try:
        movie_ID = int(input('Enter Movie ID : '))

    except ValueError:
        print('Enter ID Please.')
        return

    found = False

    for index_movie in Movies:
        if movie_ID == Movies[index_movie]['ID']:

            if not found:
                found = True
                print(f"\n🎬 {Movies[index_movie]['Name']}\n")

            Shapes = ['🆔', '🎞️', '🎭', '⏱️', '⭐', '💰', '🌐', '🔞']

            for shape, key in zip(Shapes, Movies[index_movie]):
                if key == 'Showtimes':
                    continue

                print(f'{shape} {key} : {Movies[index_movie][key]}')

            print()

    if not found:
        print('❌ Movie ID not found.')

@decorator_func('Show Movie Schedule')
# Show Movie Schedule
def Show_Movie_Schedule():
    try:
        movie_ID = int(input('Enter Movie ID : '))

    except ValueError:
        print('Please enter ID only.')
        return

    found = False

    for index_movie in Movies:
        if movie_ID == index_movie:
            found = True

            print(f'\n🎬 {Movies[index_movie]["Name"]}')
            print('⏰ Showtimes:\n')

            index = 1

            for time in Movies[index_movie]['Showtimes']:
                print(f'{index} ▶ {time}')
                index += 1

    if not found:
        print('❌ Movie ID not found.')
        
@decorator_func('Filter By Genre')       
# Fliter By Genre
def Filter_By_Genre():
    genres = []

    for index_movie in Movies:
        for element in Movies[index_movie]:
            if element == 'Genre':
                genres.append(Movies[index_movie][element]) 

    genres = set(genres) 
    print('🎭 Genres :' , end='\n\n')
    for genre in genres:
        print(f'  {genre}')
        
    print()

    genre_movie = input('Enter Genre : ').title()
    print()

    found = False

    for index_movie in Movies:
        if genre_movie in Movies[index_movie]['Genre']:
            if not found:
                found = True
                print('✅ Movies Found:')
            print(f" - {Movies[index_movie]['Name']}") 
        	
    if not found:
        print('❌ No movies found in this genre.')
        
@decorator_func('Filter By Rating')
def Filter_By_Rating():
    try:
        rate_of_movie = float(input('Enter a minimum rate : '))

    except ValueError:
        print('❌ Please enter a valid rate.')
        return

    print()
    found = False

    for index in Movies:
        if Movies[index]['Rating'] >= rate_of_movie:
            if not found:
                found = True
                print('✅ Movies Found:') # طبعتها مرة وحدة بس
            print(f"- {Movies[index]['Name']} {Movies[index]['Rating']}/10")

    if not found:
        print('No movies found with this rating')
   
@decorator_func('Filter By Price')   
# Filter By Price     
def Filter_By_Price():
	
	
	
	try :
		price_of_movie = float(input('Enter a maximum price : '))
		
	except ValueError :
		print('❌ Please enter a valid price.')
		return
	
	found = False 
	for index in Movies :
		if Movies[index]['Price'] <= price_of_movie :
			if not found :
				found = True
			print(f"- {Movies[index]['Name']}	{Movies[index]['Price']}$") 
	if not found :
			print('❌ No movies found under or equal to this price.')
   
@decorator_func('Filter By Language')   
# Filter By Language     
def Filter_By_Language():
	
	language_of_movie = input('Enter a Language : ').title()
		
	
	found = False 
	for index in Movies :
		if Movies[index]['Language'] == language_of_movie :
			if not found :
				found = True
			print(f"- {Movies[index]['Name']}	{Movies[index]['Language']}") 
	if not found :
			print('❌ No movies found.')