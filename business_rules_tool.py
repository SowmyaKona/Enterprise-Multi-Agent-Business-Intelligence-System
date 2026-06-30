from pathlib import Path

from sqlalchemy import create_engine, text
from langchain_core.tools import tool

# Database Path
BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = BASE_DIR / "database" / "enterprise.db"

# SQLAlchemy Engine
engine = create_engine(f"sqlite:///{DB_PATH}")


@tool
def get_business_rule(category: str) -> str:
    """
    Retrieve business rules based on a category.
    Examples:
    Discount, Warranty, Returns, Shipping, Approval, Commission.
    """

    try:

        with engine.connect() as conn:

            result = conn.execute(
                text("""
                    SELECT title, description
                    FROM business_rules
                    WHERE LOWER(category)=LOWER(:category)
                """),
                {"category": category},
            )

            rows = result.fetchall()

            if not rows:
                return "No business rules found."

            output = []

            for row in rows:
                output.append(
                    {
                        "title": row[0],
                        "description": row[1]
                    }
                )

            return str(output)

    except Exception as e:
        return f"Business Rule Error: {str(e)}"