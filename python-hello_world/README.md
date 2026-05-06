# Python - Hello, World

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Introduction a la programmation Python : affichage, variables, f-strings, slicing et philosophie du langage.

---

## Objectifs d'apprentissage

- Utiliser `print` pour afficher du texte et des variables
- Formater des nombres et des chaines avec les f-strings
- Manipuler les chaines de caracteres : slicing, concatenation, repetition
- Comprendre l'indexation positive et negative en Python
- Decouvrir le Zen of Python

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. Print a specific string
> **Objectif** : Afficher une chaine exacte avec `print`

```python
#!/usr/bin/python3
print("\"Programming is like building a multilingual puzzle")
```

### 1. Print integer with f-string
> **Objectif** : Utiliser les f-strings pour formater un entier dans une phrase

```python
#!/usr/bin/python3
number = 98
print(f"{number} Battery street")
```

### 2. Print float with precision
> **Objectif** : Formater un float avec une precision de 2 decimales

```python
#!/usr/bin/python3
number = 3.14159
print(f"Float: {number:.2f}")
```

### 3. Print string multiple times
> **Objectif** : Repeter une chaine et extraire une sous-chaine par slicing

```python
#!/usr/bin/python3
str = "Holberton School"
print(f"{str * 3}")
print(f"{str[:9]}")
```

### 4. Concatenation with f-string
> **Objectif** : Concatener deux variables dans une phrase formatee

```python
#!/usr/bin/python3
str1 = "Holberton"
str2 = "School"
str1 = f"Welcome to {str1} {str2}!"
print(str1)
```

### 5. String slicing - edges
> **Objectif** : Extraire les premiers, derniers et caracteres du milieu d'une chaine

```python
#!/usr/bin/python3
word = "Holberton"
word_first_3 = word[:3]
word_last_2 = word[-2:]
middle_word = word[1:-1]
```

### 6. Concat edges
> **Objectif** : Construire une nouvelle phrase en extrayant des portions d'une chaine longue

```python
#!/usr/bin/python3
str = "Python is an interpreted, interactive, object-oriented programming language..."
str = str[39:67] + str[107:112] + str[0:6]
# Concatenation par slicing
```

### 7. Easter egg - Zen of Python
> **Objectif** : Decouvrir les principes fondateurs de Python via le module `this`

```python
#!/usr/bin/python3
import this
# Affiche le Zen of Python
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20Hello%20World-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
