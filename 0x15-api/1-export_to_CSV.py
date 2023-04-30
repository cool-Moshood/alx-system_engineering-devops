#!/usr/bin/python3
"""Python script to export data in the CSV format
   Accessing a REST API for todo lists of employees"""

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

    USERNAME = user_response.get('username')

    with open('{}.csv'.format(employee_id), 'w') as file:
        for todo in todo_response:
            file.write('"{}","{}","{}","{}"\n'
                   .format(employee_id, USERNAME, todo.get('completed'),
                           todo.get('title')))
