# Social Media Insights Data Platform – POC

Developer: Prophecy Nxumalo
Reviewer(s): Gerard Reisenberg, Resham Sivnarain
Type: Assessment
Version: Will be updated in future 

This project is a production-ready Proof of Concept (POC) for a scalable data platform that ingests, processes, and exposes insights from social media and batch data sources. Designed for real-time analytics and trend detection, it supports containerized deployment using `docker-compose` as per the assessment.

---

## Objectives

- Ingest both **streaming** (Twitter API) and **batch** (Financial Sanctions List) data.
- Clean and process data using **Python / PySpark**.
- Store raw and processed data in **MinIO S3 buckets from raw to cleaned**, **PostgreSQL**, and **Redshift**.
- Orchestrate tasks using **Apache Airflow**.
- Visualize insights
- Include optional support for **Kafka** and **Cassandra** for horizontal scalability.

---

## Directory or Project Structure

social-media-insights/
│
├── docker-compose.yml
├── .env
│
├── airflow/
│ └── dags/
│ └── social_media_pipeline.py
│
├── ingestion/
│ ├── batch_ingestor.py
│ └── stream_ingestor.py
│
├── processing/
│ └── clean_transform.py
│
├── storage/
│ └── init_db.sql
│
├── api/
│ ├── Dockerfile
│ └── main.py (FastAPI endpoint for insights)
│
├── data testing datasets, other stuff
└── README.md

---

## Technology Stack Used - (Not limited)

| Layer              | Technology                                 |
|-------------------|---------------------------------------------|
| Orchestration      | Apache Airflow                              
| Batch Ingestion     | PySpark/Python (API requests)                  
| Streaming Ingestion | Twitter API, Kafka    
| Processing         | Python / PySpark                            
| Storage            | MinIO, RedShift/Cassandra/ Postgress        
                         

---



### Included in `docker-compose.yml`

- `airflow-webserver` + `scheduler`: DAG execution and monitoring
- `postgres/Redshift`: Structured data store (Gold layer)
- `minio`: Object storage (raw/cleaned files) in S3 bucket
- `cassandra`
- `api`: FastAPI for exposing processed data
- `dashboard`: Streamlit frontend
- `adminer`: GUI for Postgres database

---

## running Locally

### 1. Clone the Repository from git

```bash
git clone 
cd name of the repo here


###    creeate a .env file for environment variables:

POSTGRES_USER=sgt_data_platform_airflow
POSTGRES_PASSWORD=sgt_data_platform_airflow
POSTGRES_DB=sgt_data_platform_airflow

MINIO_ROOT_USER=sgt_data_platform_minio
MINIO_ROOT_PASSWORD=sgt_data_platform_minio123

---


###  Important Note

## install packages first before running project to avoid error:
- Python
- Airflow
- kafka
- Docker
- GitHub
- and all other necessary extensions
