#!/usr/bin/python3
"""
Python script that exports data in the CSV format for a given employee ID.
"""

import csv
import requests
import sys

if __name__ == "__main__":
    if len(sys.argv) < 2:
        sys.exit(1)

    employee_id = sys.argv[1]
    base_url = "https://jsonplaceholder.typicode.com"

    # Fetch user details
    user_response = requests.get(f"{base_url}/users/{employee_id}")
    if user_response.status_code != 200:
        sys.exit(1)

    user_data = user_response.json()
    username = user_data.get("username")

    # Fetch todos/tasks for the user
    todos_response = requests.get(
        f"{base_url}/todos",
        params={"userId": employee_id}
    )
    todos_data = todos_response.json()

    # Define filename as USER_ID.csv
    filename = f"{employee_id}.csv"

    # Write records to CSV format matching the exact requirements
    with open(filename, mode="w", newline="", encoding="utf-8") as csv_file:
        writer = csv.writer(
            csv_file,
            quoting=csv.QUOTE_ALL,
            escapechar="\\",
            doublequote=False
        )

        for task in todos_data:
            completed_status = str(task.get("completed"))
            task_title = task.get("title")
            writer.writerow([
                employee_id,
                username,
                completed_status,
                task_title
            ])
