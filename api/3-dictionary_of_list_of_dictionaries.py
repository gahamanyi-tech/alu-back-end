#!/usr/bin/python3
"""
Python script that exports tasks of all employees in JSON format
using the JSONPlaceholder API.
"""

import json
import requests
import sys

if __name__ == "__main__":
    # Fetch all users and todos from the API
    users_url = "https://jsonplaceholder.typicode.com/users"
    todos_url = "https://jsonplaceholder.typicode.com/todos"

    users_response = requests.get(users_url)
    todos_response = requests.get(todos_url)

    if users_response.status_code != 200 or todos_response.status_code != 200:
        sys.exit(1)

    users = users_response.json()
    todos = todos_response.json()

    # Map user IDs to their usernames
    user_dict = {user["id"]: user["username"] for user in users}

    # Build the dictionary mapping user ID to their list of tasks
    all_employees_tasks = {}

    for user in users:
        user_id = str(user["id"])
        username = user["username"]
        all_employees_tasks[user_id] = []

    for todo in todos:
        user_id = str(todo["userId"])
        username = user_dict.get(int(user_id))
        
        task_info = {
            "username": username,
            "task": todo["title"],
            "completed": todo["completed"]
        }
        
        if user_id in all_employees_tasks:
            all_employees_tasks[user_id].append(task_info)

    # Export data to todo_all_employees.json
    filename = "todo_all_employees.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(all_employees_tasks, f)
