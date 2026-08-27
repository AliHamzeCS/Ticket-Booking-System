import json
import os


BOOKINGS_FILE = 'bookings.json'


# Load Bookings
def Load_Bookings():

    if not os.path.exists(BOOKINGS_FILE):
        return {}

    try:
        with open(BOOKINGS_FILE, 'r') as file:
            Bookings = json.load(file)

            New_Bookings = {}

            for key, value in Bookings.items():
                New_Bookings[int(key)] = value

            return New_Bookings

    except json.JSONDecodeError:
        return {}


# Dump Bookings
def Dump_Bookings(bookings):

    with open(BOOKINGS_FILE, 'w') as file:
        json.dump(bookings, file, indent=4)


# Add Booking
def Add_Booking(bookings, booking_id, booking_data):
    
    bookings[booking_id] = booking_data
    Dump_Bookings(bookings)