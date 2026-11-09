#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
from the JSONPlaceholder REST API given their employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) > 1:
        try:
            user_id = int(sys.argv[1])
        except ValueError:
            sys.exit(1)

        user_url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        todos_url = "https://jsonplaceholder.typicode.com/todos?userId={}".format(user_id)

        user_res = requests.get(user_url).json()
        todos_res = requests.get(todos_url).json()

        employee_name = user_res.get("name")
        total_tasks = len(todos_res)
        
        completed_tasks = [task.get("title") for task in todos_res if task.get("completed")]
        number_of_done = len(completed_tasks)

        print("Employee {} is done with tasks({}/{}):".format(
            employee_name, number_of_done, total_tasks))

        for title in completed_tasks:
            print("\t {}".format(title))
