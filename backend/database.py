
import mysql.connector
from getpass import getpass

password = getpass("Enter your MySQL password: ")

try:
    connection = mysql.connector.connect(
        host="localhost",
        user="root",
        password=password,
        database="smart_bus_db"
    )

    if connection.is_connected():
        print("Successfully connected to MySQL!")
        print("Smart Bus Database is ready!")

    connection.close()

except mysql.connector.Error as error:
    print("Database connection failed:", error)
