-- SQL: SELECT, WHERE, JOIN and GROUP BY
-- Machine Learning Feature Engineering Reference Queries

-- 1. Aggregating User Transaction Statistics
SELECT 
    user_id,
    COUNT(order_id) AS total_orders,
    ROUND(AVG(order_amount)::numeric, 2) AS avg_order_value,
    MAX(order_date) AS last_active_date
FROM orders
WHERE order_date >= CURRENT_DATE - INTERVAL '90 days'
GROUP BY user_id
HAVING COUNT(order_id) >= 2
ORDER BY total_orders DESC;

-- 2. Preserving Inactive Users via LEFT JOIN
SELECT 
    u.user_id,
    u.signup_date,
    COALESCE(SUM(o.order_amount), 0.0) AS lifetime_value
FROM users u
LEFT JOIN orders o 
    ON u.user_id = o.user_id
GROUP BY u.user_id, u.signup_date;

-- 3. Temporal Sequence Features via Window Functions
SELECT 
    user_id,
    order_id,
    order_date,
    order_amount,
    ROW_NUMBER() OVER (
        PARTITION BY user_id 
        ORDER BY order_date ASC
    ) AS order_sequence_idx,
    LAG(order_amount, 1) OVER (
        PARTITION BY user_id 
        ORDER BY order_date ASC
    ) AS prev_order_amount
FROM orders;
