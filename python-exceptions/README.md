# 🐍 Python - Exceptions

## 📋 Description

Ce projet explore la gestion des exceptions en Python, un concept fondamental pour écrire du code robuste et fiable. Vous apprendrez à anticiper et gérer les erreurs de manière élégante, à utiliser les blocs `try`/`except`/`finally`, et à lever vos propres exceptions.

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Pourquoi la programmation en Python est géniale
- La différence entre les erreurs et les exceptions
- Ce qu'est une exception et comment l'utiliser
- Quand utiliser les exceptions
- Comment gérer correctement les exceptions
- Le but d'attraper les exceptions
- Comment lever une exception built-in
- Quand implémenter une fonction de nettoyage après une exception

## 📚 Ressources

- [Errors and Exceptions](https://docs.python.org/3/tutorial/errors.html)
- [Learn to Program 11 Static & Exception Handling](https://www.youtube.com/watch?v=7vbgD-3s-w4)

## 📂 Structure du Projet

```
python-exceptions/
├── README.md
├── 0-safe_print_list.py        # Imprimer x éléments d'une liste en toute sécurité
├── 1-safe_print_integer.py     # Imprimer un entier avec "{:d}".format()
├── 2-safe_print_list_integers.py  # Imprimer les x premiers entiers d'une liste
├── 3-safe_print_division.py    # Diviser deux entiers et imprimer le résultat
├── 4-list_division.py          # Diviser élément par élément deux listes
├── 5-raise_exception.py        # Lever une exception de type
├── 6-raise_exception_msg.py    # Lever une exception nommée avec un message
└── tests/                      # Tests unitaires (à créer)
```

## 💻 Fonctions Implémentées

### 0. Safe list printing
**Fichier:** `0-safe_print_list.py`

Fonction qui imprime x éléments d'une liste de manière sécurisée.

**Prototype:** `def safe_print_list(my_list=[], x=0):`

**Fonctionnalités:**
- Utilise `try`/`except` pour gérer les erreurs d'index
- Imprime les éléments sans cracher si la liste est trop courte
- Retourne le nombre réel d'éléments imprimés

**Exemple:**
```python
my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list(my_list, 2)  # Imprime: 12
print("nb_print: {:d}".format(nb_print))  # Affiche: nb_print: 2
```

---

### 1. Safe printing of an integers list
**Fichier:** `1-safe_print_integer.py`

Fonction qui imprime un entier avec `"{:d}".format()`.

**Prototype:** `def safe_print_integer(value):`

**Fonctionnalités:**
- Utilise `try`/`except` pour gérer les erreurs de formatage
- Retourne `True` si la valeur est un entier et a été imprimée correctement
- Retourne `False` sinon

---

### 2. Print and count integers
**Fichier:** `2-safe_print_list_integers.py`

Fonction qui imprime les x premiers entiers d'une liste.

**Prototype:** `def safe_print_list_integers(my_list=[], x=0):`

**Fonctionnalités:**
- Parcourt les x premiers éléments de la liste
- Imprime uniquement les entiers
- Ignore les autres types (str, float, etc.)
- Retourne le nombre réel d'entiers imprimés

---

### 3. Integers division with debug
**Fichier:** `3-safe_print_division.py`

Fonction qui divise deux entiers et imprime le résultat.

**Prototype:** `def safe_print_division(a, b):`

**Fonctionnalités:**
- Utilise `try`/`except` pour gérer la division par zéro
- Utilise `finally` pour toujours imprimer le résultat
- Retourne la valeur de la division ou `None` en cas d'erreur

**Exemple:**
```python
result = safe_print_division(10, 2)
# Affiche: Inside result: 5.0
print("{:d} / {:d} = {}".format(10, 2, result))
# Affiche: 10 / 2 = 5.0
```

---

### 4. Divide a list
**Fichier:** `4-list_division.py`

Fonction qui divise élément par élément deux listes.

**Prototype:** `def list_division(my_list_1, my_list_2, list_length):`

**Fonctionnalités:**
- Gère la division par zéro
- Gère les types incorrects (non numériques)
- Gère les listes trop courtes (out of range)
- Retourne une nouvelle liste avec tous les résultats
- La nouvelle liste est de longueur `list_length`

---

### 5. Raise exception
**Fichier:** `5-raise_exception.py`

Fonction qui lève une exception de type.

**Prototype:** `def raise_exception():`

**Fonctionnalités:**
- Lève une `TypeError`

---

### 6. Raise a message
**Fichier:** `6-raise_exception_msg.py`

Fonction qui lève une exception nommée avec un message.

**Prototype:** `def raise_exception_msg(message=""):`

**Fonctionnalités:**
- Lève une `NameError` avec un message personnalisé

---

## 🛠️ Utilisation

### Prérequis
- Python 3.12 ou supérieur
- Système d'exploitation compatible (Linux/Unix recommandé)

### Exécution
```bash
# Exemple pour tester safe_print_list
python3 0-main.py

# Exemple pour tester safe_print_division
python3 3-main.py
```

### Tests
```bash
# Exécuter tous les tests unitaires
python3 -m unittest discover tests

# Exécuter un test spécifique
python3 -m unittest tests.0-safe_print_list_test
```

## ✅ Exigences

### Python Scripts
- Tous les fichiers doivent être exécutables
- La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`
- Le code doit utiliser le style **pycodestyle** (version 2.7.*)
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Tous les modules doivent avoir une documentation
- Tous les fonctions doivent avoir une documentation

### Documentation
```bash
# Vérifier la documentation d'un module
python3 -c 'print(__import__("0-safe_print_list").__doc__)'

# Vérifier la documentation d'une fonction
python3 -c 'print(__import__("0-safe_print_list").safe_print_list.__doc__)'
```

## 🚀 Concepts Clés

### Try/Except
```python
try:
    # Code qui peut lever une exception
    result = 10 / 0
except ZeroDivisionError:
    # Gestion de l'exception
    result = None
```

### Try/Except/Finally
```python
try:
    result = a / b
except ZeroDivisionError:
    result = None
finally:
    # Toujours exécuté, qu'il y ait une exception ou non
    print("Inside result: {}".format(result))
```

### Lever une Exception
```python
# Lever une exception built-in
raise TypeError("a must be an integer")

# Lever une exception avec un message personnalisé
raise NameError(message)
```

## 📖 Bonnes Pratiques

1. **Soyez spécifique** : Attrapez des exceptions spécifiques plutôt que toutes les exceptions
2. **Ne masquez pas les erreurs** : Ne pas utiliser `except: pass` sans raison
3. **Utilisez finally pour le nettoyage** : Fermez les fichiers, les connexions, etc.
4. **Documentez les exceptions** : Indiquez quelles exceptions peuvent être levées
5. **N'utilisez pas les exceptions pour le contrôle de flux** : Utilisez-les pour les erreurs

## 🎓 Auteur

Projet réalisé dans le cadre du cursus **Holberton School**

---

<p align="center">
  <strong>Python - Exceptions</strong>
  <br>
  Apprendre à gérer les erreurs de manière élégante
  <br>
  © 2026 - Holberton School
</p>
