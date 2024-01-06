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
        count = 0
        # for element in range(len(polo)):
        #     if polo[element]["userId"] == sys.argv[1]:
        #         count = count + 1
        #         print("found")
        # print(count)
        print(polo[1])


if __name__ == "__main__":
    API()
