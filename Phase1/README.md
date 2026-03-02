# Backend Module: Industrial Energy & Cyber Intelligence

Welcome to **Backend Module** of our Industrial Energy & Cyber Intelligence Platform! This module is focused on **Backend Development** for anomaly detection, root cause analysis, and chatbot integration using **FastAPI** and **Docker**.

---

## 🚀 Overview
This backend module implements a scalable, **Onion Architecture** for real-time monitoring of:

- ⚡ **Energy Anomalies** (using Steel Industry Energy Dataset)
- 🏭 **Machine / Sensor Anomalies** (Industrial IoT Fault Dataset)
- 🔐 **Cyber Anomalies** (SWaT ICS Dataset)

It supports **parallel development** for multiple team members, integrates trained models, and exposes **API endpoints** for frontend and chatbot consumption.

---

## 📂 Directory Structure
```
backend/
│
├─ domain/          # Core business logic & entities
│   ├─ energy.py
│   ├─ machine.py
│   └─ cyber.py
│
├─ services/        # Application layer for orchestrating logic
│   ├─ energy_service.py
│   ├─ machine_service.py
│   └─ cyber_service.py
│
├─ infrastructure/  # FastAPI endpoints + Docker setup
│   ├─ main.py
│   ├─ routes/
│   └─ models_loader.py
│
├─ docker/
│   ├─ Dockerfile_energy
│   ├─ Dockerfile_cyber
│   └─ docker-compose.yml
│
├─ models/          # Trained ML models
├─ datasets/        # CSV datasets
└─ requirements.txt
```

---

## 🛠️ Features

### Energy & Machine Module (Member 1)
- Load & preprocess Steel Industry Energy Dataset and Industrial IoT Fault Dataset
- Train LSTM / Autoencoder models for anomaly detection
- Expose API endpoints: `/anomalies/energy` & `/anomalies/machine`
- Compute **root cause scores** and provide structured JSON responses

### Cyber & Chatbot Module (Member 2)
- Load & preprocess SWaT dataset
- Train LSTM / GRU / VAE models for cyber anomaly detection
- Expose API endpoints: `/anomalies/cyber` & `/chatbot/query`
- Aggregate anomalies from energy & machine modules for unified response

### Integration & Deployment
- Each module runs in a **Docker container**
- `docker-compose.yml` manages multi-container orchestration
- Frontend interacts seamlessly via REST APIs

---

## 🏗️ Technology Stack
- **Backend Framework:** FastAPI
- **Modeling:** PyTorch / TensorFlow
- **Docker:** Containerized services
- **Datasets:**
  - Steel Industry Energy Dataset
  - Industrial IoT Fault Detection Dataset
  - SWaT ICS Dataset
- **Frontend Integration:** API endpoints exposed for chatbot/dashboard

---

## ⚡ How to Run
1. Clone the repository
2. Navigate to `backend/docker`
3. Build and run containers:
```bash
docker-compose up --build
```
4. Access API endpoints:
```
GET /anomalies/energy
GET /anomalies/machine
GET /anomalies/cyber
POST /chatbot/query
```

---

## 📌 Notes & Guidelines
- Ensure all datasets are placed in `/datasets`
- Trained models should be in `/models`
- Follow the **Onion Architecture principles** for adding new services or logic
- Use shared **JSON schema** for consistent responses across modules

---

## 🎯 Goals for Backend Module
1. Real-time anomaly detection for energy, machine, and cyber modules
2. Root cause analysis integrated into API responses
3. Chatbot query system that aggregates anomalies
4. Fully containerized backend ready for frontend integration

---

## 💡 Contributors
- **Member 1:** Energy & Machine anomaly module
- **Member 2:** Cyber anomaly & Chatbot module
- **Member 3:** Frontend dashboard integration

---

## 📚 References
1. Steel Industry Energy Dataset - [Kaggle](https://www.kaggle.com/datasets/csafrit2/steel-industry-energy-consumption) | [UCI Mirror](https://archive.ics.uci.edu/dataset/851/steel%2B)
2. Industrial IoT Fault Detection Dataset - [Kaggle](https://www.kaggle.com/datasets/ziya07/industrial-iot-fault-detection-dataset/data?utm_source=chatgpt.com)
3. SWaT ICS Dataset - [Kaggle](https://www.kaggle.com/datasets/vishala28/swat-dataset-se