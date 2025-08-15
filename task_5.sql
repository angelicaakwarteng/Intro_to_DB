USE alx_book_store;

CREATE TABLE customer(
customer_id INT PRIMARY KEY, 
customer_name VARCHAR(255), 
email VARCHAR(255), 
address VARCHAR(255)
);

INSERT INTO customer VALUES (1, 'Cole Baidoo', 'cbaidoo@sandtech.com', '123 Happiness Ave.');