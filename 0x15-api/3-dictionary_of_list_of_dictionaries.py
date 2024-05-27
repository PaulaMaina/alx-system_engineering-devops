#!/usr/bin/python3
"""Exports all tasks from all employees in JSON format"""
import json
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/users"
    req = requests.get(url)
    users = req.json()
    users_dict = {}
    for user in users:
        user_id = user.get('id')
        username = user.get('username')
        url = "https://jsonplaceholder.typicode.com/users/{}".format(user_id)
        task_url = url + '/todos'
        tasks = req.json()
        users_dict[user_id] = []
        for task in tasks:
            task_completed_status = task.get('completed')
            task_title = task.get('title')
            users_dict[user_id].append({
                                       "task": task_title,
                                       "completed": task_completed_status,
                                       "username": username})
            with open('todo_all_employees.json', 'w') as json_file:
                json.dump(users_dict, json_file)
