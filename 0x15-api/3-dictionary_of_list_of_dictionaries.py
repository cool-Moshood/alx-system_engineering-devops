#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees
   Python script to export data in the CSV format
   Python script to export data in the JSON format"""


import requests
import sys
import json


if __name__ == '__main__':

    base_api = 'https://jsonplaceholder.typicode.com/users'
    user_response_data = base_api

    user_response = requests.get(user_response_data).json()

    dictionary = {}
    for user in user_response:
        employee_id = user.get('id')
        username = user.get('username')
        todo_response_data = base_api + "/{}/todos".format(employee_id)
        todo_response = requests.get(todo_response_data).json()
        dictionary[employee_id] = []
        for todo in todo_response:
            dictionary[employee_id].append({
                "username": username,
                "task": todo.get('title'),
                "completed": todo.get('completed')
            })

    with open('todo_all_employees.json', 'w') as file:
        json.dump(dictionary, file)
