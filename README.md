# E-commerce Data Exercise

This repository contains a complete A-SDLC (Accelerated Software Development Life Cycle) exercise for generating synthetic e-commerce data, ingesting it into a SQLite database, and performing complex SQL queries with multi-table joins.

## Overview

The exercise demonstrates:
- Synthetic data generation for e-commerce entities
- Database schema design with foreign key relationships
- Data ingestion using Python and SQLite
- Complex SQL queries with joins, aggregations, and window functions

## Files Included

### Data Files
- `customers.csv` - 50 customer records (customer_id, name, email, join_date, country)
- `products.csv` - 50 product records (product_id, name, category, price, sku)
- `orders.csv` - 100 order records (order_id, customer_id, order_date, total_amount)
- `order_items.csv` - 150 order item records (order_item_id, order_id, product_id, quantity, unit_price)
- `inventory.csv` - 100 inventory records (product_id, warehouse, stock_qty)

### Scripts
- `ingest_to_sqlite.py` - Creates SQLite database and loads CSV data
- `check_db.py` - Verifies database tables and row counts
- `sql_query.py` - Executes complex SQL query for customer analytics

### Database
- `ecommerce.db` - SQLite database with all loaded data

## Prerequisites

- Python 3.x
- pandas (`pip install pandas`)
- SQLite3 (included with Python)

## Usage

1. **Ingest Data:**
   ```bash
   python ingest_to_sqlite.py
   ```

2. **Check Database:**
   ```bash
   python check_db.py
   ```

3. **Run Analytics Query:**
   ```bash
   python sql_query.py
   ```

## SQL Query Details

The main query in `sql_query.py` performs a comprehensive analysis:
- Joins customers, orders, order_items, and products tables
- Calculates top 10 customers by total spent in the last 12 months
- Includes metrics: total_orders, total_items, total_spent, top_category
- Uses CTEs (Common Table Expressions) for complex aggregations
- Employs window functions for ranking

## Schema

### Tables
- **customers**: Customer information
- **products**: Product catalog
- **orders**: Order headers
- **order_items**: Order line items
- **inventory**: Stock levels by warehouse

### Relationships
- orders.customer_id → customers.customer_id
- order_items.order_id → orders.order_id
- order_items.product_id → products.product_id
- inventory.product_id → products.product_id

## Results

The SQL query outputs a CSV with columns:
- customer_id, name, email, total_orders, total_items, total_spent, top_category

Example output shows top customers with their purchase metrics and preferred product category.

## GitHub Repository

This code is hosted on GitHub: https://github.com/mdmahbub-2003/Diligent.git
