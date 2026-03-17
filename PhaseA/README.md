<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:0f2027,50:203a43,100:2c5364&height=220&section=header&text=IntelliViz&fontSize=50&fontColor=ffffff&animation=fadeIn&fontAlignY=35"/>
</p>

<p align="center">
  <b>AI-Powered Agentic Data Analysis Platform</b><br>
  Conversational analytics that thinks like a data analyst.
</p>

<p align="center">
  <img src="https://img.shields.io/badge/Architecture-Onion-blueviolet?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Backend-FastAPI-009688?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Frontend-Streamlit-FF4B4B?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/AI-LLM--Orchestrated-black?style=for-the-badge"/>
  <img src="https://img.shields.io/badge/Data-Pandas-yellow?style=for-the-badge"/>
</p>

---

## 🚀 Project Overview

**IntelliViz** is an AI-driven, agentic data analytics platform designed to transform raw CSV datasets into meaningful insights through a single orchestrating Large Language Model (LLM).

Users interact with IntelliViz conversationally — asking questions, requesting visualizations, and receiving intelligent insights — just like working with a professional data analyst.

The system autonomously performs:
- Data Cleaning
- Exploratory Data Analysis (EDA)
- Statistical Reasoning
- Visualization Generation
- Insight Extraction

---

## 🧠 Onion Architecture

IntelliViz strictly follows **Onion Architecture**, ensuring separation of concerns, testability, and scalability.
            ┌──────────────────────────┐
            │      Presentation        │
            │   (FastAPI / Schemas)   │
            └──────────▲──────────────┘
                       │
            ┌──────────┴──────────────┐
            │       Application       │
            │ (Agents / Workflows)    │
            └──────────▲──────────────┘
                       │
            ┌──────────┴──────────────┐
            │        Domain           │
            │ (Entities / Logic)      │
            └──────────▲──────────────┘
                       │
            ┌──────────┴──────────────┐
            │     Infrastructure      │
            │ (LLM / Pandas / DB)     │
            └─────────────────────────┘

            
### Layer Responsibilities

| Layer | Description |
|------|-------------|
| **Domain** | Core business logic, statistical rules, insight generation |
| **Application** | Agent orchestration, workflows, use-case services |
| **Infrastructure** | External integrations (LLM, Pandas, Matplotlib, storage) |
| **Presentation** | API endpoints and request/response schemas |
| **Frontend** | Streamlit-based interactive dashboard |

---

## 🤖 Agentic Workflow
```bash
---
User Query
│
▼
LLM Orchestrator Agent
│
├──► Data Cleaning Agent
│
├──► EDA Agent
│
├──► Visualization Agent
│
├──► Insight Generation Agent
│
▼
Response Composer
│
▼
User Output (Charts + Insights + Answers)

```
---
---

## 🧩 Agent Responsibilities

| Agent | Responsibility |
|------|----------------|
| **Orchestrator Agent** | Understands user intent and routes tasks |
| **Data Cleaning Agent** | Handles missing values, formatting, normalization |
| **EDA Agent** | Performs statistical summaries and distributions |
| **Visualization Agent** | Generates charts (bar, line, heatmap, etc.) |
| **Insight Agent** | Extracts actionable insights and trends |
| **Response Agent** | Converts results into human-like explanations |

---

## 🛠 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10+-blue?style=flat-square"/>
  <img src="https://img.shields.io/badge/FastAPI-Backend-009688?style=flat-square"/>
  <img src="https://img.shields.io/badge/Streamlit-Frontend-FF4B4B?style=flat-square"/>
  <img src="https://img.shields.io/badge/Pandas-Data-yellow?style=flat-square"/>
  <img src="https://img.shields.io/badge/Matplotlib-Visualization-orange?style=flat-square"/>
  <img src="https://img.shields.io/badge/LLM-OpenAI/GPT-black?style=flat-square"/>
</p>

---

## 📁 Repository Structure
```bash 
IntelliViz/
│
├── domain/
│ ├── entities/
│ ├── rules/
│ └── insights/
│
├── application/
│ ├── agents/
│ ├── services/
│ └── workflows/
│
├── infrastructure/
│ ├── llm/
│ ├── data_processing/
│ ├── visualization/
│ └── repositories/
│
├── presentation/
│ ├── api/
│ ├── routes/
│ └── schemas/
│
├── frontend/
│ └── streamlit_app.py
│
├── tests/
├── requirements.txt
└── README.md
```

---

## 🗺 Development Roadmap (1-Week Sprint)
```bash
| Day | Goal |
|----|------|
| Day 1 | Project setup + Onion structure |
| Day 2 | Domain layer (entities + rules) |
| Day 3 | Infrastructure (Pandas + LLM integration) |
| Day 4 | Application layer (agent orchestration) |
| Day 5 | FastAPI endpoints |
| Day 6 | Streamlit dashboard |
| Day 7 | Testing + polishing + deployment |
```
---

## 💬 Example User Queries

- "Show sales trends over time"
- "Find correlations between price and demand"
- "Which region performed best last quarter?"
- "Clean this dataset and summarize key insights"
- "Generate a heatmap of feature relationships"
- "What anomalies exist in this data?"

---

## ⚙️ Running Instructions

### 1. Clone Repository
```bash
git clone https://github.com/yourusername/IntelliViz.git
cd IntelliViz
2. Install Dependencies
pip install -r requirements.txt
3. Run Backend
uvicorn presentation.api.main:app --reload
4. Run Frontend
streamlit run frontend/streamlit_app.py
```
🌍 Project Vision

IntelliViz aims to redefine how humans interact with data.

Instead of dashboards requiring manual interpretation, IntelliViz enables:

Natural language interaction

Autonomous analytical reasoning

Real-time intelligent insights

The long-term vision is to evolve IntelliViz into a fully autonomous AI data analyst, capable of:

Decision support

Predictive analytics

Business intelligence automation

<p align="center"> <img src="https://capsule-render.vercel.app/api?type=waving&color=0:2c5364,50:203a43,100:0f2027&height=120&section=footer"/> </p> 
