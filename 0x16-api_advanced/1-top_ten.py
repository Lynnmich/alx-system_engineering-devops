#!/usr/bin/python3
"""
Write a function that queries the Reddit API and
prints the titles of the first 10 hot posts listed for a given subreddit
"""

import requests


def top_ten(subreddit):
    """
    Function that prints the title of the first 10 listed posts

    Limit the number of posts to 10
    """
    url = f"https://www.reddit.com/r/{subreddit}/hot.json"
    headers = {'User-Agent': 'Mozilla/5.0'}
    params = {'limit': 10}

    response = requests.get(url, headers=headers, params=params)

    if response.status_code == 200:
        data = response.json()
        posts = data['data']['children']

        for post in posts:
            title = post['data']['title']
            print(title)
    else:
        print(None)
