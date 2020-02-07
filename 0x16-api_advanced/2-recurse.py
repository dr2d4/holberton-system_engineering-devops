#!/usr/bin/python3
"""
    Api Reddit
"""
import requests


def recurse(subreddit, hot_list=[], after=None):
    """
        Get data recursive
    """
    url = 'https://api.reddit.com/r/{}/hot'.format(subreddit)

    params = {
        'after': after,
        't': 'all',
    }

    hs = {
        'User-Agent': 'My-User-Agent',
    }

    request = requests.get(url, params, headers=hs, allow_redirects=False)
    top_posts = request.json()

    if request.status_code == 404:
        return None

    data = top_posts.get('data')

    if data:
        children = data['children']

        for post in children:
            hot_list.append(post['data']['title'])

        after = data.get('after')

        if after is not None:
            recurse(subreddit, hot_list, after)

    return hot_list
