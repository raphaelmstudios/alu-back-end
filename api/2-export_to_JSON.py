#!/usr/bin/python3
"""This script exports employee TODO data to a JSON file."""
import json
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(
        base_url, employee_id)).json()

    username = user.get("username")
    filename = "{}.json".format(employee_id)

    tasks = [
        {
            "task": task.get("title"),
            "completed": task.get("completed"),
            "username": username
        }
        for task in todos
    ]

    with open(filename, "w") as jsonfile:
        json.dump({str(employee_id): tasks}, jsonfile)