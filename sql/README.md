## SQL studies

I’ll structure this like a mini data analyst bootcamp using SQL, and we’ll build skills incrementally. Since you already touch Python/Pandas, this will feel very natural.

### 🧠 What “Analysis with SQL” really means

You’re using SQL to:

- Explore data
- Answer business questions
- Summarize, group, filter, compare
- Prepare data for dashboards / ML

What is Analysis with SQL?

``` Analysis with SQL means using SQL to understand data.```

Instead of just storing or retrieving data, you use SQL to ask questions like:

 - How much did we sell?
 - What is happening over time?
 - Which products perform better?
 - Where are the problems?

```SQL becomes a thinking tool, not just a database language.```

Think of SQL like questions to data
Imagine the database is a big spreadsheet.

SQL lets you ask:

```sql
SELECT → What do I want to see?
FROM → From which table?
WHERE → Apply filters
GROUP BY → Group similar things
SUM / AVG / COUNT → Calculate numbers
```

### Install 

```bash
sudo apt install sqlite3 
```

### 🧩 What is the SAME in all SQLs (important)

These work everywhere:

```bash
SELECT
FROM
WHERE
GROUP BY
HAVING
ORDER BY
LIMIT
JOIN
COUNT, SUM, AVG, MIN, MAX
```

**If you master this, you already know ~80% of SQL.**

### 🆚 Main SQL flavors (analyst perspective)

1️⃣ SQLite

What you’re using now

Best for:

- Learning SQL
- Local analysis
- Prototypes
- Small datasets

Characteristics:

- File-based (database.bd)
- No server
- Very lightweight
- Minimal syntax

⚠️ Limitations:

- Weak date functions
- No advanced analytics
- Limited concurrency

## SQLite

To start - database to work it!

![](/pngs/datasqlite.png)

### Loading Database and Query

```python
import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = 'database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# list tables from the database
query = """
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name;
"""
df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
```

### Output: 

```bash
$ python analysis.py
                                 name
0                           customers
1                         geolocation
2                        leads_closed
3                     leads_qualified
4                         order_items
5                      order_payments
6                       order_reviews
7                              orders
8   product_category_name_translation
9                            products
10                            sellers

```

### Access the table

```python
import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = 'database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# get table customers with 10 lines
query = """
SELECT *
FROM customers
LIMIT 10;
"""
df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
```

### Output:

```bash
~/repo/buildingAgents-studies/sql on  main! ⌚ 10:31:21
$ python analysis.py
                        customer_id  ... customer_state
0  06b8999e2fba1a1fbc88172c00ba8bc7  ...             SP
1  18955e83d337fd6b2def6b18a428ac77  ...             SP
2  4e7b3e00288586ebd08712fdd0374a03  ...             SP
3  b2b6027bc5c5109e529d4dc6358b12c3  ...             SP
4  4f2d8ab171c80ec8364f7c12e35b23ad  ...             SP
5  879864dab9bc3047522c92c82e1212b8  ...             SC
6  fd826e7cf63160e536e0908c76c3f441  ...             SP
7  5e274e7a0c3809e14aba7ad5aae0d407  ...             MG
8  5adf08e34b2e993982a47070956c5c65  ...             PR
9  4b7139f34592b3a31687243a302fa75b  ...             MG

[10 rows x 5 columns]

```

### 1️⃣ 💰 Query: Total Revenue Analysis (single table)

```python
import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = 'database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# list tables from the database
query = """
SELECT SUM(payment_value) AS total_revenue
FROM order_payments;
"""
df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
```

```bash
$ python analysis.py
   total_revenue
0    16008872.12

```

### 2️⃣ Query: Revenue per month (classic time-series analysis)

```sql
SELECT
    substr(o.order_purchase_timestamp, 1, 7) AS month,
    SUM(p.payment_value) AS revenue
FROM orders o
JOIN order_payments p
  ON o.order_id = p.order_id
GROUP BY month
ORDER BY month;
```

### Output:

```sql
$ python analysis.py 
      month     revenue
0   2016-09      252.24
1   2016-10    59090.48
2   2016-12       19.62
3   2017-01   138488.04
4   2017-02   291908.01
5   2017-03   449863.60
6   2017-04   417788.03
7   2017-05   592918.82
8   2017-06   511276.38
9   2017-07   592382.92
10  2017-08   674396.32
11  2017-09   727762.45
12  2017-10   779677.88
13  2017-11  1194882.80
14  2017-12   878401.48
15  2018-01  1115004.18
16  2018-02   992463.34
17  2018-03  1159652.12
18  2018-04  1160785.48
19  2018-05  1153982.15
20  2018-06  1023880.50
21  2018-07  1066540.75
22  2018-08  1022425.32
23  2018-09     4439.54
24  2018-10      589.67
```

### 📌 Insight típico:

 - crescimento
 - sazonalidade
 - quedas suspeitas

## Por que essa query é “nível profissional”?

Ela combina:

 - 📅 dimensão temporal
 - 💰 métrica de negócio
 - 🔗 junção de tabelas
 - 📊 agregação
 - 🧠 clareza analítica

É exatamente o tipo de SQL esperado em:

 - Data Analyst
 - Data Scientist
 - Analytics Engineer

### 3️⃣ Query: Revenue by product category

🎯 What does this query answer?

“Which are the top 10 product categories by revenue?”

In this context, revenue means the sum of product prices sold, grouped by category.

```sql
SELECT
    t.product_category_name_english AS category,
    SUM(oi.price) AS revenue
FROM order_items oi
JOIN products p
  ON oi.product_id = p.product_id
JOIN product_category_name_translation t
  ON p.product_category_name = t.product_category_name
GROUP BY category
ORDER BY revenue DESC
LIMIT 10;
```

