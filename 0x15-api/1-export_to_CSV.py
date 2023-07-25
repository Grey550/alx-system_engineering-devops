#!/usr/bin/python3
"""Export data into CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)
    username = requests.get(user_endpoint).json().get("username")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [[user_id, username, task.get("completed"),
                  task.get("title")] for task in tasks
                  if user_id == task.get("userId")
                  ]

    """Save in Json file"""

    with open("{}.csv".format(user_id), 'w', newline='') as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)

        for row in user_tasks:
            writer.writerow(row)
