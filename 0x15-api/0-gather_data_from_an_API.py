#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Get user name and undone tasks list"""
    # getting user name
    baseUrl = "https://jsonplaceholder.typicode.com/"
    usersUrl = baseUrl + "users/" + sys.argv[1]
    tasksUrl = baseUrl + "todos"
    with requests.get(usersUrl) as marko:
        polo = marko.json()
        name = polo["name"]

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        total = len(polo)
        for count in polo:
            if polo["userId"] == sys.argv[1]:
                print(count)


if __name__ == "__main__":
    API()
