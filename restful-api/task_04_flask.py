#!/usr/bin/env python3
"""
Simple API using Python with Flask.

This module implements a RESTful API with Flask that allows users
to be stored in memory and retrieved via various endpoints.

Routes:
    GET  /              : Returns a welcome message.
    GET  /data          : Returns a JSON list of all usernames.
    GET  /status        : Returns "OK".
    GET  /users/<username> : Returns the full user object for a username.
    POST /add_user      : Adds a new user from a JSON request body.
"""

from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route("/")
def home():
    """
    Handle the root endpoint.

    Returns:
        str: A welcome message "Welcome to the Flask API!".
    """
    return "Welcome to the Flask API!"


@app.route("/data")
def data():
    """
    Handle the /data endpoint.

    Returns:
        Response: A JSON response containing a list of all usernames
        stored in the API.
    """
    return jsonify(list(users.keys()))


@app.route("/status")
def status():
    """
    Handle the /status endpoint.

    Returns:
        str: The string "OK".
    """
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """
    Handle the /users/<username> endpoint.

    Args:
        username (str): The username to look up.

    Returns:
        Response: A JSON response with the full user object if found,
        or a 404 JSON error {"error": "User not found"} if not.
    """
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route("/add_user", methods=["POST"])
def add_user():
    """
    Handle the /add_user endpoint (POST).

    Parses the incoming JSON body and adds a new user to the
    in-memory users dictionary.

    Expected JSON body:
        {
            "username": "john",
            "name": "John",
            "age": 30,
            "city": "New York"
        }

    Returns:
        Response: A 201 JSON response with the added user's data,
        a 400 if the JSON is invalid or username is missing,
        or a 409 if the username already exists.
    """
    if not request.is_json:
        return jsonify({"error": "Invalid JSON"}), 400

    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run()
