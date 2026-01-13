# 🚀 Tower Pulse
### Real-Time & Batch Data Platform for Telecom Tower Operations

**Tower Pulse** is an end-to-end **Data Engineering graduation project** developed as part of the 🎓 **ITI – Data Engineering Track**.

It delivers a **scalable, analytics-ready data platform** that integrates **batch processing** and **real-time streaming** to monitor, analyze, and visualize telecom **cell tower performance and maintenance operations**.

---

## 🌟 Key Features

- Batch + real-time data processing  
- Star Schema data warehouse  
- Medallion architecture (**Bronze / Silver / Gold**)  
- Real-time monitoring & alerting  
- Production-style data engineering stack  

---

## 🎯 Project Goals

- 📡 Monitor cell tower performance and network health  
- 🛠 Analyze maintenance impact on service quality  
- ⚠️ Detect anomalies and high-risk towers  
- 🗺 Identify geographic coverage gaps  
- 📊 Provide historical insights and real-time visibility  

---

## 🏗 Architecture Overview

### 1️⃣ Batch Layer – Historical Analytics

**Flow:**  
Python → CSV → Snowflake → dbt → Data Warehouse → Power BI

yaml
Copy code

**Responsibilities:**  
- Data ingestion & validation  
- Data cleaning and standardization  
- Dimensional modeling (Star Schema)  
- Analytics-ready datasets for BI  

---

### 2️⃣ Streaming Layer – Real-Time Monitoring

**Flow:**  
API Producer → Kafka → Spark Streaming → Cassandra → Grafana

yaml
Copy code

**Responsibilities:**  
- Real-time ingestion & processing  
- Streaming transformations & aggregations  
- Low-latency time-series storage  
- Live dashboards and alerts  

---

## 📦 Batch Layer Details

### 🔹 Data Ingestion
- Python preprocessing of telecom data  
- Exported as CSV  
- Loaded into Snowflake staging tables  

### 🔹 Data Transformation
- Implemented with **dbt**  
- Business logic transformations  
- Data quality tests  
- Model documentation & lineage  
- Modular and reusable SQL models  

### 🔹 Medallion Architecture

| Layer   | Description                  |
|--------|------------------------------|
| Bronze | Raw ingested data            |
| Silver | Cleaned & standardized data |
| Gold   | Analytics-ready Star Schema  |

---

## 📐 Data Warehouse Design

### ⭐ Fact Table
**FACT_TOWER_OPS_MAINTENANCE**  

**Grain:** Tower × Maintenance Event × Date  

**Key Metrics:**  
- Drop Rate  
- Downtime Hours  
- Quality of Experience (QoE)  
- Latency  
- Coverage Gap  
- Signal Quality  
- Anomaly Flags  

### 📊 Dimension Tables

| Dimension             | Description                                |
|----------------------|--------------------------------------------|
| DIM_TOWER             | Tower metadata & radio technology          |
| DIM_LOCATION          | Geographic attributes & location analytics |
| DIM_NETWORK           | Network operator & mobile technology       |
| DIM_DATE              | Time-based analysis                         |
| DIM_MAINTENANCE_TYPE  | Preventive, predictive & emergency maintenance |

✅ Ensures: High query performance, clean analytics, easy extensibility  

---

## ⚡ Streaming Layer Details

- **API Producer:** Simulates live telecom events  
- **Apache Kafka:** Event streaming  
- **Apache Spark Streaming:** Real-time processing  
- **Apache Cassandra:** Low-latency time-series storage  
- **Grafana:** Live dashboards & alerts  

---

## 📊 Dashboards & Analytics

### Power BI (Batch Analytics)
- Network health overview  
- Drop rate & QoE trends  
- Maintenance effectiveness analysis  
- High-risk tower identification  
- Geographic coverage insights  

### Grafana (Real-Time Monitoring)
- Live tower performance metrics  
- Tower operational status  
- Real-time anomaly detection  

---

## 🛠 Tech Stack

### 🧱 Batch & Analytics
- Python  
- Snowflake  
- dbt  
- SQL  
- Power BI  

### ⚡ Streaming
- Apache Kafka  
- Apache Spark Streaming  
- Apache Cassandra  
- Grafana  

### ⚙️ Orchestration & DevOps
- Apache Airflow  
- Docker  

---

## 📈 Key Insights & Outcomes

- Identified high-risk towers with extreme downtime events  
- Analyzed drop rate vs QoE relationships  
- Evaluated preventive vs emergency maintenance effectiveness  
- Detected geographic coverage gaps  
- Linked maintenance costs to network performance  

---

## 🎓 Learning Outcomes

- End-to-end Data Engineering pipelines  
- Batch & Streaming architectures  
- Analytics Engineering with dbt  
- Dimensional modeling (Star Schema)  
- Telecom network data analytics  
- Building production-ready data platforms  
