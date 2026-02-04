<p align="center">
  <img src="https://via.placeholder.com/800x250.png?text=IntelliViz+%F0%9F%9A%80+Data+Analytics+%26+IoT+Monitoring" alt="IntelliViz Banner"/>
</p>

# IntelliViz 🚀  
**Autonomous Data Analytics & IoT Anomaly Detection Platform**

![Python](https://img.shields.io/badge/Python-3.10+-blue) 
![PyTorch](https://img.shields.io/badge/PyTorch-✓-orange) 
![Streamlit](https://img.shields.io/badge/Streamlit-✓-red) 
![MIT License](https://img.shields.io/badge/License-MIT-green)

---

## 🌟 Project Overview
IntelliViz is an **agentic analytics platform** combining:  

1. **SLM-Based General Analytics Module** – analyze **any dataset** autonomously.  
2. **IoT Monitoring & Cybersecurity Module** – monitor sensors and networks in **real-time**.  

Users can interact via a **chatbot**, visualize insights, and receive predictive alerts without manual intervention.  

<p align="center">
  <img src="https://media.giphy.com/media/3oEjI6SIIHBdRxXI40/giphy.gif" width="700" alt="Dashboard Animation"/>
</p>

---

## 🔥 Features

### 1️⃣ SLM-Based General Data Analytics Module
- **Works on any structured dataset:** CSV, Excel, SQL, or JSON.  
- **Automated Data Preprocessing:** Missing value handling, normalization, and noise reduction.  
- **Exploratory Data Analysis (EDA):** Generates statistical summaries, correlations, trends, and charts automatically.  
- **Insight Generation:** Provides textual explanations of patterns, anomalies, and trends.  
- **Visualization & Dashboard Creation:** Interactive charts, heatmaps, and graphs with Plotly / Matplotlib.  
- **Natural Language Interaction:** Users can query data with questions like:  
  - *“Which product had the highest sales last month?”*  
  - *“Show correlations between features X and Y.”*  

### 2️⃣ IoT Monitoring & Cybersecurity Module
- **Real-Time Sensor & Network Monitoring:** Streams data from IoT devices.  
- **Anomaly Detection:** LSTM / ARIMA-based modeling for unusual patterns or attacks.  
- **Root Cause Analysis:** Pinpoints the source of anomalies (specific sensor, device, or attack).  
- **Alerts & Notifications:** Generates real-time alerts for operational or cybersecurity issues.  

---

## 🎯 Scope
- **SLM Module:** General-purpose, works across domains for autonomous data insights.  
- **IoT Module:** Specialized monitoring for smart factories, buildings, energy systems, and critical infrastructure.  
- **24/7 autonomous analytics** and anomaly detection.  
- **Interactive dashboards** for non-technical users.  

---

## 🛠 Modules & Architecture

```mermaid
graph TD
    A[Datasets (CSV, Excel, JSON, SQL)] --> B[SLM-Based Analytics Module]
    B --> C[EDA & Insights]
    B --> D[Visualization & Dashboards]

    E[IoT Devices / Network] --> F[IoT Monitoring Module]
    F --> G[Anomaly Detection]
    F --> H[Root Cause Analysis]
    G --> I[Alerts & Notifications]



## 💻 Tech Stack
- **Programming Language:** Python 3.10+  
- **Libraries:** PyTorch, TensorFlow, Pandas, NumPy, Scikit-learn, Matplotlib, Plotly  
- **Frontend / Visualization:** Streamlit / Gradio (interactive dashboards & chatbot)  
- **IDE:** VSCode / Jupyter Notebook  
- **Optional:** GPU (NVIDIA GTX 1650+) for faster LSTM training  

---

## ⚡ Advantages
- **Dual-purpose platform:** General dataset analysis + IoT anomaly detection.  
- Fully autonomous with **minimal human intervention**.  
- Provides **real-time insights** for operational and cybersecurity monitoring.  
- **Natural language chatbot interface** for easy querying.  
- **Scalable** across multiple domains and IoT environments.  

---

## ⚠️ Limitations
- Performance depends on **quality & diversity** of input datasets.  
- SLM module may require **fine-tuning** for very large datasets.  
- LSTM module may need **significant computational resources** for large IoT networks.  

---

## 🏗 Applications
- **General Analytics:** Business intelligence, finance, marketing, healthcare, or any tabular dataset.  
- **IoT & IIoT Monitoring:** Smart factories, energy plants, smart homes, and critical infrastructure.  
- **Predictive Maintenance:** Detect anomalies before failures occur.  
- **Cybersecurity Monitoring:** Real-time detection of unusual device or network behavior.  

---

## 🌱 Alignment with SDGs

| SDG Goal | Relevance |
|----------|-----------|
| **Goal 9: Industry, Innovation & Infrastructure** | Supports industrial IoT and automation. |
| **Goal 11: Sustainable Cities & Communities** | Enables smart building and city monitoring. |
| **Goal 12: Responsible Consumption & Production** | Optimizes resources, reduces waste through predictive insights. |
