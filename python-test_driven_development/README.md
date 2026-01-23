# 🧪 Python - Test-driven Development

## 📋 Description

Ce projet explore le **Test-Driven Development (TDD)**, une méthodologie de développement où les tests sont écrits avant le code de production. Vous apprendrez à écrire des tests doctests et unittest, à valider les entrées, et à créer une documentation interactive pour vos fonctions.

## 🎯 Objectifs d'Apprentissage

À la fin de ce projet, vous serez capable d'expliquer :

- Pourquoi les tests Python sont géniaux
- Qu'est-ce qu'une docstring interactive
- Comment écrire des doctests
- Comment trouver les cas limites (edge cases)
- L'importance de tester votre code avant de l'implémenter
- Comment écrire des tests unitaires avec unittest
- Comment documenter vos modules, classes et fonctions
- Les options de base pour tester votre code
- Comment collaborer sur des fichiers de test

## 📚 Ressources

- [doctest — Test interactive Python examples](https://docs.python.org/3/library/doctest.html)
- [doctest – Testing through documentation](https://pymotw.com/3/doctest/)
- [Unit Tests in Python](https://www.youtube.com/watch?v=6tNS--WetLI)
- [unittest — Unit testing framework](https://docs.python.org/3/library/unittest.html)

## 📂 Structure du Projet

```
python-test_driven_development/
├── README.md
├── 0-add_integer.py            # Fonction d'addition d'entiers
├── 2-matrix_divided.py         # Division de tous les éléments d'une matrice
├── 3-say_my_name.py            # Afficher un nom
├── 4-print_square.py           # Dessiner un carré avec #
├── 5-text_indentation.py       # Indentation de texte
├── 6-max_integer.py            # Trouver le maximum d'une liste
└── tests/
    ├── 0-add_integer.txt       # Tests doctests pour add_integer
    ├── 2-matrix_divided.txt    # Tests doctests pour matrix_divided
    ├── 3-say_my_name.txt       # Tests doctests pour say_my_name
    ├── 4-print_square.txt      # Tests doctests pour print_square
    ├── 5-text_indentation.txt  # Tests doctests pour text_indentation
    └── 6-max_integer_test.py   # Tests unittest pour max_integer
```

## 💻 Fonctions Implémentées

### 0. Integers addition
**Fichier:** `0-add_integer.py`  
**Tests:** `tests/0-add_integer.txt`

Fonction qui additionne deux entiers.

**Prototype:** `def add_integer(a, b=98):`

**Fonctionnalités:**
- `a` et `b` doivent être des entiers ou des floats
- `a` et `b` sont d'abord convertis en entiers si ce sont des floats
- Retourne un entier : l'addition de `a` et `b`
- Lève une `TypeError` si `a` ou `b` ne sont ni entiers ni floats

**Exemple:**
```python
>>> add_integer = __import__('0-add_integer').add_integer
>>> add_integer(1, 2)
3
>>> add_integer(100, -2)
98
>>> add_integer(2)
100
```

---

### 1. Divide a matrix
**Fichier:** `2-matrix_divided.py`  
**Tests:** `tests/2-matrix_divided.txt`

Fonction qui divise tous les éléments d'une matrice.

**Prototype:** `def matrix_divided(matrix, div):`

**Fonctionnalités:**
- `matrix` doit être une liste de listes d'entiers ou de floats
- Toutes les lignes de la matrice doivent avoir la même taille
- `div` doit être un nombre (entier ou float)
- `div` ne peut pas être égal à 0
- Retourne une nouvelle matrice avec tous les éléments divisés par `div`, arrondis à 2 décimales
- Lève des `TypeError` et `ZeroDivisionError` appropriés

**Exemple:**
```python
>>> matrix_divided = __import__('2-matrix_divided').matrix_divided
>>> matrix = [[1, 2, 3], [4, 5, 6]]
>>> print(matrix_divided(matrix, 3))
[[0.33, 0.67, 1.0], [1.33, 1.67, 2.0]]
```

---

### 2. Say my name
**Fichier:** `3-say_my_name.py`  
**Tests:** `tests/3-say_my_name.txt`

Fonction qui affiche "My name is <first name> <last name>".

**Prototype:** `def say_my_name(first_name, last_name=""):`

**Fonctionnalités:**
- `first_name` et `last_name` doivent être des chaînes de caractères
- Lève une `TypeError` si ce n'est pas le cas

**Exemple:**
```python
>>> say_my_name = __import__('3-say_my_name').say_my_name
>>> say_my_name("John", "Smith")
My name is John Smith
>>> say_my_name("Bob")
My name is Bob 
```

---

### 3. Print square
**Fichier:** `4-print_square.py`  
**Tests:** `tests/4-print_square.txt`

Fonction qui affiche un carré avec le caractère `#`.

**Prototype:** `def print_square(size):`

**Fonctionnalités:**
- `size` est la taille du carré
- `size` doit être un entier
- Si `size` est inférieur à 0, lève une `ValueError`
- Si `size` est un float et inférieur à 0, lève une `TypeError`

**Exemple:**
```python
>>> print_square = __import__('4-print_square').print_square
>>> print_square(4)
####
####
####
####
```

---

### 4. Text indentation
**Fichier:** `5-text_indentation.py`  
**Tests:** `tests/5-text_indentation.txt`

Fonction qui affiche un texte avec 2 nouvelles lignes après chaque `.`, `?` et `:`.

**Prototype:** `def text_indentation(text):`

**Fonctionnalités:**
- `text` doit être une chaîne de caractères
- Pas d'espace au début ou à la fin de chaque ligne imprimée
- Lève une `TypeError` si `text` n'est pas une chaîne

**Exemple:**
```python
>>> text_indentation = __import__('5-text_indentation').text_indentation
>>> text_indentation("Hello? How are you: Fine.")
Hello?

How are you:

Fine.
```

---

### 5. Max integer - Unittest
**Fichier:** `6-max_integer.py`  
**Tests:** `tests/6-max_integer_test.py`

Fonction qui trouve et retourne la valeur maximale dans une liste d'entiers.

**Prototype:** `def max_integer(list=[]):`

**Fonctionnalités:**
- Retourne le plus grand entier de la liste
- Retourne `None` si la liste est vide
- Tests implémentés avec le module `unittest`

**Exemple:**
```python
>>> max_integer = __import__('6-max_integer').max_integer
>>> max_integer([1, 2, 3, 4])
4
>>> max_integer([1, 3, 4, 2])
4
```

---

## 🛠️ Utilisation

### Prérequis
- Python 3.12 ou supérieur
- Module `doctest` (inclus avec Python)
- Module `unittest` (inclus avec Python)

### Exécution des Tests

#### Tests Doctests
```bash
# Exécuter tous les tests doctests d'un fichier
python3 -m doctest -v tests/0-add_integer.txt

# Exécuter tous les tests doctests du projet
python3 -m doctest -v tests/*.txt
```

#### Tests Unittest
```bash
# Exécuter tous les tests unittest
python3 -m unittest tests.6-max_integer_test

# Exécuter tous les tests avec plus de détails
python3 -m unittest -v tests.6-max_integer_test

# Exécuter un test spécifique
python3 -m unittest tests.6-max_integer_test.TestMaxInteger.test_empty_list
```

### Exécution des Fonctions
```bash
# Tester une fonction directement
python3 -c 'print(__import__("0-add_integer").add_integer(1, 2))'

# Utiliser un fichier main
python3 0-main.py
```

## ✅ Exigences

### Python Scripts
- Tous les fichiers doivent être exécutables
- La première ligne de tous les fichiers doit être exactement `#!/usr/bin/python3`
- Le code doit utiliser le style **pycodestyle** (version 2.7.*)
- Tous les fichiers doivent se terminer par une nouvelle ligne
- Tous les modules doivent avoir une documentation
- Toutes les fonctions doivent avoir une documentation avec docstrings

### Python Test Cases
- Tous les fichiers de test doivent être dans le dossier `tests`
- Tous les fichiers de test doivent être des fichiers texte (extension `.txt`)
- Tous les tests doivent être exécutés via : `python3 -m doctest ./tests/*`
- Tous les modules doivent avoir une documentation
- Toutes les fonctions doivent avoir une documentation

### Documentation
```bash
# Vérifier la documentation d'un module
python3 -c 'print(__import__("0-add_integer").__doc__)'

# Vérifier la documentation d'une fonction
python3 -c 'print(__import__("0-add_integer").add_integer.__doc__)'
```

## 🚀 Concepts Clés

### Test-Driven Development (TDD)
Le TDD suit le cycle **Red-Green-Refactor** :

1. **Red** : Écrire un test qui échoue
2. **Green** : Écrire le code minimal pour faire passer le test
3. **Refactor** : Améliorer le code sans casser les tests

### Doctests
Tests intégrés dans les docstrings des fonctions :

```python
def add_integer(a, b=98):
    """
    Add two integers.
    
    >>> add_integer(1, 2)
    3
    >>> add_integer(100, -2)
    98
    """
    return int(a) + int(b)
```

### Unittest
Framework de tests unitaires :

```python
import unittest

class TestAddInteger(unittest.TestCase):
    def test_add_two_integers(self):
        self.assertEqual(add_integer(1, 2), 3)
    
    def test_add_with_default(self):
        self.assertEqual(add_integer(2), 100)
```

## 🎯 Cas de Test à Considérer

Lors de l'écriture de tests, pensez à tester :

1. **Cas normaux** : Entrées valides typiques
2. **Cas limites (edge cases)** :
   - Listes vides
   - Valeurs nulles (0, None)
   - Un seul élément
   - Valeurs négatives
   - Très grandes valeurs
3. **Cas d'erreur** :
   - Types incorrects
   - Division par zéro
   - Valeurs hors limites
4. **Cas spéciaux** :
   - Float vs Integer
   - Chaînes vides
   - Matrices irrégulières

## 📖 Bonnes Pratiques

1. **Écrivez les tests d'abord** : TDD vous force à réfléchir aux cas d'usage
2. **Tests indépendants** : Chaque test doit pouvoir s'exécuter seul
3. **Nommage clair** : `test_add_two_positive_integers` est mieux que `test1`
4. **Un assert par test** : Facilite l'identification des échecs
5. **Couvrez les cas limites** : C'est là que les bugs se cachent
6. **Documentation** : Les tests servent aussi de documentation

## 🎓 Auteur

Projet réalisé dans le cadre du cursus **Holberton School**

---

<p align="center">
  <strong>Python - Test-driven Development</strong>
  <br>
  Écrire des tests avant le code pour un développement de qualité
  <br>
  © 2026 - Holberton School
</p>
