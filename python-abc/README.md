# Python - Abstract Classes and Interfaces

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![OOP](https://img.shields.io/badge/Concept-ABC%20%26%20Interfaces-blueviolet.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Explorer les classes abstraites, le duck typing, l'heritage multiple et les mixins en Python.

---

## Objectifs d'apprentissage

- Definir des classes abstraites avec le module `abc` (ABC, abstractmethod)
- Comprendre et appliquer le duck typing
- Surcharger les methodes de `list` pour creer une liste verbose
- Implementer un iterateur personnalise avec compteur
- Utiliser l'heritage multiple et comprendre le MRO (Method Resolution Order)
- Creer des mixins pour la composition de comportements

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0. Abstract Animal Class
> **Objectif** : Definir une classe abstraite `Animal` avec une methode `sound()` a implementer

```python
from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
```

### 1. Duck Typing - Shapes
> **Objectif** : Utiliser le duck typing avec des formes geometriques abstraites

```python
from abc import ABC, abstractmethod
import math

class Shape(ABC):
    @abstractmethod
    def area(self):
        pass

    @abstractmethod
    def perimeter(self):
        pass

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
    def perimeter(self):
        return math.pi * (2 * self.radius)

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.height * self.width
    def perimeter(self):
        return (self.height + self.width) * 2

def shape_info(shape):
    """Print area and perimeter using duck typing."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
```

### 2. VerboseList
> **Objectif** : Sous-classer `list` pour notifier chaque modification

```python
class VerboseList(list):
    def append(self, item):
        super().append(item)
        print("Added [{}] to the list".format(item))

    def remove(self, item):
        super().remove(item)
        print("Removed [{}] from the list".format(item))

    def extend(self, item):
        super().extend(item)
        print("Extended [{}] from the list".format(len(item)))

    def pop(self, index=None):
        # Notifie l'element retire avant de le supprimer
```

### 3. CountedIterator
> **Objectif** : Creer un iterateur qui compte le nombre d'elements iteres

```python
class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)
        self._count = 0

    def __next__(self):
        item = next(self._iterator)
        self._count += 1
        return item

    def get_count(self):
        return self._count
```

### 4. FlyingFish - Multiple Inheritance
> **Objectif** : Demonstrer l'heritage multiple avec Fish et Bird

```python
from abc import ABC, abstractmethod

class Fish(ABC):
    @abstractmethod
    def swim(self): pass
    @abstractmethod
    def habitat(self): pass

class Bird(ABC):
    @abstractmethod
    def fly(self): pass
    @abstractmethod
    def habitat(self): pass

class FlyingFish(Fish, Bird):
    def swim(self):
        print("The flying fish is swimming!")
    def fly(self):
        print("The flying fish is soaring!")
    def habitat(self):
        print("The flying fish lives both in water and the sky!")
```

### 5. Dragon - Mixins
> **Objectif** : Utiliser des mixins pour combiner des comportements independants

```python
class SwimMixin:
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    def roar(self):
        print("The dragon roars!")
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20ABC-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
