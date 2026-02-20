#!/usr/bin/python3
"""
Module that fetches posts from the JSONPlaceholder API.

Uses the requests library to send HTTP GET requests, parse JSON
responses, print post titles, and export structured data to CSV.
"""

import requests
import csv


def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles.

    Sends a GET request to https://jsonplaceholder.typicode.com/posts,
    prints the HTTP status code, and if the request is successful (200),
    parses the JSON response and prints the title of each post.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")

    if response.status_code == 200:
        posts = response.json()

        for post in posts:
            print(post['title'])


def fetch_and_save_posts():
    """Fetch all posts from JSONPlaceholder and save them to a CSV file.

    Sends a GET request to https://jsonplaceholder.typicode.com/posts.
    If the request is successful (200), structures each post into a
    dictionary with keys 'id', 'title', and 'body', then writes the
    list of dictionaries to a file called posts.csv using csv.DictWriter.
    """
    response = requests.get('https://jsonplaceholder.typicode.com/posts')

    if response.status_code == 200:
        posts = response.json()
        posts_data = [
            {
                'id': post['id'],
                'title': post['title'],
                'body': post['body']
            }
            for post in posts
        ]

        with open('posts.csv', 'w', encoding='utf-8') as csvfile:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            writer.writerows(posts_data)
