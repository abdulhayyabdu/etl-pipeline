#  ETL Pipeline

## Overview

This project implements an ETL (Extract, Transform, Load) pipeline that ingests data from CSV and JSON files, performs data cleaning and transformation, and loads the processed data into a MySQL database.

The pipeline is designed to be modular, reusable, and easily extendable to support additional data sources and storage systems.

The entire solution is containerized using Docker to ensure reproducibility and ease of execution.

---

## Features

- Ingest data from CSV and JSON files
- Data cleaning and transformation
- JSON normalization into relational tables
- Personally Identifiable Information (PII) masking
- Modular ETL pipeline design
- Logging support
- Unit testing
- Dockerized environment for easy execution

---
## Project Architecture
```
Raw Data (CSV / JSON)
│
▼
Extract Layer
│
▼
Transform Layer
(cleaning, formatting, masking)
│
▼
Load Layer
│
▼
MySQL Database
```
---

## Project Structure
malysia_task_data/
│
├── data/
│ ├── test.csv
│ └── test.json
│
├── etl/
│ ├── extract.py
│ ├── transform.py
│ └── load.py
│
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md

---

## Data Processing

### CSV File

The CSV file is ingested and loaded into the **test** table.

Data transformations include:

- Convert `created_at` and `last_login` to timestamp
- Convert `is_claimed` to boolean
- Convert `paid_amount` to numeric with two decimal precision
- Mask sensitive address information

---

### JSON File

The JSON file is normalized into three relational tables:

- **users**
- **telephone_numbers**
- **jobs_history**

Relationships are maintained using foreign keys.

Data transformations include:

- Convert timestamps
- Convert date fields (`dob`, `start`, `end`)
- Normalize nested arrays
- Mask sensitive data where applicable

---

## Database Tables

### test

| Column | Type |
|------|------|
| id | integer |
| name | string |
| address | string |
| created_at | timestamp |
| last_login | timestamp |
| is_claimed | boolean |
| paid_amount | decimal |

---

### users

| Column | Type |
|------|------|
| user_id | integer |
| name | string |
| dob | date |
| username | string |
| created_at | timestamp |
| updated_at | timestamp |
| logged_at | timestamp |

---

### telephone_numbers

| Column | Type |
|------|------|
| id | integer |
| user_id | foreign key |
| phone | string |

---

### jobs_history

| Column | Type |
|------|------|
| job_id | integer |
| user_id | foreign key |
| occupation | string |
| start | date |
| end | date |

---

## Technologies Used

- Python
- Pandas
- MySQL
- SQLAlchemy
- Docker
- PyTest

---

## Setup Instructions

### 1 Install Docker

Install Docker Desktop.

### 2 Clone the repository
git clone <https://github.com/abdulhayyabdu/etl-pipeline.git>

### 3 Run the ETL pipeline
docker-compose up --build

This will start:

- MySQL database container
- ETL pipeline container

The pipeline will automatically process the data and load it into the database.

---

## Verify Data

Connect to MySQL and run:
USE etl_db;

SHOW TABLES;

SELECT * FROM test LIMIT 10;

---

## Data Files
Place `test.csv` and `test.json` in the `data/` folder before running.
These files are excluded from the repo due to size (461MB, 60MB).
"# etl-pipeline" 
