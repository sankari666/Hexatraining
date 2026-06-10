CREATE DATABASE training_sql_db;
USE training_sql_db;
CREATE TABLE books
(
book_id INT PRIMARY KEY,
book_title VARCHAR(100),
category VARCHAR(50),
author VARCHAR(50),
price DECIMAL(10,2),
stock INT,
published_year INT
);
INSERT INTO books VALUES
(1, 'Python Basics', 'Programming', 'Ravi Kumar', 550, 30, 2021),
(2, 'Advanced SQL', 'Database', 'Priya Sharma', 750, 15, 2020),
(3, 'Data Engineering Guide', 'Data', 'Amit Verma', 1200, 10, 2023),
(4, 'Machine Learning Start', 'AI', 'Neha Reddy', 950, 8, 2022),
(5, 'Excel for Business', 'Business', 'Kiran Rao', 400, 50, 2019),
(6, 'Power BI Reports', 'Data', 'Sneha Patel', 850, 12, 2021),
(7, 'Java Fundamentals', 'Programming', 'Arjun Mehta', 600, 20, 2018),
(8, 'Cloud Basics', 'Cloud', 'Rahul Nair', 700, 18, 2022),
(9, 'SQL Interview Prep', 'Database', 'Farhan Ali', 500, 25, 2024),
(10, 'AI for Beginners', 'AI', 'Meera Singh', 650, 5, 2023);
SELECT * FROM books;
SELECT book_title,category,price from books;
SELECT DISTINCT category from books;
SELECT * FROM books where category='Programming';
SELECT * FROM books where price>700;
SELECT * FROM books where stock<15;
SELECT * FROM books WHERE category IN ('Programming','Database','AI');
SELECT * FROM books WHERE price BETWEEN 500 AND 900;
SELECT * FROM books WHERE book_title LIKE '%SQL%';
SELECT * FROM books WHERE book_title LIKE 'Data%';
SELECT * FROM books ORDER BY price DESC;
SELECT * FROM books ORDER BY category ASC,price DESC;
SELECT COUNT(*) FROM books;
SELECT MAX(price) FROM books;
SELECT MIN(price) FROM books;
SELECT AVG(price) FROM books;
SELECT SUM(stock) FROM books;
SELECT category,COUNT(*) from books group by category;
SELECT category,avg(price) from books group by category;
SELECT category,SUM(stock) from books group by category;
SELECT category from books where stock>1;
SELECT category from books group by category HAVING AVG(price)>700;
CREATE TABLE departments
(
department_id INT PRIMARY KEY,
department_name VARCHAR(50),
location VARCHAR(50)
);
CREATE TABLE employees
(
employee_id INT PRIMARY KEY,
employee_name VARCHAR(50),
department_id INT,
salary DECIMAL(10,2),
city VARCHAR(50),
manager_id INT
);
INSERT INTO departments VALUES
(10, 'IT', 'Hyderabad'),
(20, 'HR', 'Bangalore'),
(30, 'Finance', 'Mumbai'),
(40, 'Sales', 'Delhi'),
(50, 'Marketing', NULL);
INSERT INTO employees VALUES
(101, 'Rahul Sharma', 10, 75000, 'Hyderabad', 201),
(102, 'Priya Reddy', 10, 85000, 'Bangalore', 201),
(103, 'Amit Kumar', 20, 55000, NULL, 202),
(104, 'Sneha Patel', 30, 65000, 'Mumbai', 203),
(105, 'Arjun Verma', NULL, 60000, 'Chennai', 204),
(106, 'Neha Singh', 60, 50000, 'Delhi', NULL),
(107, 'Farhan Ali', 40, NULL, 'Hyderabad', 205),
(108, 'Meera Nair', 10, 90000, 'Pune', 201);
SELECT
   e.employee_name,
   e.salary,
   d.department_name,
   d.location
from employees e
INNER JOIN departments d 
ON e.department_id=d.department_id;
SELECT
   e.employee_name,
   e.salary,
   d.department_name,
   d.location
from employees e
LEFT JOIN departments d 
ON e.department_id=d.department_id;
SELECT e.employee_name FROM employees e WHERE e.department_id AND e.manager_id IS NULL;
SELECT 
   d.department_name,
   d.location,
   e.employee_name,
   e.salary,
   e.city
FROM departments d
RIGHT JOIN employees e ON d.department_id=e.department_id;
SELECT d.department_name 
FROM departments d 
WHERE NOT EXISTS (
    SELECT 1 
    FROM employees e 
    WHERE e.department_id = d.department_id
);
SELECT employee_name from employees WHERE salary IS NULL;
SELECT employee_name from employees WHERE city IS NULL;
SELECT department_name from departments WHERE location IS NULL;
SELECT d.department_name, COUNT(e.department_id) AS employee_count
FROM employees e 
INNER JOIN departments d ON e.department_id = d.department_id 
GROUP BY d.department_name
HAVING COUNT(e.department_id) > 2;
CREATE TABLE customers_new
(

customer_id INT PRIMARY KEY,
customer_name VARCHAR(50),
city VARCHAR(50),
membership_type VARCHAR(30)
);

CREATE TABLE payments
(
payment_id INT PRIMARY KEY,
customer_id INT,
amount DECIMAL(10,2),
payment_mode VARCHAR(30),
payment_status VARCHAR(30)
);

INSERT INTO customers_new VALUES
(1, 'Ramesh Gupta', 'Hyderabad', 'Gold'),
(2, 'Sana Khan', 'Bangalore', 'Silver'),
(3, 'John Mathew', 'Mumbai', 'Gold'),
(4, 'Ayesha Begum', 'Chennai', 'Bronze'),
(5, 'Vikram Rao', 'Delhi', 'Silver'),
(6, 'Divya Sharma', 'Pune', NULL);

INSERT INTO payments VALUES
(1001, 1, 15000, 'UPI', 'Success'),
(1002, 1, 8000, 'Card', 'Success'),
(1003, 2, 5000, 'Cash', 'Pending'),
(1004, 3, 22000, 'UPI', 'Success'),
(1005, 7, 12000, 'Card', 'Failed'),
(1006, NULL, 3000, 'Cash', 'Pending'),
(1007, 4, NULL, 'UPI', 'Success'),
(1008, 5, 7000, NULL, 'Success');
SELECT * FROM customers_new WHERE customer_id IN (SELECT customer_id FROM payments);
SELECT * FROM customers_new WHERE customer_id NOT IN (SELECT customer_id FROM payments);
SELECT customer_id, AVG(amount) 
FROM payments 
GROUP BY customer_id 
HAVING AVG(amount) > (SELECT AVG(amount) FROM payments);
SELECT customer_id from customers_new WHERE customer_id IN (SELECT max(amount) from payments);
SELECT customer_id from customers_new WHERE membership_type='Gold' AND customer_id IN (SELECT customer_id from payments);