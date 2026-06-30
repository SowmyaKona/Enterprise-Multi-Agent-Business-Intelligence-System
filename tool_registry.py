from tools.sql_tool import execute_sql
from tools.business_rules_tool import get_business_rule
from tools.graph_tool import query_graph
from tools.python_tool import analyze_data

tools = [
    execute_sql,
    get_business_rule,
    query_graph,
    analyze_data
]