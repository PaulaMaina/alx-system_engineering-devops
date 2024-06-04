#!/usr/bin/python3
"""This function returns a list of titles of the hottest articles"""


import requests


def recurse(subreddit, hot_list[], after=""):
    """Returns a list of the hottest articles' titles"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }
    params = {"after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        results = response.json().get("data").get("children")
        for fetch_data in results:
            sub_data = fetch_data.get("data")
            title = sub_data.get("title")
            hot_list.append(title)
        after = response.json().get("data").get("children")

        if after is None:
            return hot_list
        else:
            return recurse(subreddit, hot_list, after)
    else:
        return None
