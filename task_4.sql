USE alx_book_store;

SELECT * FROM Books;

SELECT  
	COLUMN_NAME, 
    COLUMN_TYPE, 
    TABLE_SCHEMA = 'alx_book_store',
    TABLE_NAME = 'Books'
FROM INFORMATION_SCHEMA.COLUMNS;