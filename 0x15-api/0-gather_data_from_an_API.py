#!/usr/bin/python3
"""
    Get tasks in completed and print
"""

import requests
import sys

if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users/{}"
    userId = sys.argv[1]

    user = requests.get(url.format(userId))
    ne = user.json()['name']

    todos = requests.get('https://jsonplaceholder.typicode.com/todos')
    list_tasks = []
    cd = 0
    ct = 0

    for task in todos.json():
        if task.get('userId') == int(userId):
            ct += 1

            if task.get('completed'):
                list_tasks.append(task['title'])
                cd += 1

    print('Employee {} is done with tasks({}/{}):'.format(ne, cd, ct))
    for task in list_tasks:
        print("\t {}".format(task))
