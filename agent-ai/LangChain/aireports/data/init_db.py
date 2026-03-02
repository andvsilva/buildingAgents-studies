from sqlalchemy import create_engine, text
import os

os.makedirs("data", exist_ok=True)

DATABASE_URL = "sqlite:///data/finance.db"

engine = create_engine(DATABASE_URL)

with engine.connect() as conn:
    conn.execute(text("""
        CREATE TABLE IF NOT EXISTS investments (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            asset_name TEXT,
            category TEXT,
            annual_return FLOAT
        )
    """))

    conn.execute(text("""
        INSERT INTO investments (asset_name, category, annual_return)
        VALUES
        ('Tesouro Selic', 'Fixed Income', 0.135),
        ('CDB Banco X', 'Fixed Income', 0.145),
        ('PETR4', 'Stock', 0.22),
        ('IVVB11', 'ETF', 0.18)
    """))

    conn.commit()

print("Database created successfully.")