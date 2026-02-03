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
