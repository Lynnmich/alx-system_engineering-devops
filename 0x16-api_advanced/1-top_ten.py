#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that prints the title of the first 10 listed posts
    """
<<<<<<< HEAD
    url = "https://reddit.com/r/{}/hot.json".format(subreddit)
    user_agent = "Mozilla/5.0"
    limits = 10

    response = requests.get(
        url, headers={"user-agent": user_agent}, params={"limit": limits})
    if not response:
        print('None')
        return
    response = response.json()
    posts = response['data']['children']
    for post in posts:
        print(post['data']['title'])
    return
