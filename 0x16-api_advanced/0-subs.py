#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
returns the number of subscribers for a given subreddit
"""

import requests


def number_of_subscribers(subreddit):
    """Function that returns number of subscribers of a subreddit passed"""

    url = f"https://www.reddit.com/r/{subreddit}/about.json"
    user_agent = "Mozilla/5.0"

    response = requests.get(url, headers=user_agent)

    if response.status_code == 200:
        data = response.json()
        subscribers = data['data']['subscribers']
        return subscribers
    else:
        return 0
