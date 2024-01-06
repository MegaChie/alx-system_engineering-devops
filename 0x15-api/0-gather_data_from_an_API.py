#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Get user name and undone tasks list"""
    # getting user name
    oldUrl = "https://jsonplaceholder.typicode.com/users/"
    url = oldUrl + sys.argv[1]
    with requests.get(url) as marko:
        polo = marko.json()
        print(polo['name'])


if __name__ == "__main__":
    API()
