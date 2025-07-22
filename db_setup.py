import pandas as pd
import sqlite3

conn = sqlite3.connect("ecommerce.db")

df_ad = pd.read_csv("datasets/Ad_Sales.csv")
df_total = pd.read_csv("datasets/Total_Sales.csv")
df_elig = pd.read_csv("datasets/Eligibility.csv")

df_ad.to_sql("ad_sales", conn, if_exists="replace", index=False)
df_total.to_sql("total_sales", conn, if_exists="replace", index=False)
df_elig.to_sql("eligibility", conn, if_exists="replace", index=False)

print("Database setup complete.")



