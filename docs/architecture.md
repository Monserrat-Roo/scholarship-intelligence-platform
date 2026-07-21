# Scholarship Intelligence Platform

## Overview
Scholarship Intelligence Platform (SIP) is a modular data engineering platform designed to collect, clean, organize and analyze international scholarship opportunities from multiple sources.

The platform centralizes scholarship information into a single database and provides intelligent search, filtering, recommendation and document generation features.

## Goals
- Collect scholarship information automatically.
- Normalize information from multiple websites.
- Avoid duplicated scholarships.
- Help users find scholarships according to their profile.
- Generate application documents.
- Track application progress.

## System Architecture
Internet
        │
        ▼
Scraper Layer
        │
        ▼
ETL Pipeline
        │
        ▼
SQLite Database
        │
        ▼
Recommendation Engine
        │
        ▼
Streamlit Dashboard

## Main Modules
### Scraper
Responsible for collecting scholarship information from websites.

### ETL
Extracts, cleans and normalizes the collected information.

### Database
Stores all scholarship information.

### Recommendation Engine
Ranks scholarships according to the user's profile.

### Dashboard
Displays information through Streamlit.

### AI
Generates CVs, motivation letters and checklists.


## Technologies
- Python
- BeautifulSoup
- SQLite
- SQLAlchemy
- Pandas
- Streamlit
- Plotly
- Git
- GitHub