#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Build a JSON file with id, username, task, and task status"""
    # getting user name
    baseUrl = "https://jsonplaceholder.typicode.com/"
    usersUrl = baseUrl + "users/" + sys.argv[1]
    tasksUrl = baseUrl + "todos"
    with requests.get(usersUrl) as marko:
        polo = marko.json()
        name = polo["username"]

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        fileName = sys.argv[1] + ".json"
        file.write("{", sys.argv[1], ": ")
        with open(fileName, "a", encoding="utf-8") as file:
            for elem in polo:
                if elem["userId"] == int(sys.argv[1]):
                    file.write(json.dumps([{"task": elem["title"],
                        "completed": elem["completed"], "username": name}]),
                        separators=(',',))
        file.write("}")


if __name__ == "__main__":
    API()
