#!/usr/bin/env python3
"""
Flask API with Basic Authentication, JWT Authentication, and Role-Based
Access Control.

This module demonstrates three layers of API security:
  - **Basic HTTP Authentication** using Flask-HTTPAuth with hashed
    passwords stored via werkzeug.security.
  - **Token-based Authentication** using JSON Web Tokens (JWT) via
    Flask-JWT-Extended.
  - **Role-Based Access Control (RBAC)** that restricts certain
    endpoints to users with the ``admin`` role.

Users are stored in-memory in a dictionary. Passwords are hashed with
werkzeug's ``generate_password_hash`` and verified with
``check_password_hash``.

Endpoints:
    GET  /basic-protected
        Protected by HTTP Basic Auth. Returns
        ``"Basic Auth: Access Granted"`` on success (200) or
        ``401 Unauthorized`` on failure.

    POST /login
        Accepts a JSON body with ``username`` and ``password``.
        Returns a JWT access token on success (200) or
        ``401 Unauthorized`` on invalid credentials.

    GET  /jwt-protected
        Protected by a valid JWT token in the ``Authorization`` header.
        Returns ``"JWT Auth: Access Granted"`` on success (200) or
        ``401 Unauthorized`` on missing / invalid token.

    GET  /admin-only
        Protected by JWT **and** requires the ``admin`` role.
        Returns ``"Admin Access: Granted"`` (200) for admins or
        ``403 Forbidden`` for non-admin users.

Custom JWT error handlers ensure that every authentication error
(missing, invalid, expired, revoked token, or fresh-token requirement)
consistently returns a ``401`` status code.
"""

from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (
    JWTManager,
    create_access_token,
    get_jwt,
    get_jwt_identity,
    jwt_required,
)
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
app.config["JWT_SECRET_KEY"] = "super-secret-key-change-me"

auth = HTTPBasicAuth()
jwt = JWTManager(app)

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user",
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin",
    },
}


# ---------------------------------------------------------------------------
# Basic Authentication helpers
# ---------------------------------------------------------------------------

@auth.verify_password
def verify_password(username, password):
    """
    Verify a username / password pair for HTTP Basic Auth.

    Called automatically by Flask-HTTPAuth on every request to a route
    decorated with ``@auth.login_required``.

    Args:
        username (str): The username sent in the Basic Auth header.
        password (str): The plaintext password sent in the Basic Auth
            header.

    Returns:
        str or None: The username if credentials are valid, otherwise
        ``None`` (which triggers a 401 response).
    """
    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        return username
    return None


# ---------------------------------------------------------------------------
# JWT custom error handlers – always return 401
# ---------------------------------------------------------------------------

@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    """
    Handle requests with a missing or unreadable JWT.

    Args:
        err (str): Description of the error provided by
            Flask-JWT-Extended.

    Returns:
        tuple: A JSON response ``{"error": "Missing or invalid token"}``
        with HTTP status 401.
    """
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    """
    Handle requests containing an invalid JWT.

    Args:
        err (str): Description of the error provided by
            Flask-JWT-Extended.

    Returns:
        tuple: A JSON response ``{"error": "Invalid token"}`` with
        HTTP status 401.
    """
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(jwt_header, jwt_payload):
    """
    Handle requests containing an expired JWT.

    Args:
        jwt_header (dict): The header section of the expired JWT.
        jwt_payload (dict): The payload section of the expired JWT.

    Returns:
        tuple: A JSON response ``{"error": "Token has expired"}`` with
        HTTP status 401.
    """
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(jwt_header, jwt_payload):
    """
    Handle requests containing a revoked JWT.

    Args:
        jwt_header (dict): The header section of the revoked JWT.
        jwt_payload (dict): The payload section of the revoked JWT.

    Returns:
        tuple: A JSON response ``{"error": "Token has been revoked"}``
        with HTTP status 401.
    """
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(jwt_header, jwt_payload):
    """
    Handle requests that require a fresh JWT but received a non-fresh one.

    Args:
        jwt_header (dict): The header section of the JWT.
        jwt_payload (dict): The payload section of the JWT.

    Returns:
        tuple: A JSON response ``{"error": "Fresh token required"}``
        with HTTP status 401.
    """
    return jsonify({"error": "Fresh token required"}), 401


# ---------------------------------------------------------------------------
# Routes
# ---------------------------------------------------------------------------

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    """
    Endpoint protected by HTTP Basic Authentication.

    The client must include an ``Authorization: Basic <credentials>``
    header with valid username and password.

    Returns:
        str: ``"Basic Auth: Access Granted"`` with HTTP 200 on success.
        If credentials are missing or wrong, Flask-HTTPAuth
        automatically returns a 401 Unauthorized response.
    """
    return "Basic Auth: Access Granted"


@app.route("/login", methods=["POST"])
def login():
    """
    Authenticate a user and return a JWT access token.

    The client must send a JSON body containing ``username`` and
    ``password`` fields.

    Example request body::

        {
            "username": "user1",
            "password": "password"
        }

    Returns:
        Response: A JSON object ``{"access_token": "<token>"}`` with
        HTTP 200 if the credentials are valid. Returns
        ``{"error": "Bad username or password"}`` with HTTP 401
        if authentication fails.
    """
    data = request.get_json()
    username = data.get("username")
    password = data.get("password")

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        access_token = create_access_token(
            identity=username,
            additional_claims={"role": user["role"]},
        )
        return jsonify(access_token=access_token)

    return jsonify({"error": "Bad username or password"}), 401


@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    """
    Endpoint protected by JWT authentication.

    The client must include an ``Authorization: Bearer <token>`` header
    with a valid JWT obtained from the ``/login`` endpoint.

    Returns:
        str: ``"JWT Auth: Access Granted"`` with HTTP 200 on success.
        Returns 401 if the token is missing, invalid, or expired.
    """
    return "JWT Auth: Access Granted"


@app.route("/admin-only")
@jwt_required()
def admin_only():
    """
    Endpoint restricted to users with the ``admin`` role.

    The client must provide a valid JWT whose payload contains
    ``"role": "admin"``.

    Returns:
        str: ``"Admin Access: Granted"`` with HTTP 200 if the
        authenticated user is an admin. Returns
        ``{"error": "Admin access required"}`` with HTTP 403
        if the user does not have the admin role.
    """
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"


if __name__ == "__main__":
    app.run()
