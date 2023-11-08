#!/usr/bin/python3
""" fetch list of hot lising using reddit api """
import requests
import sys


def recurse(subreddit, hot_list=[], count=0, next_page=None):
    url = "https://www.reddit.com/r/{}/hot/.json".format(subreddit)
    headers = {'user-agent': 'alx api advanced'}
    params = {"count": count, "next_page": next_page, "limit": 50}
    response = requests.get(
        url, params=params, headers=headers, allow_redirects=False
                            )
    if response.status_code != 200:
        return None
    data = response.json().get("data")
    next_page = data.get("next_page")
    count += data.get("dist")
    children = data.get("children")
    for child in children:
        title = child.get("title")
        hot_list.append(title)
    if next_page is not None:
        return recurse(subreddit, hot_list, count, next_page)
    return hot_list


if __name__ == "__main__":
    lst = recurse(sys.argv[1])
    if lst is not None:
        print(len(lst))
