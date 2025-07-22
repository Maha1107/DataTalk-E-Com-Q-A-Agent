import sqlite3

def execute_sql_query(query: str):
    conn = sqlite3.connect("ecommerce.db")
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        rows = cursor.fetchall()
        return rows
    except Exception as e:
        return str(e)
    finally:
        conn.close()
