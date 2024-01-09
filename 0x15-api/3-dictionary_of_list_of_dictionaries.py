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
    def emna(a):
        usersUrl = baseUrl + "users/" + str(a)
        with requests.get(usersUrl) as marko:
            polo = marko.json()
            name = polo["username"]
            return name

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        userdic = {}
        for num in range(1, 11):
            undone = []
            for user in polo:
                if user["userId"] == num:
                    undone.append(json.dumps({"username": emna(num),
                                   "task": user["title"],
                                   "completed": str(user["completed"])}))
            userdic[num] = undone
    
    # Fail safe: replacing ' with " and ucapilatizing False and True
    # before = str(userdic)
    # after = before.replace("'", '"')
    # after = after.replace("False", "false")
    # after = after.replace("True", "true")
    print(userdic)

    # Writing file
    # with open(fileName, "a", encoding="utf-8") as file:
    #     file.write(userdic)


if __name__ == "__main__":
    API()