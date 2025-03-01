# Macrotrends Employee Data Scraper

## Description

Python script to extract the number of employees for technology companies. 

This will serve as a backend for a frontend interface aimed at visualizing historical employee data (and potentially other types of data in the future). 

Currently, the script includes a limited set of hardcoded companies, which will be expanded later.

## Requirements

- Python 3.12

## Installation

```bash
pip install -r requirements.txt
```
## Usage
1. Run the script to get data of all companies in the list
2. Results are saved in output/employee_data.json

### TODO

#### BE:
- refactor to OOP pattern (this was only a test)
- Error handling and retry mechanism for web scraping
- Caching strategy for scraped data
- Rate limiting to respect website scraping policies
- Logging performance metrics
- Containerization (Docker)
- Unit and integration tests
- log handler
- database configuration (sql alchemy - pydantic models)
- push employees data into database
- APi development (FastAPI) with security (jwt? - tbd) to retrieve data
- Scheduled data updates (e.g., using Celery)
- deploy with aws
- think about new data to be displayed/scraped

#### FE:
- UI study
- UI development