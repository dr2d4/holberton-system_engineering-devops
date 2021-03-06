#!/usr/bin/python3
"""
    Exports info in the CSV file
"""

import csv
import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}"
    userId = sys.argv[1]

    user = requests.get(url.format(userId))
    name = user.json().get('username')

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    file = userId + '.csv'

    with open(file, mode='w') as f:
        writer = csv.writer(f, quoting=csv.QUOTE_ALL)

        for task in todos.json():
            if task.get('userId') == int(userId):
                row = [userId, name, task.get('completed'), task.get('title')]
                writer.writerow(row)
