#!/usr/bin/python3
import requests

# Your Datadog API and Application keys
api_key = ''
app_key = ''

# Define the dashboard name you want to retrieve
dashboard_name = 'alx dash'

# Set the Datadog API endpoint to list all dashboards
list_dashboards_url = 'https://api.datadoghq.com/api/v1/dashboard/'

headers = {
    'DD-API-KEY': api_key,
    'DD-APPLICATION-KEY': app_key
}
# Get the list of all dashboards
response = requests.get(list_dashboards_url, headers=headers)
if response.status_code == 200:
    dashboard_list = response.json().get('dashboards')
    for dashboard in dashboard_list:
        print(f'{dashboard.get("id")}: {dashboard.get("title")}')
