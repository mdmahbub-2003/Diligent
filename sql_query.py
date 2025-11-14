import sqlite3
import csv

# Connect to database
conn = sqlite3.connect('ecommerce.db')

# SQL Query
query = """
WITH customer_orders AS (
    SELECT
        c.customer_id,
        c.name,
        c.email,
        COUNT(DISTINCT o.order_id) as total_orders,
        SUM(oi.quantity) as total_items,
        SUM(oi.quantity * oi.unit_price) as total_spent
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    WHERE o.order_date >= date('now', '-12 months')
    GROUP BY c.customer_id, c.name, c.email
),
customer_categories AS (
    SELECT
        c.customer_id,
        p.category,
        SUM(oi.quantity) as category_quantity,
        ROW_NUMBER() OVER (PARTITION BY c.customer_id ORDER BY SUM(oi.quantity) DESC) as rn
    FROM customers c
    JOIN orders o ON c.customer_id = o.customer_id
    JOIN order_items oi ON o.order_id = oi.order_id
    JOIN products p ON oi.product_id = p.product_id
    WHERE o.order_date >= date('now', '-12 months')
    GROUP BY c.customer_id, p.category
)
SELECT
    co.customer_id,
    co.name,
    co.email,
    co.total_orders,
    co.total_items,
    co.total_spent,
    cc.category as top_category
FROM customer_orders co
JOIN customer_categories cc ON co.customer_id = cc.customer_id AND cc.rn = 1
ORDER BY co.total_spent DESC
LIMIT 10;
"""

# Execute query
cursor = conn.cursor()
cursor.execute(query)
results = cursor.fetchall()

# Print results as CSV
print("customer_id,name,email,total_orders,total_items,total_spent,top_category")
for row in results:
    print(','.join(str(x) for x in row))

conn.close()
