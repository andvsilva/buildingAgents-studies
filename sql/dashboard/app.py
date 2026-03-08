import streamlit as st
import plotly.express as px
import pandas as pd
from sqlalchemy import create_engine

st.set_page_config(layout="wide")

# Database connection
engine = create_engine(
    "postgresql+psycopg2://andrevsilva:andrevsilva@localhost:5432/datasql"
)

customers = pd.read_sql("SELECT * FROM customers", engine)
products = pd.read_sql("SELECT * FROM products", engine)
orders = pd.read_sql("SELECT * FROM orders", engine)

# Convert to datetime
customers["birth_date"] = pd.to_datetime(customers["birth_date"])
today = pd.Timestamp.today()
customers["age"] = (today - customers["birth_date"]).dt.days // 365

# Dictionary of dataframes
dataframes = {
    "Customers": customers,
    "Products": products,
    "Orders": orders
}

# Sidebar dataset selection
dataset = st.sidebar.selectbox("Choose dataset", list(dataframes.keys()))

df = dataframes[dataset]

st.title(f"{dataset} Dataset")

st.dataframe(df.head())

# Column selection
columns = df.columns.tolist()

col1 = st.selectbox("Column for histogram", columns)

col2 = st.selectbox(
    "Color by (optional)",
    ["None"] + columns
)

# Plot
if col2 == "None":

    fig = px.histogram(
        df,
        x=col1,
        template="plotly_dark"
    )

else:

    fig = px.histogram(
        df,
        x=col1,
        color=col2,
        barmode="overlay",
        template="plotly_dark"
    )

st.plotly_chart(fig, use_container_width=True)