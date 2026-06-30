from pathlib import Path
from sqlalchemy import create_engine, text
from langchain_core.tools import tool

# Database Path  - Locate the SQLite database
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "enterprise.db"

# SQLAlchemy Engine
engine = create_engine(f"sqlite:///{DB_PATH}")

@tool
def execute_sql(query: str) -> str:
    """
    Execute a SQL query on the enterprise database.
    Use this tool to retrieve information from the sales, customers,
    employees, products, and suppliers tables.
    """

    try:
        with engine.connect() as conn:

            result = conn.execute(text(query))

            rows = result.fetchall()
            columns = result.keys()

            if not rows:
                return "No records found."

            output = []

            for row in rows:
                output.append(dict(zip(columns, row)))

            return str(output)

    except Exception as e:
        return f"SQL Error: {str(e)}"