<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://www.holbertonschool.com/holberton-logo.png" alt="Holberton School logo"></a>
</p>

<h3 align="center">Python - More Data Structures: Set, Dictionary</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Un projet Holberton School pour maîtriser les structures de données avancées en Python : sets et dictionaries.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Exercises](#exercises)
- [Learning Objectives](#learning_objectives)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Ce projet fait partie du programme **Holberton School** et explore les structures de données avancées en Python. À travers 13 exercices progressifs, nous apprenons à manipuler efficacement les **sets** (ensembles) et les **dictionaries** (dictionnaires), deux structures fondamentales pour l'écriture de code Python performant et pythonique.

Le projet couvre des concepts allant de la manipulation basique de matrices et de listes jusqu'à des opérations plus complexes comme la conversion de chiffres romains en entiers, en passant par l'utilisation de fonctions de haut niveau comme `map`, `reduce` et `filter`.

## 🏁 Getting Started <a name = "getting_started"></a>

Ces instructions vous permettront d'obtenir une copie du projet et de l'exécuter sur votre machine locale à des fins de développement et de test.

### Prerequisites

Pour exécuter ce projet, vous aurez besoin de :

```
Python 3.x
pycodestyle (pour vérifier le style de code)
```

### Installation

Clonez le repository :

```bash
git clone https://github.com/votre-username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-more_data_structures
```

Vérifiez votre version de Python :

```bash
python3 --version
```

## 🎈 Usage <a name="usage"></a>

Chaque fichier contient une fonction qui peut être importée et utilisée dans vos programmes Python :

### Exemple 1 : Square Matrix

```python
#!/usr/bin/python3
square_matrix_simple = __import__('0-square_matrix_simple').square_matrix_simple

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
# Output: [[1, 4, 9], [16, 25, 36], [49, 64, 81]]
```

### Exemple 2 : Roman to Integer

```python
#!/usr/bin/python3
roman_to_int = __import__('12-roman_to_int').roman_to_int

print(roman_to_int("MCMXCIV"))  # Output: 1994
print(roman_to_int("MMXXIV"))   # Output: 2024
```

### Exemple 3 : Best Score

```python
#!/usr/bin/python3
best_score = __import__('10-best_score').best_score

scores = {"Alice": 95, "Bob": 87, "Charlie": 98, "Diana": 92}
print(best_score(scores))  # Output: Charlie
```

## 📚 Exercises <a name = "exercises"></a>

| Fichier | Description |
|---------|-------------|
| `0-square_matrix_simple.py` | Calcule le carré de tous les entiers d'une matrice |
| `1-search_replace.py` | Remplace toutes les occurrences d'un élément dans une liste |
| `2-uniq_add.py` | Additionne tous les entiers uniques d'une liste |
| `3-common_elements.py` | Retourne un ensemble d'éléments communs à deux ensembles |
| `4-only_diff_elements.py` | Retourne un ensemble d'éléments présents dans un seul ensemble |
| `5-number_keys.py` | Retourne le nombre de clés dans un dictionnaire |
| `6-print_sorted_dictionary.py` | Affiche un dictionnaire trié par ordre alphabétique des clés |
| `7-update_dictionary.py` | Remplace ou ajoute une clé/valeur dans un dictionnaire |
| `8-simple_delete.py` | Supprime une clé dans un dictionnaire |
| `9-multiply_by_2.py` | Retourne un nouveau dictionnaire avec toutes les valeurs × 2 |
| `10-best_score.py` | Retourne la clé avec la plus grande valeur entière |
| `11-multiply_list_map.py` | Utilise `map()` pour multiplier tous les éléments d'une liste |
| `12-roman_to_int.py` | Convertit un nombre romain en entier |

## 🎯 Learning Objectives <a name = "learning_objectives"></a>

À la fin de ce projet, vous serez capable d'expliquer :

- ✅ Pourquoi Python est génial pour la manipulation de données
- ✅ Les sets (ensembles) et leurs méthodes
- ✅ Les dictionnaires et leurs méthodes
- ✅ Quand utiliser sets vs lists
- ✅ Comment itérer sur des structures de données
- ✅ Les lambda functions
- ✅ Les fonctions `map`, `reduce` et `filter`

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Langage de programmation
- [PEP 8](https://pep8.org/) - Guide de style Python (pycodestyle)

## ✍️ Authors <a name = "authors"></a>

- **Alison Amblard** - [@github](https://github.com/alison-amblard)
- **Valentin Planchon** - [@github](https://github.com/valentin-planchon)
- **Yannis Leroy** - [@github](https://github.com/yannis-leroy)

---

<p align="center">
  Projet réalisé dans le cadre de la formation <strong>Holberton School</strong>
  <br>
  © 2026 Alison Amblard, Valentin Planchon, Yannis Leroy
</p>
