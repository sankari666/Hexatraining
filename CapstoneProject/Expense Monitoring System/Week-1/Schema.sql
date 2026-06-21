CREATE database HCapstone1;
USE HCapstone1;
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    full_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) UNIQUE NOT NULL,
    pass VARCHAR(255) NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
CREATE TABLE categories (
    category_id INT AUTO_INCREMENT PRIMARY KEY,
    category_name VARCHAR(50) NOT NULL
);
CREATE TABLE expenses (
    expense_id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT,
    category_id INT,
    amount DECIMAL(10,2) NOT NULL,
    expense_date DATE NOT NULL,
    description VARCHAR(255),
    FOREIGN KEY (user_id) REFERENCES users(user_id),
    FOREIGN KEY (category_id) REFERENCES categories(category_id)
);
INSERT INTO users(full_name,email,pass)
VALUES
('Siva Kumar','siva@gmail.com','pass123'),
('Ravi Kumar','ravi@gmail.com','pass456');
INSERT INTO categories(category_name)
VALUES
('Food'),
('Transport'),
('Shopping'),
('Bills');
INSERT INTO expenses(user_id,category_id,amount,expense_date,description)
VALUES
(1,1,500,'2026-06-01','Lunch'),
(1,2,200,'2026-06-02','Bus Ticket'),
(1,1,300,'2026-06-05','Dinner'),
(2,3,1500,'2026-06-03','Clothes'),
(2,4,2500,'2026-06-07','Electricity Bill');
