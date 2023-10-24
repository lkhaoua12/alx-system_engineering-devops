#!/usr/bin/python3
""" export data in json format """
import json
import requests
from sys import argv

if __name__ == "__main__":
    u_id = argv[1]
    url = 'https://jsonplaceholder.typicode.com/'
    user = requests.get(url + "users/" + u_id).json()
    todos = requests.get(url + 'todos', params={'userId': u_id}).json()

    with open(f'{u_id}.json', 'w') as jfile:
        json.dump({
            u_id:
            [{"task": t.get('title'),
              "completed": t.get('completed'),
              "username": user.get('username')} for t in todos]
        }, jfile)
