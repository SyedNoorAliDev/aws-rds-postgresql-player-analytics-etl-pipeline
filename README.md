# IPL Player Analytics ETL Pipeline

A production-style ETL (Extract, Transform, Load) pipeline built with **Python**, **Pandas**, **SQLAlchemy**, and **AWS RDS PostgreSQL** to transform raw IPL match data into analytics-ready datasets for downstream reporting and analysis.

---

## Overview

This project demonstrates how to build a modular ETL pipeline by extracting raw cricket match data from an AWS RDS PostgreSQL database, engineering player performance metrics, calculating fantasy scores, and loading the curated results into a dedicated **analytics** schema.

The project follows software engineering best practices by separating the ETL workflow into independent modules, managing configuration securely through environment variables, and organizing the repository for maintainability and scalability.

---

## Tech Stack

- Python
- Pandas
- PostgreSQL
- SQLAlchemy
- AWS RDS
- psycopg2
- python-dotenv
- Logging

---

## Project Architecture

```
                    AWS RDS PostgreSQL
                           │
          ┌────────────────┼────────────────┐
          │                │                │
     deliveries         player      player_captain
                           │
                           ▼
                     Extract Module
                     (extract.py)
                           │
                           ▼
                  Transformation Module
                    (transform.py)

              • Merge datasets
              • Aggregate batting statistics
              • Feature engineering
              • Strike Rate calculation
              • Fantasy Score calculation

                           │
                           ▼
                      Load Module
                       (load.py)
                           │
                           ▼
      analytics.player_match_stats
```

---

## ETL Workflow

### 1. Extract

Raw data is extracted from multiple PostgreSQL tables hosted on AWS RDS.

Source tables:

- deliveries
- player
- player_captain

---

### 2. Transform

The transformation stage performs:

- Dataset joins
- Data cleaning
- Missing value handling
- Grouping and aggregation
- Feature engineering
- Fantasy score calculation

The following analytics features are generated:

- Runs
- Balls Faced
- Number of Fours
- Number of Sixes
- Strike Rate
- Captain Status
- Fantasy Score

---

### 3. Load

The transformed dataset is loaded into a dedicated analytics schema.

Destination:

```
analytics.player_match_stats
```

This table is optimized for downstream SQL analytics and reporting.

---

## Project Structure

```
ipl-player-analytics-etl/

├── src/
│   ├── config.py
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── sql/
│   ├── create_schema.sql
│   ├── create_tables.sql
│   └── sample_queries.sql
│
├── notebooks/
│   └── etl_exploration.ipynb
│
├── logs/
│   └── .gitkeep
│
├── screenshots/
│
├── .env.example
├── .gitignore
├── requirements.txt
└── README.md
```

---

## Running the Pipeline

### 1. Clone the repository

```bash
git clone https://github.com/<your-username>/ipl-player-analytics-etl.git
```

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure environment variables

Create a `.env` file using `.env.example`.

```
DB_HOST=
DB_NAME=
DB_USER=
DB_PASSWORD=
DB_PORT=5432
```

### 4. Execute the ETL Pipeline

```bash
python src/main.py
```

---

## Example Output

The pipeline creates an analytics-ready table with the following columns:

| Column |
|---------|
| match_id |
| batter |
| runs |
| balls |
| fours |
| sixes |
| strike_rate |
| is_captain |
| score |

---

## Logging

The ETL workflow includes structured logging for monitoring pipeline execution.

Example:

```
INFO Starting ETL pipeline...
INFO Extraction completed.
INFO Transformation completed.
INFO Loaded 16515 rows into analytics.player_match_stats.
INFO ETL pipeline completed successfully.
```

---

## Key Technologies Used

- ETL Pipeline Development
- Data Extraction from AWS RDS
- SQLAlchemy Database Connectivity
- Pandas Data Transformation
- Feature Engineering
- PostgreSQL Analytics Schema Design
- Environment Variable Management
- Modular Python Project Structure
- Logging
- Git & GitHub

---

## Future Improvements

Potential enhancements include:

- Incremental ETL loading
- Unit testing with pytest
- Docker containerization
- Airflow orchestration
- CI/CD using GitHub Actions
- Data quality validation
- Automated scheduling

---

## Author

**Syed Noor**

GitHub: https://github.com/SyedNoorAliDev

LinkedIn: https://www/linkedin.com/in/syed-noor-ali/

---

## License

This project is licensed under the MIT License.
