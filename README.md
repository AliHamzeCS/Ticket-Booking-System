# 🎟️ Ticket Booking System

A Python-based Ticket Booking System built as a learning project to practice modular programming, functions, decorators, JSON file handling, exception handling, data management, and statistics.

## 📌 Version

v0.7.0

## 🚀 Features

### 🎬 Movies

- Show All Movies
- Search Movies
- Movie Details
- Show Movie Schedule
- Filter Movies
- Filter by Genre
- Filter by Rating
- Filter by Price
- Filter by Language

### 💺 Seats

- Show All Seats
- Show Available Seats
- Show Booked Seats
- Select Seat
- Check Seat

### 🎟️ Booking

- Create New Booking
- Select Movie
- Select Showtime
- Select Seat
- Customer Information
- Booking Confirmation
- Automatic Booking ID generation
- Booking data stored in JSON
- Customer ID integration

### 📋 Manage Bookings

- Show All Bookings
- Show My Bookings
- Booking Details
- Cancel Booking
- Modify Booking

### 🔎 Search

- Search Movie
- Search Bookings
- Search by Booking ID
- Search by Phone

### 👤 Customer Management

- Add Customer
- Show Customers
- Update Customer
- Delete Customer
- Show Customer Bookings
- Automatic Customer ID generation
- Customer data stored in JSON

### 📊 Statistics

- Movies Statistics
- Customers Statistics
- Bookings Statistics
- Seats Statistics
- Revenue Statistics
- Popular Movie Statistics

#### 🎬 Movies Statistics

- Total Movies
- Total Genres
- Average Rating
- Highest Rating
- Lowest Rating
- Average Price

#### 👤 Customers Statistics

- Total Customers
- Customers With Bookings
- Customers Without Bookings

#### 🎟️ Bookings Statistics

- Total Bookings
- Confirmed Bookings
- Cancelled Bookings

#### 💺 Seats Statistics

- Total Seats
- Available Seats
- Booked Seats

#### 💰 Revenue Statistics

- Total Revenue
- Confirmed Tickets
- Average Ticket Price

#### 🏆 Popular Movie Statistics

- Most Popular Movie
- Total Confirmed Bookings for the Movie

## 💾 JSON Data Storage

Customer and booking data are stored persistently using JSON files.

- `customers.json`
- `bookings.json`

The application loads the latest customer and booking data when performing relevant operations and statistics.

## 🔗 Customer ↔ Booking Integration

Version 0.6.0 introduced a connection between customers and bookings through Customer ID.

Each booking can contain:

- Booking ID
- Customer ID
- Movie ID
- Movie Name
- Showtime
- Seat
- Customer Name
- Phone
- Price
- Status

This allows the system to retrieve bookings belonging to a specific customer and generate customer-related statistics.

## 📊 Statistics Integration

Version 0.7.0 introduces a complete Statistics system.

The Statistics menu is integrated into `main.py` and provides information about:

- Movies
- Customers
- Bookings
- Seats
- Revenue
- Popular Movies

Statistics are calculated dynamically from the current movie, customer, and booking data.

## 🧩 Project Structure

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

├── Statistics.py

├── Utils.py

│

├── customers.json

└── bookings.json

## 🛠️ Technologies & Concepts

- Python 3
- JSON
- Colorama
- Functions
- Modules
- Decorators
- Exception Handling
- Dictionaries
- Lists
- Tuples
- Sets
- Loops
- Conditional Statements
- zip()
- Regular Expressions
- File Handling
- Data Persistence
- Basic Data Analysis

## ▶️ How to Run

Clone the repository, open the project directory, and run:

python3 main.py

Install the required external package if needed:

pip install colorama

## 🧪 Data

The project uses JSON files to keep customer and booking data between program runs.

For public repositories, use demo data only in JSON files and avoid committing real customer names or phone numbers.

## 📈 Version History

### v0.7.0

- Added Statistics System
- Added Movies Statistics
- Added Customers Statistics
- Added Bookings Statistics
- Added Seats Statistics
- Added Revenue Statistics
- Added Popular Movie Statistics
- Added Statistics submenu to `main.py`
- Added Total Movies calculation
- Added Average Movie Rating
- Added Highest Movie Rating
- Added Lowest Movie Rating
- Added Average Movie Price
- Added Total Genres calculation
- Added Customers With Bookings calculation
- Added Customers Without Bookings calculation
- Added Confirmed Bookings calculation
- Added Cancelled Bookings calculation
- Added Available Seats calculation
- Added Booked Seats calculation
- Added Total Revenue calculation
- Added Average Ticket Price calculation
- Added Most Popular Movie calculation
- Improved compatibility with bookings that may not contain Customer ID

### v0.6.0

- Added Customer Management System
- Added Customer JSON storage
- Added Customer ID
- Connected Customers with Bookings
- Added Customer Bookings
- Added Search System
- Added Search by Booking ID
- Added Search by Phone
- Improved Booking data structure
- Improved JSON loading for booking/customer IDs
- Added additional input validation

### v0.5.0

Previous stable version before Customer and Search integration.

## 👨‍💻 Author

Ali Hamze

## 📄 License

This project is created for learning and educational purposes.