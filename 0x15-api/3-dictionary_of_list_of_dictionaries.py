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
    def empnam(a):
        usersUrl = baseUrl + "users/" + a
        with requests.get(usersUrl) as marko:
            polo = marko.json()
            name = polo["username"]
            return name

    # Getting tasks list
    with requests.get(tasksUrl) as marko:
        polo = marko.json()
        undone = []
        fileName = "todo_all_employees.json"
        for user in polo:
            tasks = []
            if polo["completed"] is False:
                tasks.append(json.dump(polo["userId"]: [{
                    "username": empnam(polo["userId"]),
                    "task": polo["title"],
                    "completed": polo["completed"]}]))
        with open(fileName, "a", encoding="utf-8") as file:


if __name__ == "__main__":
    API()
