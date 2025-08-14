import mysql.connector

try:
    # Connect to MySQL server
    connection = mysql.connector.connect(
        host='localhost',        # Change if different
        user='your_mysql_user',  # Replace with your MySQL username
        password='your_password' # Replace with your MySQL password
    )

    if connection.is_connected():
        cursor = connection.cursor()
        # Create database if it doesn't exist
        cursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")
        print("Database 'alx_book_store' created successfully!")

except mysql.connector.Error as e:
    print(f"Error: {e}")

finally:
    # Close cursor and connection if they exist
    if 'cursor' in locals():
        cursor.close()
    if 'connection' in locals() and connection.is_connected():
        connection.close()
