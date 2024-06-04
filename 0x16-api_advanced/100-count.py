#!/usr/bin/python3
"""This function prints a sorted count of given keywords"""


import requests


def count_words(subreddit, word_list, after="", word_dict={}):
    """Prints a sorted count of given keywords delimited by spaces"""
    if not word_dict:
        for word in word_list:
            if word.lower() not in word_dict:
                word_dict[word.lower()] = 0

    if after is None:
        dict_word = sorted(word_dict.items(), key=lambda x: (-x[1], x[0]))
        for word in dict_word:
            if word[1]:
                print('{}: {}'.format(word[0], word[1]))
        return None

    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": ("Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                       "AppleWebKit/537.36 (KHTML, like Gecko) "
                       "Chrome/91.0.4472.124 Safari/537.36")
    }
    params = {"limit": 100, "after": after}

    response = requests.get(url, headers=headers, params=params)
    if response.status_code != 200:
        return None

    try:
        hot_data = response.json().get("data").get("children")
        after_data = response.json().get("data").get("after")
        for post in hot_data:
            title = post.get("data").get("title")
            lower = [word.lower() for word in title.split(' ')]

            for word in word_dict.keys():
                word_dict[word] += lower.count(word)

    except Exception:
        return None

    count_words(subreddit, word_list, after_data, word_dict)
