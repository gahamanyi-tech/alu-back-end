#!/usr/bin/python3
"""
Python script that, using a REST API, for a given employee ID,
returns information about his/her TODO list progress.
"""

import requests
import sys


if __name__ == '__main__':
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        base_url = 'https://jsonplaceholder.typicode.com'
        user_url = f"{base_url}/users/{emp_id}"
        todos_url = f"{base_url}/todos"

        res_user = requests.get(user_url).json()
        res_todos = requests.get(
            todos_url,
            params={'userId': emp_id}
        ).json()

        emp_name = res_user.get('name')
        total_tasks = len(res_todos)
        done_tasks = [t for t in res_todos if t.get('completed') is True]
        number_of_done = len(done_tasks)

        print(
            f"Employee {emp_name} is done with tasks"
            f"({number_of_done}/{total_tasks}):"
        )

        for task in done_tasks:
            print(f"\t {task.get('title')}")
