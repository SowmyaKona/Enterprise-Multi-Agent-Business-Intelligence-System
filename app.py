import streamlit as st

from workflow.graph import graph
from langchain_core.messages import HumanMessage

st.set_page_config(
    page_title="Enterprise Multi-Agent Business Analyst",
    page_icon="🤖",
    layout="wide"
)

# ===========================
# Sidebar
# ===========================

with st.sidebar:
    st.title("🤖 Enterprise AI Agent")
    st.divider()

    st.subheader("Architecture")
    st.markdown("""
- **Supervisor Agent**
- **Planner Agent (ReAct)**
- **Response Agent**
""")
    st.divider()

    st.subheader("Tools")
    st.markdown("""
- SQL Tool
- Neo4j Knowledge Graph
- Business Rules Tool
- Python Analysis Tool
""")
    
# ===========================
# Main Page
# ===========================

st.title("🤖 Enterprise Multi-Agent Business Analyst")
st.write("Ask questions about sales, customers, employees, products, suppliers, and company policies.")

# Session State
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display Previous Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# User Input
prompt = st.chat_input("e.g. Which region generated the highest revenue?")

if prompt:
    st.session_state.messages.append(
        {
            "role": "user",
            "content": prompt
        }
    )

    with st.chat_message("user"):
        st.markdown(prompt)

    with st.spinner("Analyzing..."):
        result = graph.invoke(
            {
                "messages": [
                    HumanMessage(content=prompt)
                ]
            }
        )

        print("\n========== RESULT ==========")
        print(result)
        print("============================")

        from langchain_core.messages import AIMessage

        response = ""

        for msg in reversed(result["messages"]):
            if isinstance(msg, AIMessage) and msg.content:
                response = msg.content
                break


    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": response
        }
    )

    with st.chat_message("assistant"):
        st.markdown(response)

        