import sqlite3
import pandas as pd
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent  # Project root folder.
DATA_DIR = BASE_DIR / "data"   # Location of all csv files 
# Create database
DB_PATH = BASE_DIR / "database" / "enterprise.db"  # Location where enterprise.db will be created.

conn = sqlite3.connect(DB_PATH)

# Load CSV files
employees = pd.read_csv(DATA_DIR / "employees.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
suppliers = pd.read_csv(DATA_DIR / "suppliers.csv")
sales = pd.read_csv(DATA_DIR / "sales.csv")
business_rules = pd.read_csv(DATA_DIR / "business_rules.csv")

# Create tables
employees.to_sql("employees", conn, if_exists="replace", index=False)
customers.to_sql("customers", conn, if_exists="replace", index=False)
products.to_sql("products", conn, if_exists="replace", index=False)
suppliers.to_sql("suppliers", conn, if_exists="replace", index=False)
sales.to_sql("sales", conn, if_exists="replace", index=False)
business_rules.to_sql("business_rules", conn, if_exists="replace", index=False)

conn.commit()
conn.close()

print("enterprise.db created successfully.")