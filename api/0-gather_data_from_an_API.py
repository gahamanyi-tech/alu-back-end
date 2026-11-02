#!/usr/bin/python3
"""
A Python script that uses a REST API for a given employee ID
and returns information about his/her TODO list progress.
"""

import requests
import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        emp_id = sys.argv[1]
        url_user = f"https://jsonplaceholder.typicode.com/users/{emp_id}"
        url_todos = f"https://jsonplaceholder.typicode.com/todos?userId={emp_id}"

        res_user = requests.get(url_user).json()
        res_todos = requests.get(url_todos).json()

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
