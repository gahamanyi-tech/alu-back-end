#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) < 2:
        sys.exit(1)

    try:
        employee_id = int(sys.argv[1])
    except ValueError:
        sys.exit(1)

    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        sys.exit(1)
    employee_name = user_response.json().get("name")

    # Fetch todos for the user
    todos_response = requests.get(f"{base_url}/todos", params={"userId": employee_id})
    if todos_response.status_code != 200:
        sys.exit(1)
    todos = todos_response.json()

    total_tasks = len(todos)
    completed_tasks = [todo for todo in todos if todo.get("completed")]
    number_of_done_tasks = len(completed_tasks)

    # Display progress
    print(f"Employee {employee_name} is done with tasks({number_of_done_tasks}/{total_tasks}):")

    # Display titles of completed tasks with 1 tabulation and 1 space
    for task in completed_tasks:
        print(f"\t {task.get('title')}")
