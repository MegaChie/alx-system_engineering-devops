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
        with open(fileName, "a", encoding="utf-8") as file:
            file.write("{")
            file.write(str(sys.argv[1]))
            file.write(": [")
            items = []
            for elem in polo:
                if elem["userId"] == int(sys.argv[1]):
                    items.append(json.dumps({"task": elem["title"],
                        "completed": elem["completed"],
                        "username": name}))
            file.write(",".join(items))
            file.write("]}")


if __name__ == "__main__":
    API()
