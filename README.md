# 🤖 Enterprise Multi-Agent Business Intelligence Assistant

## 📌 Overview

A Multi-Agent AI application built using LangGraph and LangChain that enables business users to ask natural language questions and receive structured business reports. The system uses ReAct reasoning to intelligently select enterprise tools such as SQLite, Neo4j Knowledge Graph, Business Rules Engine, and Python Analysis.

---

## 🚀 Features

- Multi-Agent Architecture using LangGraph
- ReAct-based Planning and Reasoning
- Intelligent Tool Selection
- SQLite-based Structured Data Retrieval
- Neo4j Knowledge Graph Integration
- Business Rules Engine
- Python Data Analysis Tool
- Automated Business Report Generation
- Interactive Streamlit Interface

---

## 🏗️ Architecture

### Agents

- Supervisor Agent
- Planner Agent (ReAct)
- Response Agent

### Tools

- SQL Tool
- Neo4j Knowledge Graph Tool
- Business Rules Tool
- Python Analysis Tool

---

## 🛠️ Tech Stack

- Python
- LangGraph
- LangChain
- Gemini 2.5 Flash
- SQLite
- Neo4j Aura
- Cypher
- SQLAlchemy
- Streamlit
- Pandas

---

## 📂 Project Structure

```text
Enterprise-Multi-Agent-Business-Intelligence-Assistant/
│
├── agents/
├── database/
├── data/
├── models/
├── prompts/
├── tools/
├── workflow/
├── app.py
├── llm.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Workflow

1. User submits a business query.
2. Supervisor Agent routes the request.
3. Planner Agent performs ReAct reasoning.
4. Planner selects the appropriate enterprise tool.
5. Tool retrieves the required information.
6. Response Agent generates a business report.
7. Report is displayed in Streamlit.

---

## 📊 Data Sources

- Customers
- Products
- Employees
- Suppliers
- Sales
- Business Rules

---

## 💡 Sample Questions

- Which customer generated the highest revenue?
- Show the discount policy.
- Which supplier provides Laptop Pro?
- List products purchased by ABC Technologies.
- Show warranty information for laptops.

---

## ▶️ Installation

### Clone Repository

```bash
git clone <repository-url>
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Create Database

```bash
python database/create_database.py
```

### Load Knowledge Graph

```bash
python database/load_graph.py
```

### Run Application

```bash
streamlit run app.py
```

---

## 📸 Screenshots

(Add application screenshots here)

---

## 🔮 Future Improvements

- Memory-enabled agents
- Hybrid RAG integration
- External API integration
- Authentication & Role-Based Access
- LangSmith Monitoring
- Docker Deployment

---

## 👤 Author

**Sowmya Kona**

B.Tech Artificial Intelligence

