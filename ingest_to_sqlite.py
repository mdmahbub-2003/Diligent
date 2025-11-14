import sqlite3
import pandas as pd
import os

# Create SQLite database
conn = sqlite3.connect('ecommerce.db')
cursor = conn.cursor()

# Create tables
cursor.execute('''
CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    name TEXT,
    email TEXT,
    join_date DATE,
    country TEXT
)
''')

cursor.execute('''
CREATE TABLE products (
    product_id INTEGER PRIMARY KEY,
    name TEXT,
    category TEXT,
    price REAL,
    sku TEXT
)
''')

cursor.execute('''
CREATE TABLE orders (
    order_id INTEGER PRIMARY KEY,
    customer_id INTEGER,
    order_date DATE,
    total_amount REAL,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
)
''')

cursor.execute('''
CREATE TABLE order_items (
    order_item_id INTEGER PRIMARY KEY,
    order_id INTEGER,
    product_id INTEGER,
    quantity INTEGER,
    unit_price REAL,
    FOREIGN KEY (order_id) REFERENCES orders(order_id),
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

cursor.execute('''
CREATE TABLE inventory (
    product_id INTEGER,
    warehouse TEXT,
    stock_qty INTEGER,
    FOREIGN KEY (product_id) REFERENCES products(product_id)
)
''')

# Load CSV data
customers_df = pd.read_csv('customers.csv')
products_df = pd.read_csv('products.csv')
orders_df = pd.read_csv('orders.csv')
order_items_df = pd.read_csv('order_items.csv')
inventory_df = pd.read_csv('inventory.csv')

# Insert data
customers_df.to_sql('customers', conn, if_exists='append', index=False)
products_df.to_sql('products', conn, if_exists='append', index=False)
orders_df.to_sql('orders', conn, if_exists='append', index=False)
order_items_df.to_sql('order_items', conn, if_exists='append', index=False)
inventory_df.to_sql('inventory', conn, if_exists='append', index=False)

# Print summary
print(f"customers: {len(customers_df)} rows")
print(f"products: {len(products_df)} rows")
print(f"orders: {len(orders_df)} rows")
print(f"order_items: {len(order_items_df)} rows")
print(f"inventory: {len(inventory_df)} rows")

conn.commit()
conn.close()

print("Data ingestion complete. Database saved as ecommerce.db")
