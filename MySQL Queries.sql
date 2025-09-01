-- Supermart Project Queries - MySQL

-- Create database
CREATE DATABASE IF NOT EXISTS Supermart;
USE Supermart;

-- Drop table if exists (clean start)
DROP TABLE IF EXISTS mart;

-- Create table with necessary columns
CREATE TABLE mart (
    invoice_id        INT AUTO_INCREMENT PRIMARY KEY,
    branch            VARCHAR(10),
    city              VARCHAR(100),
    category          VARCHAR(100),
    quantity          INT,
    unit_price        DECIMAL(10,2),
    total             DECIMAL(12,2),
    date              DATE,
    time              TIME,
    payment_method    VARCHAR(50),
    rating            DECIMAL(3,2),
    profit_margin     DECIMAL(5,2)   -- assumed % margin (e.g., 0.25 for 25%)
);

-- ✅ Now the analysis queries

-- Count total records
SELECT COUNT(*) AS total_records FROM mart;

-- Count payment methods and number of transactions by payment method
SELECT 
    payment_method,
    COUNT(*) AS no_payments
FROM mart
GROUP BY payment_method;

-- Count distinct branches
SELECT COUNT(DISTINCT branch) AS total_branches FROM mart;

-- Find the minimum quantity sold
SELECT MIN(quantity) AS min_quantity FROM mart;

-- Q1: Find payment methods, number of transactions, and quantity sold
SELECT 
    payment_method,
    COUNT(*) AS no_payments,
    SUM(quantity) AS no_qty_sold
FROM mart
GROUP BY payment_method;

-- Q2: Identify the highest-rated category in each branch
SELECT branch, category, avg_rating
FROM (
    SELECT 
        branch,
        category,
        AVG(rating) AS avg_rating,
        RANK() OVER(PARTITION BY branch ORDER BY AVG(rating) DESC) AS rnk
    FROM mart
    GROUP BY branch, category
) AS ranked
WHERE rnk = 1;

-- Q3: Identify the busiest day for each branch
SELECT branch, day_name, no_transactions
FROM (
    SELECT 
        branch,
        DAYNAME(date) AS day_name,   -- ✅ date is already DATE type
        COUNT(*) AS no_transactions,
        RANK() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS rnk
    FROM mart
    GROUP BY branch, DAYNAME(date)
) AS ranked
WHERE rnk = 1;

-- Q4: Total quantity of items sold per payment method
SELECT 
    payment_method,
    SUM(quantity) AS no_qty_sold
FROM mart
GROUP BY payment_method;

-- Q5: Average, min, and max rating of categories per city
SELECT 
    city,
    category,
    MIN(rating) AS min_rating,
    MAX(rating) AS max_rating,
    AVG(rating) AS avg_rating
FROM mart
GROUP BY city, category;

-- Q6: Total profit for each category
SELECT 
    category,
    SUM(unit_price * quantity * profit_margin) AS total_profit
FROM mart
GROUP BY category
ORDER BY total_profit DESC;

-- Q7: Most common payment method per branch
WITH cte AS (
    SELECT 
        branch,
        payment_method,
        COUNT(*) AS total_trans,
        RANK() OVER(PARTITION BY branch ORDER BY COUNT(*) DESC) AS rnk
    FROM mart
    GROUP BY branch, payment_method
)
SELECT branch, payment_method AS preferred_payment_method
FROM cte
WHERE rnk = 1;

-- Q8: Categorize sales into Morning, Afternoon, and Evening shifts
SELECT
    branch,
    CASE 
        WHEN HOUR(time) < 12 THEN 'Morning'
        WHEN HOUR(time) BETWEEN 12 AND 17 THEN 'Afternoon'
        ELSE 'Evening'
    END AS shift,
    COUNT(*) AS num_invoices
FROM mart
GROUP BY branch, shift
ORDER BY branch, num_invoices DESC;

-- Q9: Top 5 branches with highest revenue decrease ratio (2022 vs 2023)
WITH revenue_2022 AS (
    SELECT 
        branch,
        SUM(total) AS revenue
    FROM mart
    WHERE YEAR(date) = 2022
    GROUP BY branch
),
revenue_2023 AS (
    SELECT 
        branch,
        SUM(total) AS revenue
    FROM mart
    WHERE YEAR(date) = 2023
    GROUP BY branch
)
SELECT 
    r2022.branch,
    r2022.revenue AS last_year_revenue,
    r2023.revenue AS current_year_revenue,
    ROUND(((r2022.revenue - r2023.revenue) / r2022.revenue) * 100, 2) AS revenue_decrease_ratio
FROM revenue_2022 AS r2022
JOIN revenue_2023 AS r2023 ON r2022.branch = r2023.branch
WHERE r2022.revenue > r2023.revenue
ORDER BY revenue_decrease_ratio DESC
LIMIT 5;


-- Q10: Identify the branch–category combinations that received more than 2 low-rated feedbacks (rating < 3.0).
SELECT 
    branch,
    category,
    COUNT(*) AS low_rating_count
FROM mart
WHERE rating < 3.0
GROUP BY branch, category
HAVING COUNT(*) > 2
ORDER BY low_rating_count DESC, branch, category;

-- End of the project