from langgraph.graph import StateGraph, START, END
from langgraph.prebuilt import ToolNode
from models.state import AgentState
from agents.supervisor import supervisor
from agents.planner import planner
from agents.responder import responder
from tools.tool_registry import tools
from langchain_core.messages import AIMessage

def should_continue(state: AgentState):
    last_message = state["messages"][-1]

    if isinstance(last_message, AIMessage) and last_message.tool_calls:
        return "tools"

    return "responder"

builder = StateGraph(AgentState)
# -----------------------------
# Nodes
# -----------------------------
builder.add_node("supervisor", supervisor)
builder.add_node("planner", planner)
builder.add_node("tools", ToolNode(tools))
builder.add_node("responder", responder)

# -----------------------------
# Edges
# -----------------------------
builder.add_edge(START, "supervisor")
builder.add_edge("supervisor", "planner")

# Planner -> ToolNode OR Responder

builder.add_conditional_edges(
    "planner",
    should_continue,
    {
        "tools": "tools",
        "responder": "responder",
    },
)

# After tool execution go back to planner
builder.add_edge("tools", "planner")

# Final response
builder.add_edge("responder", END)

graph = builder.compile()