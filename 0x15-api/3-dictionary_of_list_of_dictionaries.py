#!/usr/bin/python3
"""Export data in the JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com"
    user_endpoint = "{}/users".format(url)
    users = requests.get(user_endpoint).json()
    tasks_endpoint = "{}/todos".format(url)
    tasks = requests.get(tasks_endpoint).json()
    user_tasks = {user.get("id"): [{"task": task.get("title"), "completed":
                  task.get("completed"), "username": user.get("username")}
                  for task in tasks
                  if task.get("userId") == user.get("id")]
                  for user in users
                  }

    """Save in Json file"""
    with open("todo_all_employees.json", 'w',
              encoding="utf-8") as file:
        json.dump(user_tasks, file)
