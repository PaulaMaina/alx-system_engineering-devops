#!/usr/bin/python3
"""This function queries the Redit API and returns the number of subscribers"""


import requests


def number_of_subscribers(subreddit):
    """Returns the total number of subscribers"""
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }

    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status()
        data = response.json()
        return data.get("data", {}).get("subscribers", 0)
    except requests.RequestException as err:
        print("An error occurred: ".format(err))
        return 0
