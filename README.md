# AI 620 – Data Engineering for AI Systems
## Assignment 1: Modern ELT Pipeline for Electric Vehicle Analysis

### Thematic Domain
Smart Mobility (Electric Vehicles & Infrastructure)

---

## Project Overview

This project implements a modular ELT (Extract, Load, Transform) pipeline designed to analyse global Electric Vehicle (EV) adoption trends. The pipeline integrates multiple heterogeneous data sources including market data, public discussions, and search trends to provide a comprehensive analytical dataset.

---

## Data Sources

### Structured Data
- Kaggle EV sales dataset
- Stored in CSV format

### Semi-Structured Data
- Google Trends data
- Reddit API metadata
- Stored in JSON format

### Unstructured Data
- Reddit post text (selftext)

---

## Project Structure

```
assignment_1/
├── data/
│   ├── raw/
│   ├── processed/
│   └── cleaned/
├── src/
│   ├── extract_reddit.py
│   ├── extract_kaggle.py
│   ├── extract_trends.py
│   └── transform.py
├── run_pipeline.py
├── .env
├── requirements.txt
└── README.md
```

---

## Setup Instructions

### Prerequisites
- Python 3.9+
- Reddit Developer Account
- Kaggle Account

### Create Virtual Environment

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

---

## Configure Credentials

Create a `.env` file:

```
REDDIT_CLIENT_ID=your_client_id
REDDIT_CLIENT_SECRET=your_client_secret
```

[Optional]: Place `kaggle.json` in (if required):

```
~/.kaggle/
```

---

## Running the Pipeline

### Step 1 — Extraction & Loading

```bash
python run_pipeline.py
```

### Step 2 — Transformation

```bash
python src/transform.py
```

Outputs are stored in:

```
data/cleaned/
```

---

## Storage Design

- CSV for structured analysis and BI compatibility
- JSON for semi-structured data and AI pipelines

---

## Key Findings

- EV search interest increased significantly after 2021.
- Charging infrastructure demand correlates with EV adoption.
- China and Europe lead global EV sales.

---

## Author

[Your Name]
AI 620 – Data Engineering for AI Systems
