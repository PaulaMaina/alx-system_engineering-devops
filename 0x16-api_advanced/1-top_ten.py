#!/usr/bin/python3
"""This function prints the titles of the first 10 hot posts"""


import requests


def top_ten(subreddit):
    """Prints the top ten posts"""
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }
    params = {"limit": 10}

    try:
        response = requests.get(url, headers=headers, params=params)
        response.raise_for_status()
        if response.status_code == 404:
            print("None")
            return

        data = response.json()
        results = data.get("data")
        for post in results.get("children"):
            print(post.get("data").get("title"))
    except requests.RequestException as err:
        print("An error occurred: ".format(err))
