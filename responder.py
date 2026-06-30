from llm import llm
from langchain_core.messages import SystemMessage
from models.state import AgentState

SYSTEM_PROMPT = """
You are a Business Report Generator.
Read the complete conversation including tool results.
Generate a clear business report.

Include:
- Summary
- Key Findings
- Recommendation

Do not mention tool calls.
"""

def responder(state: AgentState):

    messages = [
        SystemMessage(content=SYSTEM_PROMPT),
        *state["messages"]
    ]

    response = llm.invoke(messages)
    return {"messages": [response]}