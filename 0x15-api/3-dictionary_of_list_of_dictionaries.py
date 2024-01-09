#!/usr/bin/python3
"""API usage"""
import json
import requests
import sys


def API():
    """Build a JSON file with id, username, task, and task status"""
    # getting user name
    baseUrl = "https://jsonplaceholder.typicode.com/"
    tasksUrl = baseUrl + "todos"
    def em(a):
        usersUrl = baseUrl + "users/" + str(a)
        with requests.get(usersUrl) as marko:
            polo = marko.json()
            name = polo["username"]
            return name

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        userdic = {}
        for user in polo:
            for person in user["userId"]
                if user["completed"] is False:
                    userdic[user["userId"]] = [{"username": em(user["userId"]),
                                                "task": user["title"],
                                                "completed": user["completed"],}]
    print(userdic)

    # Writing file
    # with open(fileName, "a", encoding="utf-8") as file:
    #     file.write(undone)


if __name__ == "__main__":
    API()
