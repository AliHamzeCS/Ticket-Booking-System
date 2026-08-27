# 🎟️ Ticket Booking System

A console-based Ticket Booking System built with Python.

This project allows users to browse movies, check seat availability, make bookings, manage bookings, and store booking data using JSON.

---

## 📌 Version

**Current Version: v0.5.0**

---

## ✨ Features

### 🎬 Movies
- Show all movies
- Search movies
- Show movie details
- Show movie schedules
- Filter movies by:
  - Genre
  - Rating
  - Price
  - Language

### 💺 Seats
- Show complete seat map
- Show available seats
- Show booked seats
- Select a seat
- Check seat status

### 🎟️ Book Ticket
- Create a new booking
- Select movie
- Select showtime
- Select seat
- Enter customer information
- Generate unique Booking ID
- Confirm booking
- Automatically mark the selected seat as booked

### 📋 Manage Bookings
- Show all bookings
- Show customer's bookings
- Show booking details
- Cancel booking
- Modify booking
  - Change showtime
  - Change seat
  - Change customer name
  - Change phone number

### 💾 Data Persistence
Booking information is stored in a JSON file.

The system includes:

- `Load_Bookings()`
- `Dump_Bookings()`
- `Add_Booking()`

This allows booking data to remain available after closing and reopening the program.

### 🎨 User Interface
- Colored terminal output using Colorama
- Menu-based navigation
- Screen clearing
- Simple and organized console interface

---

## 🗂️ Project Structure

```text
Ticket-Booking-System/
│
├── main.py
├── Movies.py
├── Seats.py
├── Bookings.py
├── BookingsHistory.py
├── BookingManager.py
├── Utils.py
├── bookings.json
└── README.md