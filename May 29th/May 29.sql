CREATE DATABASE retail_db;
USE retail_db;
CREATE TABLE customers
(
     customer_id INT,
     customer_name VARCHAR(100),
     city VARCHAR(50)
);
INSERT INTO customers
VALUES
(1,'Raghul','Hyderabad'),
(2,'Priya','Bangalore'),
(3,'Amit','Mumbai');
SELECT * FROM customers;
SET SQL_SAFE_UPDATES=0;
/*UPDATE customers
SET city='Chennai'
WHERE customer_id=1;*/
DELETE FROM customers
WHERE city='Bangalore';
SET SQL_SAFE_UPDATES=1;
DROP TABLE product;
CREATE TABLE products
(
    product_id INT PRIMARY KEY,
    product_name VARCHAR(50),
    category VARCHAR(30),
    price DECIMAL(10,2),
    stock_quantity INT,
    supplier_city VARCHAR(30)
);
INSERT INTO products VALUES
(1,'Laptop','Electronics',55000,10,'Hyderabad'),
(2,'Mobile','Electronics',25000,25,'Bangalore'),
(3,'Printer','Electronics',18000,8,'Pune'),
(4,'Office Chair','Furniture',7500,15,'Mumbai'),
(5,'Desk','Furniture',12000,5,'Chennai'),
(6,'Notebook','Stationery',80,200,'Hyderabad'),
(7,'Pen','Stationery',20,500,'Delhi'),
(8,'Water Bottle','Accessories',500,50,'Bangalore');
SELECT product_name,price FROM products;
SELECT DISTINCT category from products;
SELECT * FROM products WHERE category='Electronics';
SELECT * FROM products WHERE price>10000 AND supplier_city='Bangalore';
SELECT * FROM products WHERE price>10000 OR supplier_city='Bangalore';
SELECT * FROM products WHERE NOT category='Electronics';
SELECT * FROM products WHERE supplier_city IN ('Hyderabad','Bangalore');
SELECT * FROM products where price BETWEEN 500 AND 20000;
SELECT * FROM products where product_name LIKE 'p%';
SELECT product_name AS product,price as Productprice FROM products;
SELECT * FROM products order by price desc;
SELECT COUNT(*) FROM products WHERE category='Electronics';
SELECT SUM(price) FROM products;
SELECT 
COUNT(*) AS Totalprics,
MAX(price) AS maxprice,
MIN(price) AS minprice,
AVG(price) as avgprice,
SUM(price) as Total 
FROM products;
SELECT category,
COUNT(*) AS categorycount
FROM products GROUP BY category;
USE retail_db;
