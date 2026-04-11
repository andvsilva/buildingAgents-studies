import sqlite3
import pandas as pd
from rich import print
import matplotlib.pyplot as plt


db_path = '../datasets/datasql.db'
db_connection = sqlite3.connect(db_path)

# queries
query = """
SELECT SUM(total_amount) AS total_revenue
FROM orders;
"""

df_status = pd.read_sql(query, db_connection)
print(df_status)

db_connection.close()
