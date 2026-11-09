#!/usr/bin/python3
"""
Script that fetches and displays an employee's TODO list progress
from the JSONPlaceholder REST API given their employee ID.
"""
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user_id = sys.argv[1]

    user = requests.get(url + "users/{}".format(user_id)).json()
    todos = requests.get(url + "todos", params={"userId": user_id}).json()

    completed = [task.get("title") for task in todos if task.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(completed), len(todos)))

    for title in completed:
        print("\t {}".format(title))
