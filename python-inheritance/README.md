# Python - Inheritance

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-Inheritance-blueviolet.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Maitriser l'heritage en Python : classes de base, sous-classes, validation de types et hierarchie de geometrie.

---

## Objectifs d'apprentissage

- Utiliser `isinstance`, `issubclass` et `type` pour verifier les types
- Comprendre l'heritage simple et la surcharge de methodes
- Utiliser `super()` pour appeler les methodes de la classe parente
- Definir une classe de base avec validation (`BaseGeometry`)
- Construire une hierarchie de classes : BaseGeometry > Rectangle > Square

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. Lookup
> **Objectif** : Lister les attributs et methodes disponibles d'un objet

```python
def lookup(obj):
    """Returns the list of available attributes and methods of an object."""
    return dir(obj)
```

### 1. My list
> **Objectif** : Creer une sous-classe de `list` avec une methode de tri

```python
class MyList(list):
    def print_sorted(self):
        """Prints the list, but sorted (ascending sort)."""
        print(sorted(self))
```

### 2. Exact same object
> **Objectif** : Verifier si un objet est exactement une instance d'une classe

```python
def is_same_class(obj, a_class):
    """Check if obj is exactly an instance of a_class."""
    return isinstance(obj, a_class)
```

### 3. Same class or inherit from
> **Objectif** : Verifier si un objet est une instance directe ou heritee

```python
def is_kind_of_class(obj, a_class):
    """Check if obj is an instance of, or inherited from, a_class."""
    return isinstance(obj, a_class)
```

### 4. Only sub class of
> **Objectif** : Verifier si un objet herite d'une classe (sans etre une instance directe)

```python
def inherits_from(obj, a_class):
    """Check if obj is an instance of a class that inherited from a_class."""
    return isinstance(obj, a_class) and type(obj) is not a_class
```

### 5. Geometry module
> **Objectif** : Definir une classe de base vide pour la geometrie

```python
class BaseGeometry:
    """An empty base geometry class."""
    pass
```

### 6. Improve Geometry
> **Objectif** : Ajouter une methode `area()` non implementee

```python
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
```

### 7. Integer validator
> **Objectif** : Ajouter une methode de validation pour les entiers positifs

```python
class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validate that value is a positive integer."""
        if not isinstance(value, int) or isinstance(value, bool):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
```

### 8. Rectangle (inherits from BaseGeometry)
> **Objectif** : Creer une classe Rectangle qui herite de BaseGeometry

```python
class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
```

### 9. Full Rectangle
> **Objectif** : Ajouter `area()` et `__str__` au Rectangle

```python
class Rectangle(BaseGeometry):
    def area(self):
        return self.__width * self.__height

    def __str__(self):
        return "[Rectangle] {}/{}".format(self.__width, self.__height)
```

### 10. Square #1
> **Objectif** : Creer une classe Square qui herite de Rectangle

```python
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
```

### 11. Square #2
> **Objectif** : Ajouter `__str__` au Square

```python
class Square(Rectangle):
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        return f"[Square] {self.__size}/{self.__size}"
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20Inheritance-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
