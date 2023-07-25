#!/usr/bin/python3
"""Script that uses REST API to return employee's information"""
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_id = int(sys.argv[1])
    user_endpoint = "{}/users/{}".format(url, user_id)
    name = requests.get(user_endpoint).json().get("name")
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = [dict for dict in tasks
                  if dict.get("userId") == user_id]
    tasks_completed = [dict for dict in user_tasks
                       if dict.get("completed") is True]
    print("Employee {} is done with tasks({}/{}):"
          .format(name, len(tasks_completed), len(user_tasks)))

    for task in tasks_completed:
        print("\t {}".format(task.get("title")))
