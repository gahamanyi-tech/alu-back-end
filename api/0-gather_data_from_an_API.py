#!/usr/bin/python3
"""
A script that returns information about an employee's TODO list progress
using a REST API, given an employee ID as an integer parameter.
"""

import sys
import requests


if __name__ == "__main__":
    if len(sys.argv) > 1:
        user_id = sys.argv[1]
        user_url = f"https://jsonplaceholder.typicode.com/users/{user_id}"
        todos_url = f"https://jsonplaceholder.typicode.com/todos?userId={user_id}"

        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()

        employee_name = user_res.get("name")
        total_tasks = len(todos_res)
        
        completed_tasks = [t for t in todos_res if t.get("completed") is True]
        number_of_done = len(completed_tasks)

        print(
            f"Employee {employee_name} is done with tasks("
            f"{number_of_done}/{total_tasks}):"
        )

        for task in completed_tasks:
            print(f"\t {task.get('title')}")
