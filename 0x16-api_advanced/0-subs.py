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
    # firstly, authenticate and get token
    client = "WGstrtKlV2DGfioJn-RPXQ"
    clientKey = "eBZqUUfYtdmeWENV9bZCV7ivx2FVAw"
    login = requests.auth.HTTPBasicAuth(client, clientKey)
    header = {"User-Agent": "Mega/0.2"}
    with requests.post("https://www.reddit.com/api/v1/access_token",
                       auth=login, headers=header) as authMarko:
        poloKey = authMarko.json()["access_token"]
    header["Authorization"] = "bearer {}".format(poloKey)

    # using the token to access the API
    url = "https://oauth.reddit.com/r/{}/about".format(subreddit)
    with requests.get(url, headers=header) as marko:
        if marko.status_code >= 300:
            return 0
        polo = marko.json().get("data").get("subscribers")
    return polo
