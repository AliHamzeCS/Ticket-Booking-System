🎟️ Ticket Booking System

A Python-based Ticket Booking System built as a learning project to practice modular programming, functions, decorators, JSON file handling, exception handling, and data management.

📌 Version

v0.6.0

🚀 Features

🎬 Movies

Show All Movies

Search Movies

Movie Details

Show Movie Schedule

Filter Movies

Filter by Genre

Filter by Rating

Filter by Price

Filter by Language

💺 Seats

Show All Seats

Show Available Seats

Show Booked Seats

Select Seat

Check Seat

🎟️ Booking

Create New Booking

Select Movie

Select Showtime

Select Seat

Customer Information

Booking Confirmation

Automatic Booking ID generation

Booking data stored in JSON

📋 Manage Bookings

Show All Bookings

Show My Bookings

Booking Details

Cancel Booking

Modify Booking

🔎 Search

Search Movie

Search Bookings

Search by Booking ID

Search by Phone

👤 Customer Management

Add Customer

Show Customers

Update Customer

Delete Customer

Show Customer Bookings

Automatic Customer ID generation

💾 JSON Data Storage

Customer and booking data are stored persistently using JSON files.

customers.json

bookings.json

The application loads the latest booking data when performing relevant searches and customer-booking lookups.

🔗 Customer ↔ Booking Integration

Version 0.6.0 introduces a connection between customers and bookings through Customer ID.

Each booking can now contain:

Booking ID

Customer ID

Movie ID

Movie Name

Showtime

Seat

Customer Name

Phone

Price

Status

This allows the system to retrieve bookings belonging to a specific customer.

🧩 Project Structure

Ticket-Booking-System/
│
├── main.py
├── Movies.py
├── Seats.py
├── Bookings.py
├── BookingManager.py
├── Search.py
├── Customer.py
├── CustomersHistory.py
├── BookingsHistory.py
├── Utils.py
│
├── customers.json
└── bookings.json

🛠️ Technologies & Concepts

Python 3

JSON

Colorama

Functions

Modules

Decorators

Exception Handling

Dictionaries

Lists

Tuples

Sets

Loops

Conditional Statements

zip()

Regular Expressions

▶️ How to Run

Clone the repository, open the project directory, and run:

python3 main.py

Install the required external package if needed:

pip install colorama

🧪 Data

The project uses JSON files to keep customer and booking data between program runs.

For public repositories, use demo data only in JSON files and avoid committing real customer names or phone numbers.

📈 Version History

v0.6.0

Added Customer Management System

Added Customer JSON storage

Added Customer ID

Connected Customers with Bookings

Added Customer Bookings

Added Search System

Added Search by Booking ID

Added Search by Phone

Improved Booking data structure

Improved JSON loading for booking/customer IDs

Added additional input validation

v0.5.0

Previous stable version before Customer and Search integration

👨‍💻 Author

Ali Hamze

📄 License

This project is created for learning and educational purposes.