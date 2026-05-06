# Python - RESTful API

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-000000.svg?logo=flask&logoColor=white)
![REST API](https://img.shields.io/badge/Concept-REST%20API-009688.svg)
![JWT](https://img.shields.io/badge/Auth-JWT-000000.svg?logo=jsonwebtokens&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Construire et securiser des API RESTful en Python, de http.server basique a Flask avec authentification JWT et controle d'acces par roles.

---

## Objectifs d'apprentissage

- Consommer une API externe avec la librairie `requests`
- Exporter des donnees au format CSV
- Creer un serveur HTTP basique avec `http.server`
- Construire une API REST avec Flask (CRUD complet)
- Implementer l'authentification HTTP Basic et JWT
- Mettre en place un controle d'acces par roles (RBAC)

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |
| ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) | 3.x | Framework web | `pip install flask` |
| ![JWT](https://img.shields.io/badge/JWT-000000?logo=jsonwebtokens&logoColor=white) | - | Authentification par token | `pip install flask-jwt-extended` |

---

## Taches

### 2. Consuming an API with requests
> **Objectif** : Recuperer des posts depuis une API externe et les exporter en CSV

```python
import requests
import csv

def fetch_and_print_posts():
    """Fetch all posts from JSONPlaceholder and print their titles."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    print(f"Status Code: {response.status_code}")
    if response.status_code == 200:
        for post in response.json():
            print(post['title'])

def fetch_and_save_posts():
    """Fetch posts and save id, title, body to posts.csv."""
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    if response.status_code == 200:
        posts_data = [{'id': p['id'], 'title': p['title'], 'body': p['body']}
                      for p in response.json()]
        with open('posts.csv', 'w', encoding='utf-8') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=['id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(posts_data)
```

### 3. Simple HTTP Server
> **Objectif** : Creer un serveur HTTP basique avec des endpoints JSON et texte

```python
import http.server
import json

class SimpleHTTPRequestHandler(http.server.BaseHTTPRequestHandler):
    def do_GET(self):
        """Handle GET requests for /, /data, /status, /info endpoints."""
        if self.path == "/":
            # Returns plain text greeting
        elif self.path == "/data":
            # Returns JSON data
        elif self.path == "/status":
            # Returns "OK"
        elif self.path == "/info":
            # Returns API version and description as JSON
        else:
            # 404 Not Found
```

### 4. Flask API
> **Objectif** : Construire une API REST avec Flask pour gerer des utilisateurs en memoire

```python
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}

@app.route("/")
def home():
    return "Welcome to the Flask API!"

@app.route("/data")
def data():
    return jsonify(list(users.keys()))

@app.route("/users/<username>")
def get_user(username):
    user = users.get(username)
    if user is None:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)

@app.route("/add_user", methods=["POST"])
def add_user():
    """Add a new user from JSON body. Returns 201, 400 or 409."""
    data = request.get_json()
    username = data.get("username")
    # Validation et ajout
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201
```

### 5. Basic Security - Auth & JWT & RBAC
> **Objectif** : Securiser l'API avec HTTP Basic Auth, JWT et roles

```python
from flask import Flask, jsonify, request
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import JWTManager, create_access_token, jwt_required, get_jwt
from werkzeug.security import check_password_hash, generate_password_hash

app = Flask(__name__)
auth = HTTPBasicAuth()
jwt = JWTManager(app)

@app.route("/basic-protected")
@auth.login_required
def basic_protected():
    return "Basic Auth: Access Granted"

@app.route("/login", methods=["POST"])
def login():
    """Authenticate user and return JWT access token."""
    # Verifie credentials, genere un token avec le role

@app.route("/jwt-protected")
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"

@app.route("/admin-only")
@jwt_required()
def admin_only():
    """Restricted to users with admin role."""
    claims = get_jwt()
    if claims.get("role") != "admin":
        return jsonify({"error": "Admin access required"}), 403
    return "Admin Access: Granted"
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-RESTful%20API-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
