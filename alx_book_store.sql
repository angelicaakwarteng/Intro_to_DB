CREATE DATABASE IF NOT EXISTS alx_book_store;
USE alx_book_store;


CREATE TABLE IF NOT EXISTS Authors (
author_id INT PRIMARY Key,
author_name VARCHAR(215)
);

CREATE TABLE IF NOT EXISTS Books (
book_id INT PRIMARY kEY,
title VARCHAR(130),
author_id INT,
price DOUBLE,
publication_date DATE,
FOREIGN Key (author_id) REFERENCES Authors (author_id)
);


CREATE TABLE IF NOT EXISTS Customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(215),
email VARCHAR(215),
address TEXT
);

CREATE TABLE IF NOT EXISTS Orders (
order_id INT Primary KEY,
customer_id INT,
order_date DATE,
Foreign Key(customer_id) REFERENCES Customers (customer_id)
);

CREATE TABLE IF NOT EXISTS Order_Details (
orderdetailid INT PRIMARY KEY,
order_id INT,
book_id INT,
quantity DOUBLE,
Foreign Key (order_id) REFERENCES Orders (order_id),
Foreign Key (book_id) REFERENCES Books (book_id)
);

-- DROP DATABASE alx_book_store;

-- creating new use alx_user and passing admin rights to user to access this database.
CREATE USER 'alx_user'@'localhost'
IDENTIFIED WITH mysql_native_password BY 'mypassword';

GRANT ALL PRIVILEGES ON alx_book_store.* TO 'alx_user'@'localhost';
FLUSH PRIVILEGES;