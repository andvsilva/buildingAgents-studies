import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px

engine = create_engine(
    "postgresql+psycopg2://andrevsilva:andrevsilva@localhost:5432/datasql"
)

customers = pd.read_sql("SELECT * FROM customers", engine)
products = pd.read_sql("SELECT * FROM products", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)

print(orders)