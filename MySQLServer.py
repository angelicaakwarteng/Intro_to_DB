import pymysql
from lavender import password

#establishing connection with my alx_book_store db
mydb = pymysql.connect(
    host='localhost',
    user='root',
    passwd=password,
    database='alx_book_store'
)
#save connection object
mydb_cursor = mydb.cursor()
try:
    print("Database 'alx_book_store' created successfully!")
except:
    print("Failing to connect to the DB.")


#handling close of the DB in the script.
mydb_cursor.close()
mydb.close()
