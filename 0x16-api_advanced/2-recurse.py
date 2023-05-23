#!/usr/bin/python3
"""API ADVANCED"""
import requests
import sys


def recurse(subreddit, hot_list=[], after=None):
    """A recursive function that queries the Reddit API and returns
    a list containing the titles of all hot articles for a given subreddit.
    If no results are found for the given subreddit, the function should return None"""

    headers = {"User-Agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}

    response = requests.get(
        headers=headers,
        url=url,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        hot_list.extend([child['data']['title'] for child in children])
        after = data['after']
        if after is None:
            return hot_list
        return recurse(subreddit, hot_list, after)
    else:
        return None


if __name__ == '__main__':
    if len(sys.argv) > 1:
        subreddit = sys.argv[1]
        recurse(subreddit, [])
