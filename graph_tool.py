from langchain_core.tools import tool
from neo4j import GraphDatabase
import os
from dotenv import load_dotenv

load_dotenv()

URI = os.getenv("NEO4J_URI")
USERNAME = os.getenv("NEO4J_USERNAME")
PASSWORD = os.getenv("NEO4J_PASSWORD")

driver = GraphDatabase.driver(
    URI,
    auth=(USERNAME, PASSWORD)
)


@tool
def query_graph(cypher_query: str) -> str:
    """
    Execute a Cypher query on the Neo4j Knowledge Graph.
    Use this tool to retrieve relationships between
    employees, customers, products and suppliers.
    """

    try:
        with driver.session() as session:

            result = session.run(cypher_query)

            records = [record.data() for record in result]

            if not records:
                return "No matching records found."

            return str(records)

    except Exception as e:
        return f"Graph Error: {str(e)}"