#!/usr/bin/python3
"""Export data into CSV format"""
import csv
import requests
import sys


if __name__ == "__main__":
    user_id = sys.argv[1]
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get("{}users/{}".format(url, user_id)).json()
    tasks = requests.get("{}users/{}/todos".format(url, user_id)).json()
    user_tasks = [
        [sys.argv[1], user.get("username"), task.get("completed"),
            task.get("title")] for task in tasks
    ]

    # open a new CSV file in write mode
    with open("{}.csv".format(sys.argv[1]), "w", newline="") as file:
        writer = csv.writer(file, quoting=csv.QUOTE_ALL)
        for data in user_tasks:
            writer.writerow(user_tasks)
