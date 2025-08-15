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

except mysql.connector.Error as err:
    print(f"Failed to connect: {err}")

finally:
    if 'mydb_cursor' in locals() and mydb_cursor:
        mydb_cursor.close()
    if 'my_db' in locals() and my_db.is_connected():
        my_db.close()