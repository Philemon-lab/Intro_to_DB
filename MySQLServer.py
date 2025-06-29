import mysql.connector
from mysql.connector import errorcode

try:

    connection = mysql.connector.connect(
        host="localhost",       
        user="philemon",          
        password="Mukundwajoy@2006" 
    )

    cursor = connection.cursor()

    cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as err:
    print("Error: Could not connect or create database.")
    print(f"Details: {err}")

finally:
    # Close cursor and connection
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
