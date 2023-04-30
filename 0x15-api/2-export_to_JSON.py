#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees
   Python script to export data in the CSV format
   Python script to export data in the JSON format"""

import requests
import sys
import json


if __name__ == '__main__':
    """REST API error control"""
    if len(sys.argv) > 1 and isinstance(eval(sys.argv[1]), int):
        pass
    else:
        sys.exit(0)

    base_api = 'https://jsonplaceholder.typicode.com/users'
    employee_id = sys.argv[1]
    user_response_data = base_api + "/{}".format(employee_id)
    todo_response_data = base_api + "/{}/todos".format(employee_id)

    user_response = requests.get(user_response_data).json()
    todo_response = requests.get(todo_response_data).json()

    USERNAME = user_response.get('username')

    dictionary = {employee_id: []}
    for todo in todo_response:
        dictionary[employee_id].append({
            "task": todo.get('title'),
            "completed": todo.get('completed'),
            "username": USERNAME
        })

    with open("{}.json".format(employee_id), 'w') as filename:
        json.dump(dictionary, filename)
