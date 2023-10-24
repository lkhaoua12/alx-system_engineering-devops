#!/usr/bin/python3
""" fetch employee_str todo-list status and print it """
import requests
import sys


if __name__ == "__main__":
    u_id = sys.argv[1]
    url = f'https://jsonplaceholder.typicode.com/users/{u_id}'
    employee_data = requests.get(url).json()
    employee_name = employee_data.get('name')
    todo_url = f'https://jsonplaceholder.typicode.com/todos?userId={u_id}'
    todo_list = requests.get(todo_url).json()
    finished_task = [todo for todo in todo_list if todo.get('completed')]
    total_tasks = f'{len(finished_task)}/{len(todo_list)}'
    print(f'Employee {employee_name} is done with tasks({total_tasks}):')
    for task in finished_task:
        print(f'\t{task.get("title")}')
