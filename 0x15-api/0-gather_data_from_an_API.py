#!/usr/bin/python3
"""Accessing a REST API for todo lists of employees"""

import requests
import sys


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

EMPLOYEE_NAME = user_response.get('name')

NUMBER_OF_DONE_TASKS = 0
TOTAL_NUMBER_OF_TASKS = 0
DONE_TASKS = []

for todo in todo_response:
    if todo.get("completed"):
        NUMBER_OF_DONE_TASKS += 1
        DONE_TASKS.append(todo.get("title"))
    TOTAL_NUMBER_OF_TASKS += 1

print("Employee {} is done with tasks({}/{})"
      .format(EMPLOYEE_NAME, NUMBER_OF_DONE_TASKS, TOTAL_NUMBER_OF_TASKS))

for TASK_TITLE in DONE_TASKS:
    print(TASK_TITLE)
