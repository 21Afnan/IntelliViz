# IntelliViz-Core

**Autonomous Data Analytics and Real-Time IoT Cybersecurity Monitoring Platform**  
Powered by a single Small Language Model (SLM) and an agentic system, IntelliViz enables organizations to upload any structured dataset (CSV), automatically preprocess it, generate EDA and insights, and visualize results in a fully interactive dashboard with natural language chat support.  

This repository contains the **Phase A MVP**: the core platform for data ingestion, SLM-driven analysis, EDA, insight generation, and clickable dashboards.

---

## 🚀 Project Overview

IntelliViz is designed to be a **commercial-grade SaaS platform** that:

- Works with **any structured dataset** (IoT, business, logs, industrial sensors, etc.)  
- Uses a **single SLM as the brain**, orchestrating multiple agent roles via prompt engineering  
- Automates **preprocessing, EDA, visualization, and insight generation**  
- Provides a **clickable dashboard** with filters, drill-down, and natural language querying  
- Stores the **full dataset and processed results** in a database (Supabase)  

**Phase A** demonstrates the **core platform MVP**.

---

## 📌 Phase A Scope (Core Platform)

**Objective:** Build a working MVP in 1 week that allows:

1. CSV upload and storage in Supabase  
2. SLM-based agentic system for:
   - Preprocessing decisions
   - EDA and statistical summaries
   - Chart suggestions and visualization layout
   - Insight generation in text  
3. Backend execution of all data operations (Pandas / Plotly)  
4. Interactive dashboard (Streamlit + Plotly)  
5. Natural language chat interface on insights and dashboard  
6. Full dataset storage (no metadata-only approach)  

**Outcome:** A fully functional, end-to-end pipeline for structured data analysis and visualization, ready for testing and future commercial scaling.

---

## 🧩 Architecture Overview
---
```bash
User Uploads CSV
↓
Data Ingestion Service (FastAPI)
↓
Store Full Dataset in Supabase
↓
User Prompt (Natural Language)
↓
Orchestrator Agent (SLM)
↓
┌───────────────┬───────────────┐
| Data Agent | EDA Agent |
└───────────────┴───────────────┘
↓
Insight Agent → Text Summaries
Visualization Agent → Chart Config (Plotly)
↓
Store Processed Data + EDA + Insights
↓
Interactive Dashboard + Chat Interface (Streamlit)
---
```
---

## 🧠 Agent Roles (Single SLM, Multiple Tasks)
```bash

| Agent Role           | Responsibility                                                                 |
|---------------------|-------------------------------------------------------------------------------|
| **Orchestrator**     | Receives user prompt and routes tasks to other agents                          |
| **Data Agent**       | Decides preprocessing steps (missing values, normalization, etc.)             |
| **EDA Agent**        | Generates statistical summaries, correlations, top features                   |
| **Visualization Agent** | Suggests chart types, layout, filters for interactive dashboard              |
| **Insight Agent**    | Converts statistical output into textual insights                              |
| **Chat Agent**       | Handles user queries about insights and dashboard visualizations              |

> **Note:** All agents are logical roles powered by **one SLM** through LangChain prompt engineering. Backend executes all actual data operations.
```
---

## 🛠️ Tech Stack

- **LLM / Agents:** Mistral 7B (local, fast, open-source), LangChain, Pydantic  
- **Backend:** FastAPI, Pandas / Polars, Supabase (Postgres + Storage)  
- **Frontend / Dashboard:** Streamlit + Plotly, Streamlit Chat / Gradio  
- **Async / Orchestration:** FastAPI BackgroundTasks or Celery (optional)  
- **Version Control:** Git + GitHub  

---

## 📁 Repository Structure
```bash
intelliviz-core/
│
├── backend/
│ ├── app/
│ │ ├── api/
│ │ │ ├── upload.py
│ │ │ ├── query.py
│ │ │ ├── chat.py
│ │ ├── core/
│ │ │ ├── config.py
│ │ │ ├── database.py
│ │ ├── preprocessing/
│ │ │ └── preprocess.py
│ │ ├── eda/
│ │ │ └── eda.py
│ │ ├── visualization/
│ │ │ └── chart_builder.py
│ │ ├── agents/
│ │ │ ├── orchestrator.py
│ │ │ ├── data_agent.py
│ │ │ ├── eda_agent.py
│ │ │ ├── viz_agent.py
│ │ │ ├── insight_agent.py
│ │ │ └── chat_agent.py
│ ├── main.py
│
├── frontend/
│ ├── dashboard/
│ ├── chat_ui/
│
├── llm/
│ ├── prompts/
│ │ ├── orchestrator.txt
│ │ ├── data_agent.txt
│ │ ├── eda_agent.txt
│ │ ├── viz_agent.txt
│ │ └── insight_agent.txt
│
├── data/
│ ├── raw/
│ ├── processed/
│
├── docker/
├── requirements.txt
└── README.md

```
---

## ⚡ Phase A Step-by-Step Execution Plan (1 Week)

| Day | Tasks |
|-----|-------|
| **Day 1** | Repo setup, install Mistral 7B, setup Supabase, FastAPI boilerplate |
| **Day 2** | CSV upload API, store full dataset in Supabase, test read/write |
| **Day 3** | Implement Data Agent: preprocessing pipeline (missing values, normalization) |
| **Day 4** | Implement EDA Agent: compute summary stats, correlations, anomalies |
| **Day 5** | Implement Visualization Agent: chart config generation, Streamlit dashboard setup |
| **Day 6** | Orchestrator agent + Chat Agent: route tasks, handle queries, answer questions |
| **Day 7** | Testing, debugging, end-to-end workflow demo, README polish |

---

## 📌 Key Notes for Team

1. **Single LLM = one brain** → roles handled via prompt engineering  
2. **Backend executes actual data ops** → LLM only decides what to do  
3. **Store full datasets in Supabase** → raw + processed + insights  
4. **Dashboard is fully clickable + filterable** → Plotly + Streamlit  
5. **Phase A MVP** is commercial-grade but simplified → later can scale with multiple LLMs, Kafka streaming, additional modules  

---

## 📝 Future Extensions (Beyond Phase A)

- Real-time streaming datasets (IoT / sensor data)  
- Cybersecurity anomaly detection module  
- Multi-agent system with separate LLMs  
- Advanced dashboards (React + Plotly.js)  
- Cloud deployment (Docker + Kubernetes + Supabase / S3)  
- User authentication and role management  

---

## 🔗 Demo / References

- Mistral 7B: [https://huggingface.co/mistralai/Mistral-7B-Instruct](https://huggingface.co/mistralai/Mistral-7B-Instruct)  
- LangChain Agents: [https://www.langchain.com](https://www.langchain.com)  
- Supabase Docs: [https://supabase.com/docs](https://supabase.com/docs)  
- Streamlit Docs: [https://docs.streamlit.io](https://docs.streamlit.io)  
- Plotly Docs: [https://plotly.com/python/](https://plotly.com/python/)  

---

**Phase A**: This README and repo layout covers **all aspects** to get your team coding immediately.  

---

If you want, I can also **draw a clear visual architecture diagram** with **user → DB → SLM → dashboard → chat** for the README, which will make it very easy to explain to your team and supervisors.  

Do you want me to make that diagram next?