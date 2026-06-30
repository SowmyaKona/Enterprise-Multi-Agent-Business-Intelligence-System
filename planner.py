from models.state import AgentState
from llm import llm
from prompts.planner_prompt import planner_prompt
from tools.tool_registry import tools

planner_chain = planner_prompt | llm.bind_tools(tools)

def planner(state: AgentState):

    response = planner_chain.invoke(
        {
            "messages": state["messages"]
        }
    )
    print("\n==============================")
    print(response)
    print("==============================\n")

    return {"messages": [response],}