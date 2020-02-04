#!/usr/bin/python3
"""
    Exports info in the JSON file
"""

import json
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}"
    userId = sys.argv[1]

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    user = requests.get(url.format(userId))
    todos = todos.json()

    user_tasks = {}
    rows = []

    for task in todos:
        if task.get('userId') == int(userId):
            u = user.json().get('username')
            c = task.get('completed')
            t = task.get('title')

            row = {"task": t, "completed": c, "username": u}
            rows.append(row)

    user_tasks[userId] = rows
    file = userId + '.json'

    with open(file, mode='w') as f:
        json.dump(user_tasks, f)
