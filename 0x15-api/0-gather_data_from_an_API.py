import requests
import sys

if len(sys.argv) != 2:
    print("Usage: python3 script_name.py <employee_id>")
    sys.exit(1)

employee_id = sys.argv[1]

url = f"https://jsonplaceholder.typicode.com/users/{employee_id}"
response = requests.get(url)

if response.status_code != 200:
    print("Employee not found")
    sys.exit(1)

employee_data = response.json()
employee_name = employee_data['name']

url = f"https://jsonplaceholder.typicode.com/todos?userId={employee_id}"
response = requests.get(url)
todos = response.json()

completed_tasks = [todo for todo in todos if todo['completed']]
total_tasks = len(todos)

print(f"Employee {employee_name} is done with tasks({len(completed_tasks)}/{total_tasks}):")
for todo in completed_tasks:
    print(f"\t{todo['title']}")
