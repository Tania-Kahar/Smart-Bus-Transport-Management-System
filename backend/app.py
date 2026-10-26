
from flask import Flask, jsonify,request, send_from_directory
import mysql.connector
from getpass import getpass

app = Flask(__name__)

from pathlib import Path

FRONTEND_DIR = Path(__file__).resolve().parent.parent / "frontend"


@app.route("/dashboard")
def dashboard():
    return send_from_directory(FRONTEND_DIR, "index.html")


@app.route("/style.css")
def stylesheet():
    return send_from_directory(FRONTEND_DIR, "style.css")


@app.route("/script.js")
def javascript():
    return send_from_directory(FRONTEND_DIR, "script.js")


db_password = getpass("Enter MySQL password: ")


@app.route("/")
def home():
    return jsonify({
        "message": "Welcome to Smart Bus Transport Management System",
        "status": "Backend is running"
    })


@app.route("/buses")
def get_buses():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor(dictionary=True)
        cursor.execute("SELECT * FROM buses")
        buses = cursor.fetchall()

        return jsonify(buses)

    except mysql.connector.Error:
        app.logger.exception("Database query failed")
        return jsonify({"error": "Unable to retrieve buses"}), 500

    finally:
        if cursor is not None:
            cursor.close()
        if connection is not None and connection.is_connected():
            connection.close()

