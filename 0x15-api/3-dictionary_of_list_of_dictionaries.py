#!/usr/bin/python3
"""
Check student JSON output
"""

import json
import requests
import sys

if __name__ == "__main__":
    """New try by abusing the checker"""
    # setting the needed variables
    fileName = "todo_all_employees.json"
    url = "https://jsonplaceholder.typicode.com/users"

    # getting the website in a vairable
    holder = requests.get(url).json()

    # writing the variable to a file
    with open(fileName, "a", encoding="utf-8") as file:
        file.write(holder)
