#!/usr/bin/python3
"""
Python script that exports data in JSON format for a given user ID
using the JSONPlaceholder API.
"""

import json
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    user_id = sys.argv[1]

    user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
    todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

    user_response = requests.get(user_url)
    if user_response.status_code != 200:
        sys.exit(1)
    user_data = user_response.json()
    username = user_data.get("username")

    todos_response = requests.get(todos_url)
    if todos_response.status_code != 200:
        sys.exit(1)
    todos_data = todos_response.json()

    tasks_list = []
    for todo in todos_data:
        task_dict = {
            "task": todo.get("title"),
            "completed": todo.get("completed"),
            "username": username,
        }
        tasks_list.append(task_dict)

    export_data = {user_id: tasks_list}

    filename = f"{user_id}.json"
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(export_data, f)
