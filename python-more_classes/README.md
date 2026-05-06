# Python - More Classes and Objects

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-OOP-blueviolet.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Approfondir la POO en Python avec les methodes speciales, les class/static methods et les attributs de classe, via la construction progressive d'une classe Rectangle.

---

## Objectifs d'apprentissage

- Implementer `__str__`, `__repr__` et `__del__`
- Differencier attributs d'instance et attributs de classe
- Utiliser `@classmethod` et `@staticmethod`
- Compter les instances avec un attribut de classe
- Personnaliser le symbole d'affichage avec `print_symbol`

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. Simple Rectangle
> **Objectif** : Definir une classe Rectangle vide

```python
class Rectangle:
    """An empty class that represents a rectangle."""
    pass
```

### 1. Real definition of a rectangle
> **Objectif** : Ajouter les properties `width` et `height` avec validation

```python
class Rectangle:
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        # Raises TypeError/ValueError
        self.__width = value
```

### 2. Area and Perimeter
> **Objectif** : Calculer l'aire et le perimetre du rectangle

```python
def area(self):
    return self.__width * self.__height

def perimeter(self):
    if self.__width == 0 or self.__height == 0:
        return 0
    return 2 * (self.__width + self.__height)
```

### 3. String representation
> **Objectif** : Implementer `__str__` pour afficher le rectangle avec `#`

```python
def __str__(self):
    """Return rectangle drawn with '#' characters."""
    if self.__width == 0 or self.__height == 0:
        return ""
    return "\n".join(["#" * self.__width for _ in range(self.__height)])
```

### 4. Reproducible representation
> **Objectif** : Implementer `__repr__` pour obtenir une representation recreable de l'objet

```python
def __repr__(self):
    return f"Rectangle({self.__width}, {self.__height})"
```

### 5. Detect instance deletion
> **Objectif** : Afficher un message lors de la suppression d'une instance avec `__del__`

```python
def __del__(self):
    """Print 'Bye rectangle...' when instance is deleted."""
    print("Bye rectangle...")
```

### 6. How many instances
> **Objectif** : Compter les instances actives avec un attribut de classe

```python
class Rectangle:
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        # ...
        Rectangle.number_of_instances += 1

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
```

### 7. Change representation
> **Objectif** : Utiliser `print_symbol` pour personnaliser le caractere d'affichage

```python
class Rectangle:
    print_symbol = "#"

    def __str__(self):
        # Utilise str(self.print_symbol) au lieu de "#"
        return "\n".join([str(self.print_symbol) * self.__width
                          for _ in range(self.__height)])
```

### 8. Compare rectangles
> **Objectif** : Comparer deux rectangles par leur aire avec une methode statique

```python
@staticmethod
def bigger_or_equal(rect_1, rect_2):
    """Return the biggest rectangle based on area."""
    if not isinstance(rect_1, Rectangle):
        raise TypeError("rect_1 must be an instance of Rectangle")
    if not isinstance(rect_2, Rectangle):
        raise TypeError("rect_2 must be an instance of Rectangle")
    if rect_1.area() >= rect_2.area():
        return rect_1
    return rect_2
```

### 9. A square is a rectangle
> **Objectif** : Creer un carre via une methode de classe

```python
@classmethod
def square(cls, size=0):
    """Create a new Rectangle with width == height == size."""
    return cls(size, size)
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20More%20Classes-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
