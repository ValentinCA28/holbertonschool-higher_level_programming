# Python - Object Relational Mapping

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1.svg?logo=mysql&logoColor=white)
![SQLAlchemy](https://img.shields.io/badge/ORM-SQLAlchemy-D71F00.svg?logo=sqlalchemy&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Interagir avec une base de donnees MySQL depuis Python en utilisant MySQLdb (raw SQL) puis SQLAlchemy (ORM).

---

## Objectifs d'apprentissage

- Se connecter a une base MySQL depuis Python avec MySQLdb
- Executer des requetes SQL parametrees pour eviter les injections
- Definir un modele SQLAlchemy mappe a une table MySQL
- Effectuer des operations CRUD avec l'ORM SQLAlchemy
- Comprendre la difference entre requetes brutes et ORM

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |
| ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) | 8.0 | Base de donnees relationnelle | `sudo apt install mysql-server` |
| ![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?logo=sqlalchemy&logoColor=white) | 2.x | ORM Python | `pip install sqlalchemy` |
| ![MySQLdb](https://img.shields.io/badge/MySQLdb-4479A1?logo=mysql&logoColor=white) | 2.x | Connecteur MySQL natif | `pip install mysqlclient` |

---

## Taches

### 0. Get all states (raw SQL)
> **Objectif** : Lister tous les etats depuis MySQL avec MySQLdb

```python
#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa"""
import MySQLdb, sys

db = MySQLdb.connect(host="localhost", port=3306,
                     user=sys.argv[1], passwd=sys.argv[2], db=sys.argv[3])
cursor = db.cursor()
cursor.execute("SELECT * FROM states ORDER BY id ASC")
```

### 1. Filter states
> **Objectif** : Filtrer les etats dont le nom commence par N

```python
cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")
```

### 2. Filter states by user input
> **Objectif** : Filtrer les etats par un argument utilisateur (vulnerable aux injections)

```python
cursor.execute("SELECT * FROM states WHERE name='{}' ORDER BY id ASC"
               .format(sys.argv[4]))
```

### 3. SQL Injection safe
> **Objectif** : Utiliser des requetes parametrees pour se proteger des injections SQL

```python
cursor.execute("SELECT * FROM states WHERE name=%s ORDER BY id ASC",
               (sys.argv[4],))
# Requete parametree : la valeur est echappee automatiquement
```

### 4. Cities by states (JOIN)
> **Objectif** : Lister toutes les villes avec leur etat via un JOIN

```python
cursor.execute(
    "SELECT cities.id, cities.name, states.name "
    "FROM cities JOIN states ON cities.state_id = states.id "
    "ORDER BY cities.id ASC"
)
```

### 5. Filter cities by state
> **Objectif** : Lister les villes d'un etat specifique (safe SQL)

```python
cursor.execute(
    "SELECT cities.name FROM cities JOIN states ON cities.state_id = states.id "
    "WHERE states.name=%s ORDER BY cities.id ASC",
    (sys.argv[4],)
)
```

### 6. State model definition
> **Objectif** : Definir le modele SQLAlchemy `State` mappe a la table `states`

```python
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class State(Base):
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, autoincrement=True, nullable=False)
    name = Column(String(128), nullable=False)
```

### 7. All states via ORM
> **Objectif** : Lister tous les objets State avec SQLAlchemy

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State

engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format(...))
Session = sessionmaker(bind=engine)
session = Session()
for state in session.query(State).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
```

### 8. First state
> **Objectif** : Afficher le premier objet State ou "Nothing"

```python
state = session.query(State).order_by(State.id).first()
if state:
    print("{}: {}".format(state.id, state.name))
else:
    print("Nothing")
```

### 9. Contains `a`
> **Objectif** : Filtrer les etats contenant la lettre `a` avec l'ORM

```python
for state in session.query(State).filter(
        State.name.like('%a%')).order_by(State.id).all():
    print("{}: {}".format(state.id, state.name))
```

### 10. Get a state
> **Objectif** : Rechercher un etat par nom exact et afficher son id

```python
state = session.query(State).filter(State.name == sys.argv[4]).first()
if state is None:
    print("Not found")
else:
    print(state.id)
```

### 11. Add a new state
> **Objectif** : Inserer un nouvel objet State via l'ORM

```python
new_state = State(name="Louisiana")
session.add(new_state)
session.commit()
print(new_state.id)
```

### 12. Update a state
> **Objectif** : Modifier le nom d'un etat existant via l'ORM

```python
state = session.query(State).filter(State.id == 2).first()
if state:
    state.name = "New Mexico"
    session.commit()
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20ORM-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
