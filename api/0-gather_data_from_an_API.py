#!/usr/bin/python3
"""Return information about an employee's TODO list progress."""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    employee_id = sys.argv[1]

    user = requests.get(
        "{}/users/{}".format(url, employee_id)).json()
    todos = requests.get(
        "{}/todos".format(url),
        params={"userId": employee_id}).json()

    done = [t.get("title") for t in todos if t.get("completed")]

    print("Employee {} is done with tasks({}/{}):".format(
        user.get("name"), len(done), len(todos)))
    for title in done:
        print("\t {}".format(title))
