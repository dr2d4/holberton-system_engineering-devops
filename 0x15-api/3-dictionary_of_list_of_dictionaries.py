#!/usr/bin/python3
"""
    Exports info in the JSON file
"""

import requests
import json
import sys

if __name__ == "__main__":
    users = requests.get("https://jsonplaceholder.typicode.com/users")
    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    users = users.json()
    todos = todos.json()
    users_tasks = {}
    tasks_list = []

    for user in users:
        for task in todos:
            if task.get('userId') == user.get('id'):
                c = task.get('completed')
                u = user.get('username')
                t = task.get('title')

                row = {"username": u, "task": t, "completed": c}
                tasks_list.append(row)

        users_tasks[user.get('id')] = tasks_list

    with open('todo_all_employees.json', mode='w') as f:
        json.dump(users_tasks, f)
