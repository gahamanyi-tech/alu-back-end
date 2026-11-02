# API Data Gathering

This directory contains Python scripts for interacting with REST APIs to fetch and process data.

## Tasks

### 0. Gather data from an API
`0-gather_data_from_an_API.py` is a Python script that uses the JSONPlaceholder REST API to fetch information about a given employee's TODO list progress.

#### Requirements
- Python 3.x
- `requests` library (`pip install requests`)

#### Usage
Pass an integer representing the employee ID as a command-line parameter:

```bash
python3 0-gather_data_from_an_API.py <employee_id>
