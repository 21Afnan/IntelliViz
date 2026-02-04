# IntelliViz: Autonomous Data Analytics & Anomaly Detection Platform

[![License](https://img.shields.io/badge/license-MIT-blue)](LICENSE)

## Project Overview
**IntelliViz** is an autonomous data analytics and anomaly detection platform designed for real-world applications. It allows users to **upload datasets**, **analyze them automatically**, **generate interactive insights**, and **visualize results** through a **clickable dashboard**.  

This project is built with **commercial scalability in mind** while also serving as a Final Year Project. It demonstrates a **domain-agnostic SLM-powered analytics engine** integrated with **interactive visualization and chat-based insights**, ready for industrial, business, and IoT applications.

---

## 🔍 Features

- **Upload & Store Datasets:** Upload CSV files; full datasets stored for processing.
- **Autonomous Preprocessing:** Missing value handling, normalization, and cleaning.
- **Exploratory Data Analysis (EDA):** Automatic generation of statistics, correlations, and trends.
- **Insight Generation:** Natural-language explanations of data patterns and anomalies.
- **Interactive Dashboard:** Clickable, filterable charts built with Plotly & Streamlit.
- **Chat Interface:** Ask questions about your data and insights naturally.
- **Agentic Architecture:** One SLM acts as multiple agents — orchestrator, data agent, EDA agent, visualization agent, insight agent, and chat agent.

---

## 🎯 Phase A (Core Platform) Roadmap

**Goal:** Build a fully functional MVP with a **single LLM** as the brain.

**Pipeline:**

1. **CSV Upload → Backend API**
2. **Dataset Stored** in Supabase/PostgreSQL
3. **Orchestrator Agent** receives user prompt (e.g., "Analyze dataset for insights")
4. **Agent Roles:**
   - **Data Agent:** Preprocessing decisions  
   - **EDA Agent:** Compute stats, correlations, anomaly hints  
   - **Visualization Agent:** Suggest chart types & layout  
   - **Insight Agent:** Generate textual explanations  
5. **Processed Data & Insights Stored** in DB
6. **Streamlit Dashboard** renders clickable charts & filters
7. **Chat Interface** answers questions using insights and dashboard config

**Timeline (1 week MVP):**

| Day | Tasks |
|-----|-------|
| Day 1 | Repo setup, Supabase & FastAPI setup |
| Day 2 | CSV upload API, dataset storage |
| Day 3 | Preprocessing agent & backend pipeline |
| Day 4 | EDA agent + text insight generation |
| Day 5 | Visualization agent, dashboard creation |
| Day 6 | Orchestrator + Chat integration |
| Day 7 | Testing, polishing, demo workflow |

---

## 🛠️ Tech Stack

| Layer | Technology |
|-------|------------|
| **LLM / Agents** | Mistral 7B (local, fast, open-source), LangChain, Pydantic |
| **Backend** | FastAPI, Supabase (Postgres + Storage), Pandas/Polars, Celery / BackgroundTasks |
| **Frontend** | Streamlit, Plotly, Streamlit Chat / Gradio |
| **Deployment** | Docker (optional), Windows/Linux compatible |

---

## 🧩 Agentic System (Single LLM)

**Roles managed by one LLM via prompt engineering:**

- **Orchestrator:** Routes tasks based on user prompts  
- **Data Agent:** Cleans & preprocesses data  
- **EDA Agent:** Computes stats & trends  
- **Visualization Agent:** Chooses charts & layouts  
- **Insight Agent:** Converts analysis to textual insights  
- **Chat Agent:** Handles user queries in natural language  

> LLM handles reasoning and task routing; actual computation is executed by backend code for efficiency.

---

## 📁 GitHub Repo Structure
```bash
intelliviz/
│
├── backend/
│ ├── app/
│ │ ├── api/ # CSV upload, query, chat endpoints
│ │ ├── preprocessing/ # Preprocessing scripts
│ │ ├── eda/ # EDA computation
│ │ ├── visualization/ # Plotly chart generation
│ │ ├── agents/ # Orchestrator + agent prompts
│ │ ├── core/ # Config, database connection
│ │ ├── models/ # Optional ML models
│ │ ├── main.py # FastAPI entrypoint
│
├── frontend/
│ ├── dashboard/ # Streamlit dashboard components
│ ├── chat_ui/ # Chat interface
│
├── llm/
│ ├── prompts/ # Prompt templates for agents
│
├── data/
│ ├── raw/ # Uploaded CSVs
│ ├── processed/ # Preprocessed datasets
│
├── docker/
├── requirements.txt
└── README.md

```
---

## 🚀 How to Run Locally

1. Clone the repo:
```bash
git clone https://github.com/YourUsername/intelliviz.git
cd intelliviz
Install dependencies:

pip install -r requirements.txt
Start FastAPI backend:

uvicorn backend.app.main:app --reload
Start Streamlit frontend:

streamlit run frontend/dashboard/main.py
Upload CSV → View insights → Ask questions in chat → Interact with dashboard

👥 Collaboration
Supervisor: Dr. Hina Ali

Team Members: Afnan Shoukat, Usama Shahid, Dure Addan Noor

🔮 Future Work
Add IoT & real-time monitoring module (Phase B)

Integrate multi-LLM orchestration for larger datasets

Expand dashboard to multi-user SaaS platform

Add predictive maintenance & cybersecurity insights

📄 License
MIT License


---