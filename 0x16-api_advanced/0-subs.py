#!/usr/bin/python3
""" fetch num of subs for a subreddit """

import requests
import sys


def number_of_subscribers(subreddit):
    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    headers = {
        "User-Agent": "0x16 API"
        }
    response = requests.get(url, headers=headers, allow_redirects=False)
    if response.status_code == 200:
        sub = response.json().get("data").get("subscribers")
        return sub
    else:
        return 0


if __name__ == "__main__":
    subr = sys.argv[1]
    print(number_of_subscribers(subr))
