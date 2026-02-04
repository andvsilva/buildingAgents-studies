import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = 'database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# queries
query = """
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
"""

df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
