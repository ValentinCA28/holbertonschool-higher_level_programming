#!/usr/bin/python3

import requests


def fetch_and_print_posts():
	response = requests.get('https://jsonplaceholder.typicode.com/todos/1')
	print(response.json())