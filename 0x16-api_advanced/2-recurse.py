#!/usr/bin/python3
"""
    Api Reddit
"""
import requests


def recurse(subreddit, hot_list=[], count=0, after=None):
    """
        Get data recursive
    """
    url = "https://www.reddit.com/r/{}/hot.json".format(subreddit)

    params = {
        "count": count,
        "after": after,
    }

    hs = {
        "User-Agent": "My-User-Agent",
    }

    sub_info = requests.get(url, params, headers=hs, allow_redirects=False)
    sub_info = sub_info.json()

    if sub_info.status_code >= 400:
        return None

    hot_l = [child["data"]["title"] for child in sub_info["data"]["children"]]
    hot_l += hot_list

    if not sub_info["data"]["after"]:
        return hot_l

    count = sub_info["data"]["count"]
    after = sub_info["data"]["after"]

    return recurse(subreddit, hot_l, count, after)
