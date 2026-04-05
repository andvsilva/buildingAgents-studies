import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = '../database/olist.sqlite'
db_connection = sqlite3.connect(db_path)

# queries
query = """
SELECT
    AVG(order_total) AS avg_ticket
FROM (
    SELECT
        order_id,
        SUM(payment_value) AS order_total
    FROM order_payments
    GROUP BY order_id
);
"""

df_status = pd.read_sql(query, db_connection)

print(df_status)

db_connection.close()
