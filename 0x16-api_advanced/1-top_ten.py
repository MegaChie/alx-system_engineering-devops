#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def top_ten(subreddit=sys.argv[1]):
    """
    Returns the number of subscribers for a given subreddit,
    or 0 if an invalid subreddit is given.
    """
    # firstly, authenticate and get token
    client = "XVngJrvVrijzTzOU09512w"
    clientKey = "h6FGkpwlvaqLY1RjMkr-fn4Yu26SNQ"
    login = requests.auth.HTTPBasicAuth(client, clientKey)
    header = {"User-Agent": "Mega/0.0.2"}
    sendData = {"grant_type": "client_credentials"}
    wanted = {"limit": 9}
    with requests.post("https://www.reddit.com/api/v1/access_token",
                    auth=login, headers=header, data=sendData) as authMarko:
        poloKey = authMarko.json()
    header["Authorization"] = "bearer {}".format(poloKey["access_token"])

    # using the token to access the API
    url = "https://oauth.reddit.com/r/{}/hot".format(subreddit)
    with requests.get(url, headers=header, params=wanted) as marko:
        if marko.status_code >= 300:
            return None
        polo = marko.json()
    for hot in polo["data"]["children"]:
        print(hot["data"]["title"])
