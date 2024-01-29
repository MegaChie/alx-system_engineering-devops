#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def number_of_subscribers(subreddit=sys.argv[1]):
    """
    Returns the number of subscribers for a given subreddit,
    or 0 if an invalid subreddit is given.
    """
    url = "https://www.reddit.com/r/{}/about.json".format(subreddit)
    with requests.get(url, headers={"User-Agent": "Mega"}) as mark:
        if marko.status_code >= 300:
            return 0
        polo = marko.json().get("data").get("subscribers")
    return polo