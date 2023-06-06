#!/usr/bin/python3
"""
Queries the Reddit API and returns a list of titles of all hot articles for a given subreddit.
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
    Returns a list of titles of all hot articles for a subreddit.
    If the subreddit is invalid or no results are found, returns None.
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3"
    }
    params = {"limit": 100, "after": after}
    response = requests.get(url, headers=headers,
                            params=params, allow_redirects=False)
    if response.status_code == 200:
        data = response.json()
        posts = data["data"]["children"]
        after = data["data"]["after"]
        for post in posts:
            hot_list.append(post["data"]["title"])
        if after is not None:
            return recurse(subreddit, hot_list, after)
        return hot_list
    else:
        return None
