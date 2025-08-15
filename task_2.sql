
CREATE TABLE IF NOT EXISTS authors (
author_id INT PRIMARY Key,
author_name VARCHAR(215)
);

CREATE TABLE IF NOT EXISTS books (
book_id INT PRIMARY kEY,
title VARCHAR(130),
author_id INT,
price DOUBLE,
publication_date DATE,
FOREIGN Key (author_id) REFERENCES authors (author_id)
);


CREATE TABLE IF NOT EXISTS customers (
customer_id INT PRIMARY KEY,
customer_name VARCHAR(215),
email VARCHAR(215),
address TEXT
);

CREATE TABLE IF NOT EXISTS orders (
order_id INT Primary KEY,
customer_id INT,
order_date DATE,
Foreign Key(customer_id) REFERENCES customers (customer_id)
);

CREATE TABLE IF NOT EXISTS order_details (
orderdetailid INT PRIMARY KEY,
order_id INT,
book_id INT,
quantity DOUBLE,
Foreign Key (order_id) REFERENCES orders (order_id),
Foreign Key (book_id) REFERENCES books (book_id)
);