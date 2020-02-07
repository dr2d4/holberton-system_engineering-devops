#!/usr/bin/python3
"""
    Api Reddit
"""
import requests


def top_ten(subreddit):
    """
        Get top ten in subreddit
    """
    url = 'https://www.reddit.com/r/{}/hot.json?limit=10'.format(subreddit)

    headers = {
        'User-Agent': 'My-User-Agent',
    }

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code >= 300:
        print('None')
    else:
        children = resp.json()['data']['children']

        for child in children:
            print(child['data']['title'])
