# SQL: SELECT, WHERE, JOIN and GROUP BY

Study notes, reference cheatsheets, and query recipes for **SQL in Machine Learning and Feature Engineering**.

---

## 🧠 True SQL Logical Execution Order

```
1. FROM & JOIN     ──> Locate and unite physical tables
2. WHERE           ──> Filter individual row observations (before grouping)
3. GROUP BY        ──> Bucket rows into discrete groups
4. HAVING          ──> Filter groups based on aggregate statistics
5. SELECT          ──> Project columns, compute math expressions & aliases
6. DISTINCT        ──> Eliminate duplicate output rows
7. ORDER BY        ──> Sort the final materialized output
8. LIMIT / OFFSET  ──> Slice row pagination
```

> **Important**: Aggregate functions (like `COUNT(*)`, `AVG()`) cannot be evaluated in `WHERE` because `WHERE` filters rows before groups are formed. Always filter aggregate metrics in `HAVING`.

---

## ⚡ Key ML Feature Engineering SQL Patterns

### 1. Inactive Entity Retention with `LEFT JOIN`
```sql
SELECT 
    u.user_id,
    u.signup_date,
    COALESCE(COUNT(o.order_id), 0) AS total_orders,
    COALESCE(SUM(o.amount), 0.0) AS lifetime_spend
FROM users u
LEFT JOIN orders o ON u.user_id = o.user_id
GROUP BY u.user_id, u.signup_date;
```

### 2. Sequential & Temporal Features with Window Functions
```sql
SELECT 
    user_id,
    order_id,
    order_date,
    amount,
    -- Sequential purchase counter per customer
    ROW_NUMBER() OVER (
        PARTITION BY user_id ORDER BY order_date ASC
    ) AS purchase_sequence_idx,
    -- Previous purchase amount (lag feature)
    LAG(amount, 1) OVER (
        PARTITION BY user_id ORDER BY order_date ASC
    ) AS prev_order_amount,
    -- 3-order rolling moving average spend
    AVG(amount) OVER (
        PARTITION BY user_id 
        ORDER BY order_date ASC
        ROWS BETWEEN 2 PRECEDING AND CURRENT ROW
    ) AS rolling_3_order_avg
FROM orders;
```

### 3. In-Process Feature Extraction with DuckDB
```python
import duckdb

# Querying local Parquet files directly with vectorized SIMD:
df = duckdb.query("""
    SELECT user_id, COUNT(*) AS event_count, AVG(duration) AS mean_duration
    FROM 'data/raw/events_*.parquet'
    GROUP BY user_id
    HAVING COUNT(*) >= 5
""").to_df()
```

---

## 📁 Repository Files
- `SQL_Queries_Feature_Engineering_Reference.sql`: Tested SQL scripts covering feature extraction, point-in-time joins, and window function recipes.
