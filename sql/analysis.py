import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = 'database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# queries
query = """
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
"""

df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
