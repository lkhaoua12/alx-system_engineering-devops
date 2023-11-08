#!/usr/bin/python3
""" hot posts listed for a given subreddit """
import requests
import sys


def top_ten(subreddit):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {"User-Agent": "0x16. API_advanced"}
    params = {'limit': 10}
    response = requests.get(
        url, headers=headers, params=params, allow_redirects=False
    )
    if response.status_code != 200:
        print("None")
        return
    data = response.json().get('data')
    for child in data.get('children'):
        print(child.get("data").get("title"))


if __name__ == "__main__":
    top_ten(sys.argv[1])
