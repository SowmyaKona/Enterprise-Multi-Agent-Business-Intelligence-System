import os
from pathlib import Path
import pandas as pd
from dotenv import load_dotenv
from neo4j import GraphDatabase
load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

employees = pd.read_csv(DATA_DIR / "employees.csv")
customers = pd.read_csv(DATA_DIR / "customers.csv")
products = pd.read_csv(DATA_DIR / "products.csv")
suppliers = pd.read_csv(DATA_DIR / "suppliers.csv")
sales = pd.read_csv(DATA_DIR / "sales.csv")

with driver.session() as session:

    print("Creating Employee nodes...")

    for _, row in employees.iterrows():

        session.run(
            """
            MERGE (e:Employee {employee_id:$employee_id})
            SET e.name=$employee_name,
                e.role=$role,
                e.department=$department,
                e.region=$region
            """,
            employee_id=row["employee_id"],
            employee_name=row["employee_name"],
            role=row["role"],
            department=row["department"],
            region=row["region"]
        )

    print("Creating Customer nodes...")

    for _, row in customers.iterrows():

        session.run(
            """
            MERGE (c:Customer {customer_id:$customer_id})
            SET c.name=$customer_name,
                c.city=$city,
                c.state=$state,
                c.segment=$segment
            """,
            customer_id=row["customer_id"],
            customer_name=row["customer_name"],
            city=row["city"],
            state=row["state"],
            segment=row["segment"]
        )

    print("Creating Product nodes...")

    for _, row in products.iterrows():

        session.run(
            """
            MERGE (p:Product {product_id:$product_id})
            SET p.name=$product_name,
                p.category=$category,
                p.cost_price=$cost_price,
                p.selling_price=$selling_price
            """,
            product_id=row["product_id"],
            product_name=row["product_name"],
            category=row["category"],
            cost_price=float(row["cost_price"]),
            selling_price=float(row["selling_price"])
        )

    print("Creating Supplier nodes...")

    for _, row in suppliers.iterrows():

        session.run(
            """
            MERGE (s:Supplier {supplier_id:$supplier_id})
            SET s.name=$supplier_name,
                s.country=$country
            """,
            supplier_id=row["supplier_id"],
            supplier_name=row["supplier_name"],
            country=row["country"]
        )

    print("Creating REPORTS_TO relationships...")

    for _, row in employees.iterrows():

        if pd.notna(row["manager_id"]):

            session.run(
                """
                MATCH (e:Employee {employee_id:$employee})
                MATCH (m:Employee {employee_id:$manager})
                MERGE (e)-[:REPORTS_TO]->(m)
                """,
                employee=row["employee_id"],
                manager=row["manager_id"]
            )

    print("Creating SUPPLIED_BY relationships...")

    for _, row in products.iterrows():

        session.run(
            """
            MATCH (p:Product {product_id:$product})
            MATCH (s:Supplier {supplier_id:$supplier})
            MERGE (p)-[:SUPPLIED_BY]->(s)
            """,
            product=row["product_id"],
            supplier=row["supplier_id"]
        )

    print("Creating PURCHASED relationships...")

    for _, row in sales.iterrows():

        session.run(
            """
            MATCH (c:Customer {customer_id:$customer})
            MATCH (p:Product {product_id:$product})
            MERGE (c)-[r:PURCHASED]->(p)
            SET r.transaction_id=$transaction,
                r.date=$date,
                r.quantity=$quantity,
                r.discount=$discount,
                r.revenue=$revenue,
                r.region=$region
            """,
            customer=row["customer_id"],
            product=row["product_id"],
            transaction=row["transaction_id"],
            date=row["date"],
            quantity=int(row["quantity"]),
            discount=float(row["discount"]),
            revenue=float(row["revenue"]),
            region=row["region"]
        )

    print("Creating SOLD relationships...")

    for _, row in sales.iterrows():

        session.run(
            """
            MATCH (e:Employee {employee_id:$employee})
            MATCH (p:Product {product_id:$product})
            MERGE (e)-[r:SOLD]->(p)
            SET r.transaction_id=$transaction,
                r.quantity=$quantity,
                r.revenue=$revenue
            """,
            employee=row["employee_id"],
            product=row["product_id"],
            transaction=row["transaction_id"],
            quantity=int(row["quantity"]),
            revenue=float(row["revenue"])
        )

driver.close()

print("\nGraph loaded successfully into Neo4j Aura.")