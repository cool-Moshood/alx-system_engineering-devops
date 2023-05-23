#!/usr/bin/python3
"""API ADVANCED"""
import requests
import sys


def count_words(subreddit, word_list, hot_list=[], after=None):
    """Recursive function that queries the Reddit API,
    parses the title of all hot articles, and prints
    a sorted count of given keywords
    (case-insensitive, delimited by spaces.
    Javascript should count as javascript, but java should not)"""

    headers = {"User-agent": "user_agent"}
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    params = {"limit": 100, "after": after}

    response = requests.get(
        url=url,
        headers=headers,
        params=params,
        allow_redirects=False
    )

    if response.status_code == 200:
        data = response.json()['data']
        children = data['children']
        hot_list.extend([child['data']['title']
                         for child in children])
        after = data['after']
        if after is None:
            wordcounts = {}
            search_str = " ".join(hot_list)
            wordcounts = {word.lower(): search_str.lower().count(
                word.lower()) for word in word_list}
            sorted_wordcounts = dict(
                sorted(wordcounts.items(),
                       key=lambda item: (-item[1], item[0])))
            for key, value in sorted_wordcounts.items():
                if value != 0:
                    print("{}: {}".format(key, value))
            return 0
        return count_words(subreddit, word_list, hot_list, after)
    else:
        return None


if __name__ == "__main__":
    if len(sys.argv) > 2:
        subreddit = sys.argv[1]
        word_list = sys.argv[2:]
        count_words(subreddit, word_list)
