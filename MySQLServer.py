import pymysql
from lavender import password

# # establishing connection with my alx_book_store db
# try:
#     mydb = pymysql.connect(
#         host='localhost',
#         user='root',
#         passwd=password,
#         database='alx_book_store'
#     )
#     #save connection object
#     mydb_cursor = mydb.cursor()
#     print("Database 'alx_book_store' created successfully!")

# except mysql.connector.Error:
#     print("Failing to connect to the DB.")

# #handling close of the DB in the script.
# finally:
#     mydb_cursor.close()
#     mydb.close()




#using mysql-connector
import mysql.connector

try:
    my_db = mysql.connector.connect(
    host="localhost",
    user="alx_user",
    password="mypassword",
    database="alx_book_store"
    )

    # save connection object
    mydb_cursor = my_db.cursor()
    print("Connected to database 'alx_book_store' successfully!")

    #creating a new database if it does not exist.
    creation = 'CREATE DATABASE IF NOT EXISTS alx_book_store'
    mydb_cursor.execute(creation)
    my_db.commit()

    #creating tables if they don't exist
    author_table = 'CREATE TABLE IF NOT EXISTS Authors (author_id INT PRIMARY Key, author_name VARCHAR(215)'
    mydb_cursor.execute(author_table)
    my_db.commit()

    book_table = 'CREATE TABLE IF NOT EXISTS Books (book_id INT PRIMARY kEY, title VARCHAR(130), author_id INT,price DOUBLE,publication_date DATE,FOREIGN Key (author_id) REFERENCES Authors (author_id)'
    mydb_cursor.execute(book_table)
    my_db.commit()

    customer_table = 'CREATE TABLE IF NOT EXISTS Customers (customer_id INT PRIMARY KEY, customer_name VARCHAR(215),email VARCHAR(215),address TEXT)'
    mydb_cursor.execute(customer_table)
    my_db.commit()

except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")

finally:
    if 'mydb_cursor' in locals() and mydb_cursor:
        mydb_cursor.close()
    if 'my_db' in locals() and my_db.is_connected():
        my_db.close()


