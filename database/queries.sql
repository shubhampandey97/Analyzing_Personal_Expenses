-- 1. Total amount spent in each category
SELECT category, SUM(amount_paid) AS total_spent
FROM expenses
GROUP BY category;

-- 2. Total amount spent using each payment mode
SELECT payment_mode, SUM(amount_paid) AS total_spent
FROM expenses
GROUP BY payment_mode;

-- 3. Total cashback received across all transactions
SELECT SUM(cashback) AS total_cashback FROM expenses;

-- 4. Top 5 most expensive categories
SELECT category, SUM(amount_paid) AS total_spent
FROM expenses
GROUP BY category
ORDER BY total_spent DESC
LIMIT 5;

-- 5. Amount spent on transportation using different payment modes
SELECT payment_mode, SUM(amount_paid) AS total_spent
FROM expenses
WHERE category = 'Transportation'
GROUP BY payment_mode;

-- 6. Transactions that resulted in cashback
SELECT * FROM expenses WHERE cashback > 0;

-- 7. Total spending in each month
SELECT MONTH(date) AS month, SUM(amount_paid) AS total_spent
FROM expenses
GROUP BY month
ORDER BY month;

-- 8. Months with highest spending in "Travel", "Entertainment", "Gifts"
SELECT MONTH(date) AS month, category, SUM(amount_paid) AS total_spent
FROM expenses
WHERE category IN ('Travel', 'Entertainment', 'Gifts')
GROUP BY month, category
ORDER BY total_spent DESC;

-- 9. Recurring expenses in specific months
SELECT category, COUNT(*) AS occurrences
FROM expenses
WHERE category IN ('Insurance', 'Property Tax')
GROUP BY category;

-- 10. Cashback earned in each month
SELECT MONTH(date) AS month, SUM(cashback) AS total_cashback
FROM expenses
GROUP BY month;

-- 11. Overall spending trend (monthly increase or decrease)
SELECT MONTH(date) AS month, SUM(amount_paid) AS total_spent
FROM expenses
GROUP BY month
ORDER BY month;

-- 12. Costs associated with different types of travel
SELECT category, SUM(amount_paid) AS total_cost
FROM expenses
WHERE category = 'Travel'
GROUP BY category;

-- 13. Grocery spending patterns (weekends vs weekdays)
SELECT 
    CASE WHEN DAYOFWEEK(date) IN (1, 7) THEN 'Weekend' ELSE 'Weekday' END AS day_type,
    SUM(amount_paid) AS total_spent
FROM expenses
WHERE category = 'Groceries'
GROUP BY day_type;

-- 14. High vs Low Priority Categories
SELECT category, SUM(amount_paid) AS total_spent,
       CASE WHEN SUM(amount_paid) > (SELECT AVG(amount_paid) FROM expenses) THEN 'High Priority' ELSE 'Low Priority' END AS priority
FROM expenses
GROUP BY category;

-- 15. Category contributing highest percentage of total spending
SELECT category, (SUM(amount_paid) / (SELECT SUM(amount_paid) FROM expenses) * 100) AS percentage
FROM expenses
GROUP BY category
ORDER BY percentage DESC
LIMIT 1;
