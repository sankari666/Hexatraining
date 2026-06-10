select * from customers; 

select customer_name,city,membership_type from customers;

select * from products order by price desc;  

select * from customers where city='Hyderabad'; 

select * from customers where membership_type='Gold'; 

select * from products where price between 500 and 5000; 

select * from products where category in ('Electronics','Fashion');  

select * from orders where order_date > '2026-01-01'; 

select * from payments where payment_mode='UPI'; 

select * from deliveries where delivery_status='Pending'; 

select count(*) from customers; 

select count(*) from orders; 

select count(*) from products; 

select sum(amount) from payments;  

select avg(amount) from payments;  

select max(amount) from payments; 

select city,count(*) from customers group by city;   

select category,count(*) from products group by category;   

select order_status,count(*) from orders group by order_status; 

select c.customer_name,o.order_id,o.order_date from customers c INNER JOIN orders o ON c.customer_id=o.customer_id; 

select o.order_id,p.product_name,o.quantity,p.price from order_items o INNER JOIN products p ON o.product_id=p.product_id; 

select c.customer_name,p.product_name,oi.quantity,o.order_date from customers c INNER JOIN orders o ON c.customer_id = o.customer_id 
INNER JOIN order_items oi ON o.order_id = oi.order_id INNER JOIN products p  ON oi.product_id = p.product_id; 

SELECT o.order_id,p.payment_mode,p.payment_status,p.amount FROM orders o INNER JOIN payments p ON o.order_id = p.order_id;  

SELECT o.order_id,d.delivery_partner,d.delivery_status FROM orders o INNER JOIN deliveries d ON o.order_id = d.order_id;  

select c.customer_id,c.city,o.order_id,o.order_date,p.product_name,p.category,oi.quantity,p.price,py.payment_status,d.delivery_status
from customers c INNER JOIN orders o ON c.customer_id=o.customer_id INNER JOIN order_items oi ON o.order_id=oi.order_id
INNER JOIN products p ON oi.product_id=p.product_id INNER JOIN payments py ON o.order_id=py.order_id INNER JOIN deliveries d ON o.order_id=d.order_id;  

SELECT c.city, SUM(pay.amount) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN payments pay ON o.order_id = pay.order_id GROUP BY c.city; 

SELECT c.customer_name, SUM(pay.amount) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN payments pay ON o.order_id = pay.order_id GROUP BY c.customer_id; 

SELECT p.product_name,SUM(oi.quantity) FROM products p INNER JOIN order_items oi ON p.product_id = oi.product_id GROUP BY p.product_id;  

SELECT p.category,SUM(oi.quantity * p.price) FROM products p INNER JOIN order_items oi ON p.product_id = oi.product_id GROUP BY p.category;

SELECT c.customer_name,COUNT(o.order_id) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id GROUP BY c.customer_id;

SELECT c.customer_name,COUNT(o.order_id) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id 
GROUP BY c.customer_id having count(o.order_id)>1;

SELECT p.category,SUM(oi.quantity * p.price) FROM products p INNER JOIN order_items oi ON p.product_id = oi.product_id 
GROUP BY p.category HAVING SUM(oi.quantity * p.price) > 10000;

SELECT city,COUNT(*) FROM customers GROUP BY city HAVING COUNT(*) > 2;

SELECT p.product_name,SUM(oi.quantity) FROM products p INNER JOIN order_items oi ON p.product_id=oi.product_id 
GROUP BY p.product_id having SUM(oi.quantity)>3;

select * from customers where customer_id in(select customer_id from orders);

select * from customers where customer_id not in(select customer_id from orders);

select * from products where product_id not in (select product_id from order_items);

select * from orders where order_id IN (select order_id from payments where amount>(select avg(amount) from payments));

SELECT c.customer_name FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id INNER JOIN payments p
ON o.order_id = p.order_id WHERE p.amount = (SELECT MAX(amount) FROM payments);

SELECT * FROM products WHERE price > (SELECT AVG(price) FROM products);

SELECT DISTINCT c.* FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id INNER JOIN order_items oi
ON o.order_id = oi.order_id INNER JOIN products p ON oi.product_id = p.product_id WHERE p.category = 'Electronics';

SELECT * FROM orders WHERE order_id IN ( SELECT order_id FROM payments WHERE payment_status = 'Success');

SELECT * FROM orders WHERE order_id not IN ( SELECT order_id FROM deliveries WHERE delivery_status = 'Delivered');

SELECT c.customer_name,SUM(p.amount) FROM customers c INNER JOIN orders o ON c.customer_id = o.customer_id
INNER JOIN payments p ON o.order_id = p.order_id GROUP BY c.customer_id, c.customer_name
HAVING SUM(p.amount) > (SELECT AVG(total_spend) FROM ( SELECT SUM(p2.amount) AS total_spend FROM orders o2
JOIN payments p2 ON o2.order_id = p2.order_id GROUP BY o2.customer_id) as customer_averages );

select * from orders where order_id not in (select order_id from products);

select * from orders where order_id not in (select order_id from deliveries);

select * from payments where amount=0 or amount is null;

select * from orders where order_id in (select order_id from payments where payment_status='Success') and order_status ='Cancelled';

select * from orders where order_id in (select order_id from deliveries where delivery_status='Delivered') and 
order_id in (select order_id from payments where payment_status='Failed');

select * from order_items where product_id not in (select product_id from products);

select * from orders where customer_id not in (select customer_id from customers);
