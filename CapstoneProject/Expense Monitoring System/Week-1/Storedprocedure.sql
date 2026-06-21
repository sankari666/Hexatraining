#STORED PROCEDURE
DELIMITER $$
CREATE PROCEDURE MonthlyCategoryExpense(
    IN p_year INT,
    IN p_month INT
)
BEGIN
    SELECT
        c.category_name,
        SUM(e.amount) AS total_expense
    FROM expenses e
    JOIN categories c
        ON e.category_id = c.category_id
    WHERE YEAR(e.expense_date) = p_year
      AND MONTH(e.expense_date) = p_month
    GROUP BY c.category_name;

END $$
DELIMITER ;
CALL MonthlyCategoryExpense(2026,6);
