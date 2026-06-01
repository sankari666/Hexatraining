create database retail_capstone_db;
use retail_capstone_db;
CREATE TABLE customers
(
customer_id INT PRIMARY KEY,
customer_name VARCHAR(100),
city VARCHAR(50),
state VARCHAR(50),
gender VARCHAR(10),
membership_type VARCHAR(30)
);
CREATE TABLE products
(
product_id INT PRIMARY KEY,
product_name VARCHAR(100),
category VARCHAR(50),
price DECIMAL(10,2)
);
CREATE TABLE orders
(
order_id INT PRIMARY KEY,
customer_id INT, 
FOREIGN KEY (customer_id) REFERENCES customers(customer_id),
order_date DATE,
order_status VARCHAR(30)
);
CREATE TABLE order_items
(
item_id INT PRIMARY KEY,
order_id INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
product_id INT,
FOREIGN KEY (product_id) REFERENCES products(product_id),
quantity INT
);
CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
order_id INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
payment_mode VARCHAR(30),
payment_status VARCHAR(30),
amount DECIMAL(10,2)
);
CREATE TABLE deliveries
(
delivery_id INT PRIMARY KEY,
order_id INT,
FOREIGN KEY (order_id) REFERENCES orders(order_id),
delivery_partner VARCHAR(50),
delivery_status VARCHAR(30),
delivery_city VARCHAR(50)
);
