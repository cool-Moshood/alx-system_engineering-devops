#!/usr/bin/python3

"""API ADVANCED"""

import requests
import sys


def top_ten(subreddit):
    """a function that queries the Reddit API and prints
    the titles of the first 10 hot posts listed for a given subreddit"""

    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/hot.json?limit=10".format(subreddit)
    response = requests.get(
        url=url,
        headers=headers,
        allow_redirects=False
    )
    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        for child in children:
            title = child['data']['title']
            print(title)
    else:
        print("None")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        top_ten(subreddit)
