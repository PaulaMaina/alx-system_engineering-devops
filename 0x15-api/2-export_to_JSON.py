#!/usr/bin/python3
"""Exports data in the JSON format"""
import csv
import json
import requests
import sys


if __name__ == "__main__":
    USER_ID = sys.argv[1]
    user_url = "https://jsonplaceholder.typicode.com/users/" + USER_ID
    req = requests.get(user_url)
    USERNAME = req.json().get('username')
    task_url = user_url + '/todos'
    task_req = requests.get(task_url)
    tasks = task_req.json()

    data_dict = {USER_ID: []}
    for task in tasks:
        TASK_COMPLETED_STATUS = task.get('completed')
        TASK_TITLE = task.get('title')
        data_dict[USER_ID].append({
                                  "task": TASK_TITLE,
                                  "completed": TASK_COMPLETED_STATUS,
                                  "username": USERNAME})
        with open('{}.json'.format(USER_ID), 'w') as json_file:
            json.dump(data_dict, json_file)
