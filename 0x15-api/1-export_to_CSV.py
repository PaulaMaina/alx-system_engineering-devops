#!/usr/bin/python3
"""Export API to CSV"""
import csv
import requests
import sys


if __name__ == "__main__":
    user = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + user
    req = requests.get(user_url)
    user_name = req.json().get('username')
    task_req = requests.get(user_url + '/todos')
    tasks = task_req.json()

    with open('{}.csv'.format(user), 'w') as csv_file:
        for task in tasks:
            completed_tasks = task.get('completed')
            task_title = task.get('title')
            csv_file.write('"{}","{}","{}","{}"\n'.format
                           (user, user_name, completed_tasks, task_title))
