<!-- ================== INTELLIVIZ — PHASE A ================== -->

<!-- HERO HEADER -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=220&section=header&text=IntelliViz%20Phase%20A&fontSize=48&fontColor=ffffff&animation=fadeIn&fontAlignY=38&color=FF69B4"
    width="100%"
  />
</p>

<!-- AGENTIC TYPING -->
<div align="center">
  <img
    src="https://readme-typing-svg.demolab.com?font=JetBrains+Mono&weight=800&size=22&duration=2500&pause=600&color=FF69B4&center=true&vCenter=true&width=950&lines=🧠+Single+LLM+Thinking...;🧭+Routing+Tasks+to+Agents...;📊+Analyzing+Data...;📈+Generating+Visuals...;💡+Extracting+Insights...;💬+Ready+to+Chat"
    alt="Agentic typing animation"
  />
</div>

<!-- BADGES -->
<p align="center">
  <img src="https://img.shields.io/badge/Phase-A-FF69B4?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Architecture-Agentic-FF77A9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/LLM-Single%20Brain-FFA6C9?style=for-the-badge" />
  <img src="https://img.shields.io/badge/Status-Building-FFD6E5?style=for-the-badge" />
</p>

<!-- DIVIDER -->
<p align="center">
  <img src="https://capsule-render.vercel.app/api?type=rect&height=2&color=FF69B4" width="100%" />
</p>

## 🚀 What is IntelliViz?

**IntelliViz (Phase A)** is an **agentic data analysis platform**.

You upload a CSV.  
A **single LLM thinks like a team**.

It decides:
- *How to clean the data*
- *What statistics matter*
- *Which charts explain the story*
- *What insights a human would care about*

<p align="center">
✨ <b>LLM reasons → Backend executes → Dashboard communicates</b> ✨
</p>

---

## 🧠 Agentic System (Visual Mental Model)

<p align="center">
  <img src="https://raw.githubusercontent.com/ashishpatel26/agentic-ai-diagrams/main/agent-routing.gif" width="80%" alt="Agent routing animation (placeholder)" />
</p>
```bash
User Intent
↓
🧠 Orchestrator (Single LLM)
↓
┌──────────┬──────────┬────────────┬────────────┐
│ 🧹 Data │ 📊 EDA │ 📈 Viz │ 💡 Insight │
│ Agent │ Agent │ Agent │ Agent │
└──────────┴──────────┴────────────┴────────────┘
↓
⚙️ Backend Execution (Pandas / Plotly)
↓
📊 Dashboard + 💬 Chat


> The LLM **never touches raw rows** — it only reasons over schema, samples, and stats.
```
---

## 🤖 Agents in Action

<div align="center">
```bash
| Agent | Animation | Responsibility |
|------|-----------|----------------|
| 🧭 Orchestrator | 🔁 Thinking | Routes tasks & intent |
| 🧹 Data Agent | 🧼 Cleaning | Missing values, scaling |
| 📊 EDA Agent | 📐 Measuring | Stats, correlations |
| 📈 Viz Agent | 🎨 Designing | Chart selection |
| 💡 Insight Agent | 💭 Explaining | Human-readable insights |
| 💬 Chat Agent | 🗣️ Conversing | Answers questions |

</div>
```
---

## 🔄 End-to-End Flow (Animated Concept)

<p align="center">
  <img src="https://media.giphy.com/media/26tn33aiTi1jkl6H6/giphy.gif" width="70%" alt="Processing animation placeholder"/>
</p>

1️⃣ Upload CSV  
2️⃣ LLM reasons about the dataset  
3️⃣ Backend executes transformations  
4️⃣ Charts & insights are generated  
5️⃣ Chat explores the results  

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
```bash
intelliviz-core/
│
├── backend/
│ ├── app/
│ │ ├── api/ # Upload, query, chat
│ │ ├── agents/ # Orchestrator + roles
│ │ ├── preprocessing/ # Data cleaning
│ │ ├── eda/ # Statistics
│ │ ├── visualization/ # Charts
│ │ └── main.py
│
├── frontend/
│ └── streamlit_app.py
│
├── llm/prompts/
├── docker/
└── README.md

```
---

## 🧪 Try It Like a User

💬 Ask things like:
- *“What stands out in this dataset?”*
- *“Are there anomalies?”*
- *“Which features matter most?”*

The system **answers like an analyst**, not a chatbot.

---

## 🗓️ Phase A — 1 Week Sprint

| Day | Focus |
|----|------|
| 1 | Infra + LLM |
| 2 | CSV upload |
| 3 | Data agent |
| 4 | EDA + insights |
| 5 | Visuals |
| 6 | Orchestrator + chat |
| 7 | Demo polish |

---

<p align="center">
💗 <b>Agentic by design. Minimal by necessity. Built to scale.</b>
</p>

<!-- FOOTER -->
<p align="center">
  <img
    src="https://capsule-render.vercel.app/api?type=waving&height=140&section=footer&color=FF69B4"
    width="100%"
  />
</p>