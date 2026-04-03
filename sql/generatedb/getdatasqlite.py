from faker import Faker
import pandas as pd
import random
import uuid
from sqlalchemy import create_engine, text
from tqdm import tqdm

# -----------------------------
# SETUP
# -----------------------------
fake = Faker()
Faker.seed(42)
random.seed(42)

engine = create_engine("sqlite:///datasql.db")

# SQLite performance tuning
with engine.connect() as conn:
    conn.execute(text("PRAGMA journal_mode=WAL;"))
    conn.execute(text("PRAGMA synchronous=OFF;"))

# dataset size
n_customers = 10000
n_products = 10000
n_orders = 20000
BATCH_SIZE = 5000

# -----------------------------
# CUSTOMERS
# -----------------------------
customers = []

for _ in tqdm(range(n_customers), desc="Generating customers"):
    signup = fake.date_between(start_date="-3y", end_date="today")

    customers.append({
        "customer_id": str(uuid.uuid4()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=80),  # ✅ FIXED
        "gender": random.choice(["Male", "Female"]),
        "street": fake.street_address(),
        "city": fake.city(),
        "state": fake.state(),
        "country": fake.country(),
        "zipcode": fake.postcode(),
        "signup_date": signup,
        "customer_segment": random.choice(["Basic","Silver","Gold","VIP"]),
        "loyalty_points": random.randint(0,5000),
        "marketing_optin": random.choice([True, False]),
        "last_login": fake.date_time_between(start_date=signup)
    })

df_customers = pd.DataFrame(customers)

df_customers.to_sql("customers", engine, if_exists="replace", index=False, method="multi")


# -----------------------------
# PRODUCTS
# -----------------------------
product_categories = ["Electronics","Accessories","Office","Gaming","Home"]

products = []

for i in tqdm(range(1, n_products), desc="Generating products"):
    price = round(random.uniform(10,5000),2)

    products.append({
        "product_id": i,
        "product_name": fake.word().capitalize(),
        "category": random.choice(product_categories),
        "brand": fake.company(),
        "price": price,
        "cost": round(price * random.uniform(0.4,0.7),2),
        "weight_kg": round(random.uniform(0.1,5),2),
        "color": fake.color_name(),
        "release_date": fake.date_between(start_date="-5y"),
        "warranty_months": random.choice([6,12,24]),
        "rating": round(random.uniform(2.5,5.0),1),
        "reviews_count": random.randint(0,5000),
        "stock_quantity": random.randint(0,1000),
        "supplier": fake.company(),
        "origin_country": fake.country(),
        "is_active": random.choice([True, True, True, False])
    })

df_products = pd.DataFrame(products)

df_products.to_sql("products", engine, if_exists="replace", index=False, method="multi")


# -----------------------------
# ORDERS (BATCHED)
# -----------------------------
customer_ids = df_customers["customer_id"].values

# Convert products to faster access arrays
product_ids = df_products["product_id"].values
product_prices = df_products["price"].values

for start in range(0, n_orders, BATCH_SIZE):

    batch_size = min(BATCH_SIZE, n_orders - start)
    orders_batch = []

    for i in range(batch_size):

        idx = random.randint(0, len(product_ids) - 1)

        product_id = product_ids[idx]
        price = product_prices[idx]

        quantity = random.randint(1, 5)
        discount = random.choice([0,0,0,5,10,15])

        total = quantity * price * (1 - discount / 100)

        orders_batch.append({
            "order_id": start + i + 1,
            "customer_id": random.choice(customer_ids),
            "product_id": product_id,
            "quantity": quantity,
            "unit_price": price,
            "discount_percent": discount,
            "total_amount": round(total, 2),
            "order_date": fake.date_between(start_date="-1y"),
            "payment_method": random.choice(["credit_card","debit_card","pix","paypal"]),
            "payment_status": random.choice(["paid","pending","refunded"]),
            "shipping_method": random.choice(["standard","express","pickup"]),
            "shipping_cost": round(random.uniform(5,50),2),
            "order_status": random.choice(["processing","shipped","delivered","cancelled"]),
            "delivery_days": random.randint(1,10),
            "warehouse": random.choice(["SP01","SP02","RJ01","MG01"]),
            "sales_channel": random.choice(["website","mobile_app","marketplace"]),
            "coupon_used": random.choice([True, False]),
            "customer_rating": random.choice([1,2,3,4,5,None])
        })

    df_batch = pd.DataFrame(orders_batch)

    df_batch.to_sql(
        "orders",
        engine,
        if_exists="append",
        index=False,
        method="multi"
    )

    print(f"Inserted {start + batch_size} rows...")

print("✅ SQLite dataset created successfully!")