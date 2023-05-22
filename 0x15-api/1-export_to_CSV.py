#!/usr/bin/python3
"""A Python script that, using this REST API, for a given employee ID,
returns information about his/her TODO list progress"""

import csv
import requests
import sys


if __name__ == "__main__":
    url = "https://jsonplaceholder.typicode.com/"
    user = requests.get(url + "users/{}".format(sys.argv[1])).json()
    user_name = user.get("username")
    todos = requests.get(url + "todos", params={"userId": sys.argv[1]}).json()
    user_id = sys.argv[1]


    with open("{}.csv".format(user_id), "w", newline="") as csvfile:
        writer = csv.writer(csvfile, quoting=csv.QUOTE_ALL)
        [writer.writerow(
            [user_id, user_name, task.get("completed"), task.get("title")]
         ) for task in todos]


