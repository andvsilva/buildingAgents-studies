from google.cloud import bigquery

client = bigquery.Client()

query = """
SELECT user_id, SUM(amount) AS total_spent
FROM learning.orders
GROUP BY user_id
"""

df = client.query(query).to_dataframe()
print(df)
