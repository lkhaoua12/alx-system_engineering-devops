#!/usr/bin/python3
""" fetch list of hot lising using reddit api """
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {"User-Agent": "Alx/api"}

    if after:
        params = {"limit": 100, "after": after}
    else:
        params = {"limit": 100}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code != 200:
        return None

    data = response.json().get("data")

    if data is None:
        return None

    children = data.get("children")

    if not children:
        return hot_list

    for child in children:
        title = child.get("data").get("title")
        hot_list.append(title)

    after = data.get("after")

    if not after:
        return hot_list
    else:
        return recurse(subreddit, hot_list, after)


if __name__ == "__main__":
    lst = recurse(sys.argv[1])
    if lst is not None:
        print(len(lst))
