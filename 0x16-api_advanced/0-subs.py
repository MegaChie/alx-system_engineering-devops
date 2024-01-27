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
    url = "http://www.reddit.com/dev/api#GET_r_{}_about.json".format(subreddit)
    # with requests.get(url) as marko:
    #     polo = marko
    return (url)
