CREATE DATABASE IF NOT EXISTS PersonalExpenses;
USE PersonalExpenses;

-- Create a table for each month
CREATE TABLE IF NOT EXISTS expenses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    date DATE,
    category VARCHAR(50),
    payment_mode VARCHAR(50),
    description TEXT,
    amount_paid DECIMAL(10,2),
    cashback DECIMAL(10,2)
);