```sql
$ python analysis.py
                category     revenue
0          health_beauty  1258681.34
1          watches_gifts  1205005.68
2         bed_bath_table  1036988.68
3         sports_leisure   988048.97
4  computers_accessories   911954.32
5        furniture_decor   729762.49
6             cool_stuff   635290.85
7             housewares   632248.66
8                   auto   592720.11
9           garden_tools   485256.46
```

#### 🔥 Excelente para storytelling:

- Top 10 categorias que geram mais receita


- SQL query that calculates total revenue by product category, ranks categories by revenue in descending order, and returns the top 10 highest-performing categories.


### 4️⃣ Query: Average order value (AOV)

```sql
SELECT
    AVG(order_total) AS avg_ticket
FROM (
    SELECT
        order_id,
        SUM(payment_value) AS order_total
    FROM order_payments
    GROUP BY order_id
);
```
### Output:

```bash
$ python analysis.py
   avg_ticket
0  160.990267
```


### 5️⃣ Query: Average order rating

```sql
SELECT
    AVG(review_score) AS avg_review
FROM order_reviews;
```

### Output:

```bash
$ python analysis.py
   avg_review
0    4.086421
```

Ou por categoria 👀:

🎯 What does this query answer?

“What is the average customer review score for each product category?”

It ranks product categories by customer satisfaction, from highest to lowest average rating.

```sql
SELECT
    t.product_category_name_english AS category,
    AVG(r.review_score) AS avg_score
FROM order_reviews r
JOIN order_items oi ON r.order_id = oi.order_id
JOIN products p ON oi.product_id = p.product_id
JOIN product_category_name_translation t
  ON p.product_category_name = t.product_category_name
GROUP BY category
ORDER BY avg_score DESC;
```

### Output:

```bash
$ python analysis.py
                     category  avg_score
0           cds_dvds_musicals   4.642857
1   fashion_childrens_clothes   4.500000
2      books_general_interest   4.446266
3     costruction_tools_tools   4.444444
4                     flowers   4.419355
..                        ...        ...
66      fashion_male_clothing   3.641221
67             home_comfort_2   3.629630
68           office_furniture   3.493183
69        diapers_and_hygiene   3.256410
70      security_and_services   2.500000

[71 rows x 2 columns]
```

### 6️⃣ Query: Average delivery time

🎯 What does this query answer?

“On average, how many days does it take for an order to be delivered after it is purchased?”

```sql
SELECT
    AVG(
        julianday(order_delivered_customer_date) -
        julianday(order_purchase_timestamp)
    ) AS avg_delivery_days
FROM orders
WHERE order_delivered_customer_date IS NOT NULL;
```

### Output:

```bash
$ python analysis.py
   avg_delivery_days
0          12.558702
```

### 7️⃣ Top sellers by revenue

🎯 What does this query answer?

“Which sellers generated the highest total product revenue?”

Revenue here is defined as the sum of product prices sold by each seller.

```sql
SELECT
    s.seller_id,
    SUM(oi.price) AS revenue
FROM sellers s
JOIN order_items oi
  ON s.seller_id = oi.seller_id
GROUP BY s.seller_id
ORDER BY revenue DESC
LIMIT 10;
```

### Output:

```bash
$ python analysis.py
                          seller_id    revenue
0  4869f7a5dfa277a7dca6462dcf3b52b2  229472.63
1  53243585a1d6dc2643021fd1853d8905  222776.05
2  4a3ca9315b744ce9f8e9374361493884  200472.92
3  fa1c13f2614d7b5c4749cbc52fecda94  194042.03
4  7c67e1448b00f6e969d365cea6b010ab  187923.89
5  7e93a43ef30c4f03f38b393420bc753a  176431.87
6  da8622b14eb17ae2831f4ac5b9dab84a  160236.57
7  7a67c85e85bb2ce8582c35f2203ad736  141745.53
8  1025f0e2d44d7041d6cf58b6550e0bfa  138968.55
9  955fee9216a65b617aa5c0531780ce60  135171.70
```

### 8️⃣ Query: Simple churn analysis (customers with only one order)

🎯 What does this query answer?

“How many customers made only one purchase?”

This is a classic customer retention / repeat-purchase metric

```sql
SELECT
    COUNT(*) AS one_time_customers
FROM (
    SELECT
        customer_id,
        COUNT(order_id) AS total_orders
    FROM orders
    GROUP BY customer_id
)
WHERE total_orders = 1;
```

### Output:

```bash
$ python analysis.py
   one_time_customers
0               99441

```


✅ Perfect for learning and practicing

🧪 Practical advice for YOU (based on what you’re doing)

Since you are:

 - learning hands-on
 - using SQLite
 - doing analysis (not DBA work)

👉 Best path:

 - Learn SQLite deeply
 - Move to PostgreSQL
 - Then adapt easily to:
 - SQL Server (Power BI)
 - BigQuery (analytics)

### Comparing SQL types

| Feature          | SQLite | PostgreSQL | MySQL | SQL Server | BigQuery |
| ---------------- | ------ | ---------- | ----- | ---------- | -------- |
| Learning         | ⭐⭐⭐⭐⭐  | ⭐⭐⭐⭐       | ⭐⭐⭐   | ⭐⭐⭐        | ⭐⭐⭐      |
| Analytics        | ⭐⭐     | ⭐⭐⭐⭐⭐      | ⭐⭐⭐   | ⭐⭐⭐⭐       | ⭐⭐⭐⭐⭐    |
| Window functions | ❌      | ✅          | ✅     | ✅          | ✅        |
| Date functions   | ⚠️     | ✅          | ⚠️    | ⚠️         | ✅        |
| Big data         | ❌      | ❌          | ❌     | ❌          | ✅        |
