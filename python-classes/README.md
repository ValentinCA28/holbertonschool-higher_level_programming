# Python - Classes

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-OOP-blueviolet.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Decouvrir la programmation orientee objet en Python a travers la construction progressive d'une classe Square.

---

## Objectifs d'apprentissage

- Comprendre les concepts de classe, objet et instance
- Utiliser les attributs prives avec le name mangling
- Implementer des properties (getter/setter) avec validation
- Definir des methodes d'instance
- Gerer les exceptions `TypeError` et `ValueError` dans les setters

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. My first square
> **Objectif** : Definir une classe vide comme point de depart

```python
class Square:
    """An empty class that defines a square."""
    pass
```

### 1. Square with size
> **Objectif** : Ajouter un attribut prive `__size` avec validation dans `__init__`

```python
class Square:
    def __init__(self, size=0):
        # Raises TypeError if size is not an integer
        # Raises ValueError if size < 0
        self.__size = size
```

### 2. Size validation
> **Objectif** : Renforcer la validation de `size` dans le constructeur

```python
class Square:
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
```

### 3. Area of a square
> **Objectif** : Calculer et retourner l'aire du carre

```python
class Square:
    def __init__(self, size=0):
        # Validation de size
        self.__size = size

    def area(self):
        """Calculate and return the area of the square."""
        return self.__size * self.__size
```

### 4. Access and update private attribute
> **Objectif** : Implementer des properties pour acceder et modifier `size` avec validation

```python
class Square:
    @property
    def size(self):
        """Get the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size with type and value validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        return self.__size ** 2
```

### 5. Printing a square
> **Objectif** : Afficher le carre avec le caractere `#` via `my_print()`

```python
class Square:
    # Properties size, area()...

    def my_print(self):
        """Print the square using the # character."""
        if self.__size == 0:
            print()
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
```

### 6. Coordinates of a square
> **Objectif** : Ajouter un attribut `position` (tuple) pour decaler l'affichage du carre

```python
class Square:
    def __init__(self, size=0, position=(0, 0)):
        self.size = size
        self.position = position

    @property
    def position(self):
        return self.__position

    @position.setter
    def position(self, value):
        """Validate position as a tuple of 2 positive integers."""
        if (not isinstance(value, tuple) or len(value) != 2
                or not all(isinstance(n, int) and n >= 0 for n in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Print the square with position offset."""
        # Vertical offset with position[1], horizontal with position[0]
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20Classes-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
