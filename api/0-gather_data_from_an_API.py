#!/usr/bin/python3
"""Return information about an employee's TODO list progress
using the JSONPlaceholder REST API.

Usage: python3 0-gather_data_from_an_API.py <employee_id>
"""
import requests
import sys

BASE_URL = "https://jsonplaceholder.typicode.com"


if __name__ == "__main__":
    employee_id = int(sys.argv[1])

    # Fetch the employee
    user = requests.get("{}/users/{}".format(BASE_URL, employee_id)).json()

    # Fetch all todos belonging to that employee
    todos = requests.get(
        "{}/todos".format(BASE_URL), params={"userId": employee_id}
    ).json()

    # Keep only the completed tasks
    done_tasks = [task for task in todos if task.get("completed")]

    # First line: progress summary
    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done_tasks), len(todos)))

    # Following lines: one tab + one space + title
    for task in done_tasks:
        print("\t {}".format(task.get("title")))
