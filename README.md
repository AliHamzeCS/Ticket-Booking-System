# 🎟️ Ticket Booking System

A Python-based Ticket Booking System built as a learning project to practice modular programming, functions, decorators, JSON file handling, exception handling, data management, and basic statistics.

## 📌 Version

v0.*8.0

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

### ⚙️ Settings

- Change Currency
- Change Screen Delay
- Show Current Settings
- Reset Settings
- Settings stored using JSON
- Currency is used dynamically when displaying prices
- Screen Delay is used dynamically by the application

## 💾 JSON Data Storage

The project uses JSON files to store data persistently between program runs.

### JSON Files

- `customers.json`
- `bookings.json`
- `settings.json`

The application loads the latest customer, booking, and settings data when performing relevant operations.

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

## ⚙️ Settings Integration

The Settings system allows the user to customize application behavior.

### Currency

The currency can be changed from the Settings menu and is used when displaying prices and revenue.

### Screen Delay

The screen delay can be changed from the Settings menu and is used by the application when clearing and refreshing screens.

Settings are stored persistently in:

`settings.json`

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

├── Settings.py

├── SettingsHistory.py

├── Utils.py

│

├── customers.json

├── bookings.json

└── settings.json

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
- `zip()`
- Regular Expressions
- File Handling
- Data Persistence
- Basic Data Analysis

## ▶️ How to Run

Clone the repository, open the project directory, and run:

```bash
python3 main.py

## 👨‍💻 Author

Ali Hamze

## 📄 License

This project is created for learning and educational purposes.