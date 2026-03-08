from faker import Faker
import pandas as pd
import random
import uuid
from sqlalchemy import create_engine
from tqdm import tqdm   # <-- ADDED

fake = Faker()

# -----------------------------
# DATABASE CONNECTION
# -----------------------------
engine = create_engine(
    "postgresql+psycopg2://andrevsilva:andrevsilva@localhost:5432/datasql"
)

# dataset size
n_customers = 100000
n_products = 100
n_orders = 2000000

# -----------------------------
# CUSTOMERS TABLE (15 columns)
# -----------------------------
customers = []

for _ in tqdm(range(n_customers), desc="Generating customers"):  # <-- ADDED

    signup = fake.date_between(start_date="-3y", end_date="today")

    customers.append({
        "customer_id": str(uuid.uuid4()),
        "first_name": fake.first_name(),
        "last_name": fake.last_name(),
        "email": fake.email(),
        "phone": fake.phone_number(),
        "birth_date": fake.date_of_birth(minimum_age=18, maximum_age=80),
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


# -----------------------------
# PRODUCTS TABLE (15 columns)
# -----------------------------
product_categories = [
    "Electronics","Accessories","Office","Gaming","Home"
]

products = []

for i in tqdm(range(1,n_products), desc="Generating products"):  # <-- ADDED

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


# -----------------------------
# ORDERS TABLE (18 columns)
# -----------------------------
orders = []

customer_ids = df_customers["customer_id"].tolist()
product_ids = df_products["product_id"].tolist()

for i in tqdm(range(n_orders), desc="Generating orders"):  # <-- ADDED

    quantity = random.randint(1,5)
    product = df_products.sample(1).iloc[0]

    price = product["price"]
    discount = random.choice([0,0,0,5,10,15])
    total = quantity * price * (1 - discount/100)

    orders.append({
        "order_id": i+1,
        "customer_id": random.choice(customer_ids),
        "product_id": random.choice(product_ids),
        "quantity": quantity,
        "unit_price": price,
        "discount_percent": discount,
        "total_amount": round(total,2),
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

df_orders = pd.DataFrame(orders)


# -----------------------------
# SAVE TO DATABASE
# -----------------------------
df_customers.to_sql("customers", engine, if_exists="replace", index=False)
df_products.to_sql("products", engine, if_exists="replace", index=False)
df_orders.to_sql("orders", engine, if_exists="replace", index=False)

print("Fake relational dataset created successfully!")