@app.route("/routes")
def get_routes():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                route_id,
                source,
                destination,
                distance_km,
                estimated_duration
            FROM routes
            ORDER BY route_id
        """)

        routes = cursor.fetchall()

        return jsonify(routes)

    except mysql.connector.Error:
        app.logger.exception("Failed to retrieve routes")
        return jsonify({
            "error": "Unable to retrieve routes"
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

@app.route("/schedules")
def get_schedules():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                s.schedule_id,
                b.bus_number,
                b.bus_type,
                r.source,
                r.destination,
                d.driver_name,
                s.departure_time,
                s.arrival_time,
                s.fare
            FROM schedules s
            JOIN buses b
                ON s.bus_id = b.bus_id
            JOIN routes r
                ON s.route_id = r.route_id
            JOIN drivers d
                ON s.driver_id = d.driver_id
            ORDER BY s.departure_time
        """)

        schedules = cursor.fetchall()

        for schedule in schedules:
            schedule["departure_time"] = (
                schedule["departure_time"].isoformat(
                    sep=" "
                )
            )
            schedule["arrival_time"] = (
                schedule["arrival_time"].isoformat(
                    sep=" "
                )
            )
            schedule["fare"] = float(schedule["fare"])

        return jsonify(schedules)

    except mysql.connector.Error:
        app.logger.exception("Failed to retrieve schedules")
        return jsonify({
            "error": "Unable to retrieve schedules"
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

@app.route("/passengers")
def get_passengers():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor(dictionary=True)

        cursor.execute("""
            SELECT
                passenger_id,
                passenger_name,
                email,
                phone,
                gender,
                age
            FROM passengers
            ORDER BY passenger_id
        """)

        passengers = cursor.fetchall()

        return jsonify(passengers)

    except mysql.connector.Error:
        app.logger.exception("Failed to retrieve passengers")
        return jsonify({
            "error": "Unable to retrieve passengers"
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()


# BOOKING MANAGEMENT API

@app.route("/bookings")
def get_bookings():
    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor(dictionary=True)

        query = """
            SELECT
                b.booking_id,
                p.passenger_name,
                bu.bus_number,
                r.source,
                r.destination,
                b.seat_number,
                b.booking_date,
                b.booking_status,
                s.fare
            FROM bookings b
            JOIN passengers p
                ON b.passenger_id = p.passenger_id
            JOIN schedules s
                ON b.schedule_id = s.schedule_id
            JOIN buses bu
                ON s.bus_id = bu.bus_id
            JOIN routes r
                ON s.route_id = r.route_id
            ORDER BY b.booking_id
        """

        cursor.execute(query)
        bookings = cursor.fetchall()

        for booking in bookings:
            if booking["booking_date"] is not None:
                booking["booking_date"] = str(
                    booking["booking_date"]
                )

        return jsonify(bookings)

    except mysql.connector.Error:
        app.logger.exception("Failed to retrieve bookings")
        return jsonify({
            "error": "Unable to retrieve bookings"
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

# NEW PASSENGER REGISTRATION API

@app.route("/register-passenger", methods=["POST"])
def register_passenger():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Please send valid JSON data."
        }), 400

    name = str(data.get("passenger_name") or "").strip()
    email = str(data.get("email") or "").strip()
    phone = str(data.get("phone") or "").strip()
    gender = str(data.get("gender") or "").strip()

    try:
        age = int(data.get("age"))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Age must be a valid number."
        }), 400

    if not all([name, email, phone, gender]):
        return jsonify({
            "error": "All fields are required."
        }), 400

    if age < 1 or age > 120:
        return jsonify({
            "error": "Age must be between 1 and 120."
        }), 400

    if gender not in ("Male", "Female", "Other"):
        return jsonify({
            "error": "Please select a valid gender."
        }), 400

    if not phone.isdigit() or len(phone) != 10:
        return jsonify({
            "error": "Phone must contain exactly 10 digits."
        }), 400

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor()

        query = """
            INSERT INTO passengers
                (passenger_name, email, phone, gender, age)
            VALUES (%s, %s, %s, %s, %s)
        """

        values = (name, email, phone, gender, age)

        cursor.execute(query, values)
        connection.commit()

        return jsonify({
            "message": "Passenger registered successfully!",
            "passenger_id": cursor.lastrowid
        }), 201

    except mysql.connector.Error:
        if connection is not None and connection.is_connected():
            connection.rollback()

        app.logger.exception("Passenger registration failed")

        return jsonify({
            "error": "Unable to register passenger."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

# TICKET BOOKING API

@app.route("/book-ticket", methods=["POST"])
def book_ticket():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid booking information."
        }), 400

    try:
        passenger_id = int(data.get("passenger_id"))
        schedule_id = int(data.get("schedule_id"))
        seat_number = int(data.get("seat_number"))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Enter valid passenger, schedule and seat numbers."
        }), 400

    if min(passenger_id, schedule_id, seat_number) < 1:
        return jsonify({
            "error": "All ID and seat numbers must be positive."
        }), 400

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor()

        # Check passenger exists
        cursor.execute(
            "SELECT passenger_id FROM passengers WHERE passenger_id = %s",
            (passenger_id,)
        )

        if cursor.fetchone() is None:
            return jsonify({
                "error": "Passenger ID not found."
            }), 404

        # Check schedule exists
        cursor.execute(
            "SELECT schedule_id FROM schedules WHERE schedule_id = %s",
            (schedule_id,)
        )

        if cursor.fetchone() is None:
            return jsonify({
                "error": "Schedule ID not found."
            }), 404

        # Check whether seat is already booked
        cursor.execute("""
            SELECT booking_id
            FROM bookings
            WHERE schedule_id = %s
              AND seat_number = %s
        """, (schedule_id, seat_number))

        if cursor.fetchone() is not None:
            return jsonify({
                "error": "This seat is already booked."
            }), 409

        # Create booking
        cursor.execute("""
            INSERT INTO bookings
                (passenger_id, schedule_id, seat_number)
            VALUES (%s, %s, %s)
        """, (passenger_id, schedule_id, seat_number))

        connection.commit()

        return jsonify({
            "message": "Ticket booked successfully!",
            "booking_id": cursor.lastrowid
        }), 201

    except mysql.connector.IntegrityError:
        if connection is not None:
            connection.rollback()

        return jsonify({
            "error": "Booking conflict or invalid reference."
        }), 409

    except mysql.connector.Error:
        if connection is not None:
            connection.rollback()

        app.logger.exception("Ticket booking failed")

        return jsonify({
            "error": "Unable to book ticket."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

# BOOKING CANCELLATION API

@app.route("/cancel-ticket", methods=["POST"])
def cancel_ticket():
    data = request.get_json(silent=True)

    if not isinstance(data, dict):
        return jsonify({
            "error": "Invalid cancellation request."
        }), 400

    try:
        booking_id = int(data.get("booking_id"))
    except (TypeError, ValueError):
        return jsonify({
            "error": "Enter a valid Booking ID."
        }), 400

    if booking_id < 1:
        return jsonify({
            "error": "Booking ID must be positive."
        }), 400

    connection = None
    cursor = None

    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=db_password,
            database="smart_bus_db"
        )

        cursor = connection.cursor()

        # Find and lock the booking record
        cursor.execute("""
            SELECT booking_status
            FROM bookings
            WHERE booking_id = %s
            FOR UPDATE
        """, (booking_id,))

        booking = cursor.fetchone()

        if booking is None:
            return jsonify({
                "error": "Booking ID not found."
            }), 404

        if booking[0] == "Cancelled":
            return jsonify({
                "error": "This ticket is already cancelled."
            }), 409

        # Update booking status
        cursor.execute("""
            UPDATE bookings
            SET booking_status = 'Cancelled'
            WHERE booking_id = %s
        """, (booking_id,))

        connection.commit()

        return jsonify({
            "message": "Ticket cancelled successfully!",
            "booking_id": booking_id
        }), 200

    except mysql.connector.Error:
        if connection is not None and connection.is_connected():
            connection.rollback()

        app.logger.exception("Ticket cancellation failed")

        return jsonify({
            "error": "Unable to cancel ticket."
        }), 500

    finally:
        if cursor is not None:
            cursor.close()

        if connection is not None and connection.is_connected():
            connection.close()

if __name__ == "__main__":
    print("\nREGISTERED FLASK ROUTES:")
    print(app.url_map)
    app.run(debug=False, port=5000)


