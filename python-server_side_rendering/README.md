# Python - Server Side Rendering

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Framework-Flask-000000.svg?logo=flask&logoColor=white)
![Jinja2](https://img.shields.io/badge/Template-Jinja2-B41717.svg?logo=jinja&logoColor=white)
![SQLite](https://img.shields.io/badge/Database-SQLite-003B57.svg?logo=sqlite&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Construire des applications web dynamiques avec Flask, Jinja2 et des sources de donnees multiples (JSON, CSV, SQLite).

---

## Objectifs d'apprentissage

- Generer des fichiers a partir de templates textuels (string templating)
- Creer des routes Flask et servir des templates Jinja2
- Utiliser les boucles et conditions dans les templates
- Lire des donnees depuis des fichiers JSON, CSV et une base SQLite
- Filtrer des produits par source de donnees et par identifiant

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |
| ![Flask](https://img.shields.io/badge/Flask-000000?logo=flask&logoColor=white) | 3.x | Framework web | `pip install flask` |
| ![SQLite](https://img.shields.io/badge/SQLite-003B57?logo=sqlite&logoColor=white) | 3.x | Base de donnees embarquee | Inclus avec Python |

---

## Taches

### 0. Generating Invitations
> **Objectif** : Generer des fichiers d'invitation personnalises a partir d'un template et d'une liste de participants

```python
def generate_invitations(template, attendees):
    """Generate personalized invitation files from a template and attendees.

    Args:
        template: A string containing placeholders like {name}, {event_title}.
        attendees: A list of dictionaries with attendee data.
    """
    # Remplace les placeholders par les valeurs, "N/A" si absent
    # Genere un fichier output_N.txt par participant
```

### 1. Basic Flask with Jinja
> **Objectif** : Creer une application Flask servant des pages HTML via Jinja2

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')
```

### 2. Dynamic Templates with Logic
> **Objectif** : Utiliser des boucles Jinja2 pour afficher une liste d'items depuis un fichier JSON

```python
@app.route('/items')
def items():
    with open('items.json', 'r') as f:
        data = json.load(f)
    items_list = data.get("items", [])
    return render_template('items.html', items=items_list)
```

### 3. Multiple Data Sources
> **Objectif** : Afficher des produits depuis JSON ou CSV selon un parametre de requete

```python
@app.route('/products')
def products():
    source = request.args.get('source')    # 'json' ou 'csv'
    product_id = request.args.get('id', type=int)
    # Lecture depuis la source appropriee
    # Filtrage optionnel par id

def read_json():
    """Read product data from JSON file."""
    # ...

def read_csv():
    """Read product data from CSV file."""
    # Utilise csv.DictReader pour parser le fichier
```

### 4. Database Integration
> **Objectif** : Ajouter SQLite comme troisieme source de donnees

```python
import sqlite3

@app.route('/products')
def products():
    source = request.args.get('source')  # 'json', 'csv' ou 'sql'
    # ...

def read_sql():
    """Read product data from SQLite database."""
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, category, price FROM Products")
    rows = cursor.fetchall()
    conn.close()
    return [{"id": r[0], "name": r[1], "category": r[2], "price": r[3]}
            for r in rows]
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20Server%20Side%20Rendering-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
