<!-- ================== INTELLIVIZ — PHASE A ================== -->

<!-- HERO HEADER -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=220&section=header&text=IntelliViz%20Phase%20A&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&color=FF69B4"
    width="100%"
  />
</p>

<!-- TYPING TAGLINE -->
<div align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=22&duration=3000&pause=900&color=FF69B4&center=true&vCenter=true&width=900&lines=Agentic+Data+Analysis+Platform;Single+LLM+Commercial+MVP;Upload+CSV+→+Insights+→+Dashboard+→+Chat"
    alt="Typing animation"
  />
</div>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Phase-A-FF69B4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Single%20Brain-FF77A9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Active%20Development-FFA6C9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/License-MIT-FFD6E5?style=for-the-badge" />
</p>

<!-- DIVIDER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=FF69B4" width="100%" />
</p>

## 🚀 What is IntelliViz?

**IntelliViz (Phase A)** is a **commercial-ready MVP** for automated data analysis and visualization.

Upload a CSV and IntelliViz behaves like a **team of analysts**, powered by **one LLM**:

- 🧹 Automatic preprocessing  
- 📊 Exploratory Data Analysis (EDA)  
- 📈 Interactive visualizations  
- 💡 Human-readable insights  
- 💬 Chat interface to explore results  

<p align="center">✨ <i>LLM decides. Backend executes. Dashboard explains.</i> ✨</p>

---

## 🧠 Architecture Overview

CSV Upload
↓
Supabase (Full Dataset Storage)
↓
Orchestrator (Single LLM)
↓
┌──────────┬──────────┬────────────┬────────────┐
│ Data │ EDA │ Viz │ Insight │
│ Agent │ Agent │ Agent │ Agent │
└──────────┴──────────┴────────────┴────────────┘
↓
Backend (Pandas / Plotly)
↓
Streamlit Dashboard + Chat


---

## 🧠 Agentic Design (Single LLM)

| Agent | Responsibility |
|-----|----------------|
| 🧭 Orchestrator | Understands intent & routes tasks |
| 🧹 Data Agent | Decides preprocessing steps |
| 📊 EDA Agent | Chooses statistics & correlations |
| 📈 Viz Agent | Recommends chart types |
| 💡 Insight Agent | Converts numbers into insights |
| 💬 Chat Agent | Answers questions from stored outputs |

> ⚠️ The LLM **never touches raw data** — only schema, samples, and statistics.

---

## 🧰 Tech Stack

<p align="center">
  <img src="https://img.shields.io/badge/Mistral%207B-FF5C8A?style=for-the-badge" />
  <img src="https://img.shields.io/badge/FastAPI-FF77A9?style=for-the-badge&logo=fastapi&logoColor=white" />
  <img src="https://img.shields.io/badge/LangChain-FFA6C9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Supabase-FFD6E5?style=for-the-badge&logo=supabase&logoColor=white" />
  <img src="https://img.shields.io/badge/Streamlit-FF9DBD?style=for-the-badge&logo=streamlit&logoColor=white" />
  <img src="https://img.shields.io/badge/Plotly-FFB7D1?style=for-the-badge" />
</p>

---

## 📁 Repository Structure



intelliviz-core/
│
├── backend/
│ ├── app/
│ │ ├── api/ # Upload, query, chat endpoints
│ │ ├── agents/ # Orchestrator + agent roles
│ │ ├── preprocessing/ # Data cleaning logic
│ │ ├── eda/ # Statistics & correlations
│ │ ├── visualization/ # Plotly chart builders
│ │ ├── core/ # Config & DB
│ │ └── main.py
│
├── frontend/
│ └── streamlit_app.py
│
├── llm/
│ └── prompts/ # Prompt templates per agent
│
├── docker/
├── requirements.txt
└── README.md


---

## 🧪 Demo Workflow

1. Upload a CSV file  
2. Click **Analyze Dataset**  
3. Explore interactive charts & filters  
4. Ask questions in chat:
   - “What trends stand out?”
   - “Any anomalies?”
   - “Which features matter most?”

---

## 🗓️ Phase A — 1 Week Plan

| Day | Output |
|---|---|
| 1 | Infra + DB + LLM setup |
| 2 | CSV upload & storage |
| 3 | Preprocessing agent |
| 4 | EDA + insight agent |
| 5 | Visualization & dashboard |
| 6 | Orchestrator + chat |
| 7 | Polish & demo |

---

## 🔮 Phase B (Next)

- Multi-dataset joins  
- Saved dashboards  
- Vector search over insights  
- Multi-LLM routing  
- Scheduled re-analysis  

---

<p align="center">💗 Built for speed. Designed for clarity. Ready for production.</p>

<!-- FOOTER -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=140&section=footer&color=FF69B4"
    width="100%"
  />
</p>
