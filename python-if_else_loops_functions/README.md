# Python - if/else, loops, functions

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Maitriser les structures de controle, les boucles et la definition de fonctions en Python.

---

## Objectifs d'apprentissage

- Utiliser les instructions conditionnelles `if`, `elif`, `else`
- Maitriser les boucles `while` et `for` avec `range`
- Comprendre le scope des variables
- Definir des fonctions avec parametres et valeur de retour
- Utiliser les operateurs arithmetiques et les conversions ASCII

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. Positive or negative
> **Objectif** : Determiner si un nombre aleatoire est positif, negatif ou nul

```python
#!/usr/bin/python3
import random
number = random.randint(-10, 10)
# Affiche "{number} is positive/negative/zero"
```

### 1. Last digit
> **Objectif** : Extraire et analyser le dernier chiffre d'un nombre aleatoire

```python
#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
# Analyse le dernier chiffre avec modulo
```

### 2. Print alphabet
> **Objectif** : Afficher l'alphabet en minuscules sans saut de ligne

```python
#!/usr/bin/python3
# Utilise chr() et range() pour parcourir les lettres a-z
```

### 3. Print alphabet (sans q et e)
> **Objectif** : Afficher l'alphabet en excluant certaines lettres

```python
#!/usr/bin/python3
# Filtre les lettres 'q' et 'e' dans la boucle
```

### 4. Hexadecimal
> **Objectif** : Afficher les nombres de 0 a 98 en decimal et hexadecimal

```python
#!/usr/bin/python3
# Utilise format {:x} pour la conversion hexadecimale
```

### 5. Print 00..99
> **Objectif** : Afficher les nombres de 00 a 99 avec un format a 2 chiffres

```python
#!/usr/bin/python3
# Utilise format {:02d} pour le zero-padding
```

### 6. Combinations of two digits
> **Objectif** : Afficher toutes les combinaisons uniques de deux chiffres

```python
#!/usr/bin/python3
# Double boucle avec condition pour eviter les doublons
```

### 7. islower
> **Objectif** : Verifier si un caractere est minuscule via les codes ASCII

```python
def islower(c):
    """Check if a character is lowercase."""
    return 97 <= ord(c) <= 122
```

### 8. uppercase
> **Objectif** : Convertir une chaine en majuscules sans utiliser `.upper()`

```python
def uppercase(str):
    """Print a string in uppercase."""
    # Conversion caractere par caractere via ord() et chr()
```

### 9. Print last digit
> **Objectif** : Extraire et afficher le dernier chiffre d'un nombre (gere les negatifs)

```python
def print_last_digit(number):
    """Prints the last digit of a number."""
    last_digit = abs(number) % 10
    print(last_digit, end="")
    return last_digit
```

### 10. Add
> **Objectif** : Additionner deux entiers

```python
def add(a, b):
    """Adds two integers and returns the result."""
    return a + b
```

### 11. Power
> **Objectif** : Calculer la puissance d'un nombre

```python
def pow(a, b):
    """Compute a to the power of b."""
    return a ** b
```

### 12. FizzBuzz
> **Objectif** : Implementer l'algorithme classique FizzBuzz de 1 a 100

```python
def fizzbuzz():
    """Print numbers from 1 to 100 with Fizz Buzz rules."""
    # FizzBuzz pour les multiples de 3 et 5
    # Fizz pour les multiples de 3
    # Buzz pour les multiples de 5
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20If%20Else%20Loops%20Functions-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
