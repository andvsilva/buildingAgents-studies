### SQL studies

I’ll structure this like a mini data analyst bootcamp using SQL, and we’ll build skills incrementally. Since you already touch Python/Pandas, this will feel very natural.

🧠 What “Analysis with SQL” really means

You’re using SQL to:

- Explore data
- Answer business questions
- Summarize, group, filter, compare
- Prepare data for dashboards / ML

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

![](/pngs/table-customers.png)

### 💰 Basic revenue analysis (single table)

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
