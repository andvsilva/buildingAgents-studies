---

# 📊 SQL Data Analysis Queries (SQLite Dataset)

This document contains **10 SQL queries (from basic to advanced)** designed to analyze the generated dataset (`customers`, `products`, `orders`).

---

## 🟢 1. Total Customers

```sql
SELECT COUNT(*) AS total_customers
FROM customers;
```

---

## 🟢 2. Total Revenue

```sql
SELECT SUM(total_amount) AS total_revenue
FROM orders;
```

---

## 🟡 3. Revenue by Payment Method

```sql
SELECT 
    payment_method,
    ROUND(SUM(total_amount), 2) AS revenue
FROM orders
GROUP BY payment_method
ORDER BY revenue DESC;
```

---

## 🟡 4. Top 10 Best-Selling Products

```sql
SELECT 
    p.product_name,
    SUM(o.quantity) AS total_sold
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.product_name
ORDER BY total_sold DESC
LIMIT 10;
```

---

## 🟡 5. Average Order Value (AOV)

```sql
SELECT 
    ROUND(AVG(total_amount), 2) AS avg_order_value
FROM orders;
```

---

## 🟠 6. Revenue by Product Category

```sql
SELECT 
    p.category,
    ROUND(SUM(o.total_amount), 2) AS revenue
FROM orders o
JOIN products p ON o.product_id = p.product_id
GROUP BY p.category
ORDER BY revenue DESC;
```

---

## 🟠 7. Top 5 Customers by Revenue

```sql
SELECT 
    c.first_name || ' ' || c.last_name AS customer_name,
    ROUND(SUM(o.total_amount), 2) AS total_spent
FROM orders o
JOIN customers c ON o.customer_id = c.customer_id
GROUP BY customer_name
ORDER BY total_spent DESC
LIMIT 5;
```

---

## 🔵 8. Monthly Revenue (Time Series)

```sql
SELECT 
    strftime('%Y-%m', order_date) AS month,
    ROUND(SUM(total_amount), 2) AS revenue
FROM orders
GROUP BY month
ORDER BY month;
```

---

## 🔵 9. Cancellation Rate

```sql
SELECT 
    ROUND(
        SUM(CASE WHEN order_status = 'cancelled' THEN 1 ELSE 0 END) * 100.0
        / COUNT(*), 
    2) AS cancellation_rate_percent
FROM orders;
```

---

## 🔴 10. Customer Segmentation (RFM Analysis)

```sql
SELECT 
    c.customer_id,

    -- Recency (days since last purchase)
    JULIANDAY('now') - JULIANDAY(MAX(o.order_date)) AS recency,

    -- Frequency (number of orders)
    COUNT(o.order_id) AS frequency,

    -- Monetary (total spend)
    ROUND(SUM(o.total_amount), 2) AS monetary

FROM customers c
JOIN orders o ON c.customer_id = o.customer_id
GROUP BY c.customer_id
ORDER BY monetary DESC;
```

---

# 🔥 Bonus: Advanced (Window Function)

## Cumulative Revenue Over Time

```sql
SELECT 
    order_date,
    SUM(total_amount) AS daily_revenue,
    SUM(SUM(total_amount)) OVER (ORDER BY order_date) AS cumulative_revenue
FROM orders
GROUP BY order_date
ORDER BY order_date;
```

---

# 🧠 Key Concepts Covered

* Aggregations (`SUM`, `AVG`, `COUNT`)
* `GROUP BY` and `ORDER BY`
* `JOIN` operations
* Time-based analysis (`strftime`)
* Conditional logic (`CASE WHEN`)
* Customer analytics (RFM)
* Window functions (`OVER`)

---

# 🚀 