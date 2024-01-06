#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Get user name and undone tasks list"""
    # getting user name
    url = "https://jsonplaceholder.typicode.com/users/"
    with requests.get(url) as marko:
        polo = marko.json()
        print(type(polo))
        print(len(polo))


if __name__ == "__main__":
    API()
