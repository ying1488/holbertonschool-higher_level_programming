#!/usr/bin/python3
"""This module handles a method to fetch posts
from JSONPlaceholder using requests.get()
"""

import requests
import json
import csv

def fetch_and_print_posts():
    url = 'https://jsonplaceholder.typicode.com/todos'
    res = requests.get(url)
    print("Status Code: {}".format(res.status_code))
    if res: 
        data = res.json()
    for todo in data:
        print(todo["title"])

def fetch_and_save_posts():
    print ("here")