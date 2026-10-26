
# Smart Bus Transport Management System
## Installation and Setup Guide

### 1. Project Requirements

Install the following software:

- Python 3.10 or newer
- MySQL Server
- MySQL Workbench
- Visual Studio Code
- Git (optional)

### 2. Open the Project

Open the Smart-Bus-Transport-Management-System
folder in Visual Studio Code.

### 3. Create a Python Virtual Environment

Open the VS Code terminal and run:

```powershell
python -m venv .venv
```

Activate the virtual environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, you can use
the virtual environment's Python executable
directly in the following steps.

### 4. Install Python Dependencies

Run:

```powershell
.\.venv\Scripts\python.exe -m pip install flask mysql-connector-python
```

### 5. Set Up the MySQL Database

1. Open MySQL Workbench.
2. Connect to your local MySQL server.
3. Open the SQL file:

   database/smart_bus_db.sql

4. Execute the SQL script.

If the export does not create or select
the database automatically, first run:

```sql
CREATE DATABASE IF NOT EXISTS smart_bus_db;
USE smart_bus_db;
```

Then execute the exported SQL statements.

Note: The supplied SQL export may contain
table structures only, without sample records.

### 6. Start the Flask Server

Open the terminal in the main project folder.

Run:

```powershell
.\.venv\Scripts\python.exe backend\app.py
```

Enter your MySQL password when prompted.

Wait until Flask displays:

Running on http://127.0.0.1:5000

### 7. Open the Website

Open a browser and visit:

http://127.0.0.1:5000/dashboard

### 8. Available Features

- Dashboard
- Bus Management
- Route Management
- Schedule Management
- Passenger Management
- Booking Management
- Passenger Registration
- Ticket Booking
- Ticket Cancellation

### 9. Database Tables

The project uses six MySQL tables:

1. buses
2. routes
3. drivers
4. passengers
5. schedules
6. bookings

### 10. Troubleshooting

If Flask does not start:
- Check that Python dependencies are installed.
- Check that the MySQL server is running.
- Verify the MySQL password.
- Check that port 5000 is available.

If the dashboard does not load:
- Make sure Flask is running.
- Check the browser address.
- Review error messages in the VS Code terminal.

If database records are missing:
- Check that smart_bus_db exists.
- Verify that the tables were created.
- Confirm that sample records have been inserted.

### 11. Notes

- This project is intended for local demonstration.
- The database must be configured before running.
- MySQL credentials should not be uploaded to GitHub.
- Cancelled bookings remain stored in the database.
- Cancelled seats are not currently reusable.
- The application does not yet enforce bus seat capacity.
