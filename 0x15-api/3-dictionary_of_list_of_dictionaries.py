#!/usr/bin/python3
""" exports in json format """
import json
import requests


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    users = requests.get(url + "users").json()
    t_url = url + "todos"

    with open("todo_all_employees.json", "w") as jfile:
        json.dump({
            user.get('id'): [
                {"username": user.get('username'),
                 "task": t.get('title'),
                 "completed": t.get('completed')}
                for t in requests.get(t_url,
                                      params={"userId": user.get('id')}).json()
            ]for user in users}, jfile)
