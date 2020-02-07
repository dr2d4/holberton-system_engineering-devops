#!/usr/bin/python3
"""
  Api Reddit
"""
import requests


def number_of_subscribers(subreddit):
    """
      Get JSON of users of a subreddit
    """
    url = 'https://www.reddit.com/r/{}/about.json'.format(subreddit)

    headers = {
        'User-Agent': 'My-User-Agent'
    }

    resp = requests.get(url, headers=headers, allow_redirects=False)

    if resp.status_code >= 300:
        return 0

    resp = resp.json()['data']['subscribers']
    return resp
