from langchain_core.tools import tool
import pandas as pd

@tool
def analyze_data(data: str) -> str:
    """
    Perform simple data analysis on tool outputs.
    Use this tool for summaries, statistics and insights.
    """

    try:

        df = pd.DataFrame(eval(data))

        summary = {
            "rows": len(df),
            "columns": list(df.columns),
            "summary": df.describe(include="all").to_string()
        }

        return str(summary)

    except Exception as e:
        return f"Python Analysis Error: {str(e)}"