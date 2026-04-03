import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

engine = create_engine(
    "postgresql+psycopg2://andrevsilva:andrevsilva@localhost:5432/datasql"
)

query = """
SELECT * 
FROM orders
WHERE unit_price < 1000;
"""

#tablenames = ['customers', 'products', 'orders']

request = pd.read_sql(f"{query}", engine)
print(request)