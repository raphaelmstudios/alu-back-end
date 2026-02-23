#!/usr/bin/python3
"""Script that gathers data from an API and returns employee TODO progress."""
import requests
import sys


if __name__ == "__main__":
    employee_id = int(sys.argv[1])
    base_url = "https://jsonplaceholder.typicode.com"

    user = requests.get("{}/users/{}".format(base_url, employee_id)).json()
    todos = requests.get("{}/todos?userId={}".format(
        base_url, employee_id)).json()

    employee_name = user.get("name")
    done_tasks = [task for task in todos if task.get("completed")]
    total_tasks = len(todos)
    number_of_done_tasks = len(done_tasks)

    print("Employee {} is done with tasks({}/{}):".format(
        employee_name, number_of_done_tasks, total_tasks))

    for task in done_tasks:
        print("\t {}".format(task.get("title"))i)
