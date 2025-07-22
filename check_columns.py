import sqlite3

conn = sqlite3.connect("ecommerce.db")
cursor = conn.cursor()

print("\n--- total_sales ---")
cursor.execute("PRAGMA table_info(total_sales);")
for col in cursor.fetchall():
    print(col)

print("\n--- ad_sales ---")
cursor.execute("PRAGMA table_info(ad_sales);")
for col in cursor.fetchall():
    print(col)
