#!/usr/bin/python3
"""
A script that fetches and displays an employee's TODO list progress
from the JSONPlaceholder REST API using their employee ID.
"""

import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 0-gather_data_from_an_API.py <employee_id>")
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    # API endpoints
    user_url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"

    # Fetch data
    user_response = requests.get(user_url).json()
    todos_response = requests.get(todos_url).json()

    employee_name = user_response.get("name")
    total_tasks = len(todos_response)
    
    # Filter completed tasks
    done_tasks = [task for task in todos_response if task.get("completed")]
    number_of_done_tasks = len(done_tasks)

    # Display progress header
    print(
        f"Employee {employee_name} is done with tasks("
        f"{number_of_done_tasks}/{total_tasks}):"
    )

    # Display titles of completed tasks
    for task in done_tasks:
        print(f"\t {task.get('title')}")
