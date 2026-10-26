
# Smart Bus Transport Management System

## Project Overview

The Smart Bus Transport Management System is a
web-based Database Management System (DBMS) project
developed to manage bus transportation information.

The system helps organize buses, routes, drivers,
schedules, passengers, and ticket bookings using
a centralized MySQL database.

## Objectives

- Manage bus transportation records.
- Display bus routes and schedules.
- Maintain passenger information.
- Allow new passenger registration.
- Enable bus ticket booking.
- Prevent duplicate seat bookings.
- Allow ticket cancellation.
- Maintain booking history in the database.

## Technologies Used

### Frontend
- HTML
- CSS
- JavaScript

### Backend
- Python
- Flask

### Database
- MySQL

### Development Tools
- Visual Studio Code
- MySQL Workbench
- Git and GitHub

## Database Tables

The project uses six main tables:

1. buses
2. routes
3. drivers
4. passengers
5. schedules
6. bookings

### Database Relationships

- A schedule is associated with a bus.
- A schedule is associated with a route.
- A schedule is associated with a driver.
- A booking is associated with a passenger.
- A booking is associated with a schedule.

These relationships are implemented using
primary keys and foreign keys.

## Main Features

### Dashboard
Displays an overview of transportation records.

### Bus Management
Retrieves and displays bus information.

### Route Management
Retrieves and displays available routes.

### Schedule Management
Displays bus schedules and their related details.

### Passenger Management
Displays passenger records stored in MySQL.

### Passenger Registration
Allows new passengers to register.

### Ticket Booking
Allows passengers to book tickets using a
Passenger ID, Schedule ID, and Seat Number.

The system prevents duplicate seat bookings
for the same schedule.

### Ticket Cancellation
Allows users to cancel an existing ticket
using its Booking ID.

Cancelled bookings remain stored in the database
with their status changed to "Cancelled".

## Project Structure

Smart-Bus-Transport-Management-System/
|
|-- backend/
|   |-- app.py
|   |-- database.py
|
|-- database/
|
|-- frontend/
|   |-- index.html
|   |-- style.css
|   |-- script.js
|
|-- README.md
|-- SETUP.md
|-- .gitignore

## How to Run

1. Install Python and MySQL.
2. Open the project in Visual Studio Code.
3. Create and activate a Python virtual environment.
4. Install the required Python dependencies.
5. Set up the MySQL database using the project's
   database scripts or setup instructions.
6. Start the Flask application:

   python backend/app.py

7. Enter the MySQL password when prompted.
8. Open the website at:

   http://127.0.0.1:5000/dashboard

For additional setup details, see SETUP.md.

## Testing

The following features have been tested:

- Flask server and dashboard
- Bus Management
- Route Management
- Schedule Management
- Passenger Management
- Booking Management
- Passenger Registration
- Ticket Booking
- Duplicate-seat prevention
- Ticket Cancellation
- Double-cancellation prevention

## Current Limitations

- The system is designed for local demonstration.
- Cancelled seats are not currently reusable
  for another booking on the same schedule.
- Seat numbers are not yet checked against
  the assigned bus's seating capacity.
- The booking date is automatically recorded
  by MySQL.

## Future Enhancements

- User login and authentication
- Online payment integration
- Automatic seat availability management
- Booking history search
- Administrative controls
- Real-time bus tracking

## Conclusion

The Smart Bus Transport Management System
demonstrates the practical use of DBMS concepts,
including relational tables, primary keys,
foreign keys, SQL queries, data insertion,
data retrieval, record updates, and constraints.

It integrates Flask, MySQL, HTML, CSS, and
JavaScript into a functional web application.
