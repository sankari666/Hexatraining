#CRUD operation
#CREATE
INSERT INTO expenses
(user_id, category_id, amount, expense_date, description)
VALUES
(1,1,250,'2026-06-10','Breakfast');
#READ
SELECT * FROM expenses;
SELECT *
FROM expenses
WHERE user_id = 1;
SELECT
e.expense_id,
u.full_name,
c.category_name,
e.amount,
e.expense_date,
e.description
FROM expenses e
JOIN users u
ON e.user_id = u.user_id
JOIN categories c
ON e.category_id = c.category_id;
#UPDATE
UPDATE expenses
SET amount = 350,
    description = 'Updated Breakfast'
WHERE expense_id = 1;
#DELETE
DELETE FROM expenses
WHERE expense_id = 1;
