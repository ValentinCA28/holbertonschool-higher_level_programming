<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://www.holbertonschool.com/holberton-logo.png" alt="Holberton School logo"></a>
</p>

<h3 align="center">Python - Data Structures: Lists, Tuples</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Maîtriser les structures de données fondamentales en Python : listes et tuples.
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

Ce projet fait partie du programme **Holberton School** et explore les structures de données fondamentales en Python. À travers 13 exercices progressifs, nous apprenons à manipuler efficacement les **listes** et les **tuples**, deux structures essentielles pour la programmation Python.

Le projet couvre des opérations allant de la manipulation basique de listes (accès, remplacement, suppression) jusqu'à des concepts plus avancés comme les tuples, les matrices, et l'utilisation de techniques pythoniques pour le traitement de données.

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
cd holbertonschool-higher_level_programming/python-data_structures
```

Vérifiez votre version de Python :

```bash
python3 --version
```

## 🎈 Usage <a name="usage"></a>

Chaque fichier contient une fonction qui peut être importée et utilisée dans vos programmes Python :

### Exemple 1 : Print List Integer

```python
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)
```
```
1
2
3
4
5
```

### Exemple 2 : Element at Index

```python
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
print(element_at(my_list, 3))  # Output: 4
print(element_at(my_list, 10)) # Output: None
```

### Exemple 3 : Add Tuple

```python
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)  # Output: (89, 100)
```

### Exemple 4 : Max Integer

```python
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print(max_value)  # Output: 90
```

### Exemple 5 : Multiple Returns

```python
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At Holberton school, I learnt C!"
length, first = multiple_returns(sentence)
print(f"Length: {length}, First character: {first}")
# Output: Length: 32, First character: A
```

## 📚 Exercises <a name = "exercises"></a>

| Fichier | Description |
|---------|-------------|
| `0-print_list_integer.py` | Affiche tous les entiers d'une liste |
| `1-element_at.py` | Récupère un élément d'une liste à un index donné |
| `2-replace_in_list.py` | Remplace un élément d'une liste à un index spécifique |
| `3-print_reversed_list_integer.py` | Affiche tous les entiers d'une liste en ordre inverse |
| `4-new_in_list.py` | Remplace un élément dans une copie de la liste |
| `5-no_c.py` | Supprime tous les caractères 'c' et 'C' d'une chaîne |
| `6-print_matrix_integer.py` | Affiche une matrice d'entiers |
| `7-add_tuple.py` | Additionne deux tuples élément par élément |
| `8-multiple_returns.py` | Retourne la longueur d'une chaîne et son premier caractère |
| `9-max_integer.py` | Trouve le plus grand entier dans une liste |
| `10-divisible_by_2.py` | Trouve tous les multiples de 2 dans une liste |
| `11-delete_at.py` | Supprime l'élément à un index spécifique dans une liste |
| `12-switch.py` | Échange les valeurs de deux variables |

## 🎯 Learning Objectives <a name = "learning_objectives"></a>

À la fin de ce projet, vous serez capable d'expliquer :

- ✅ Pourquoi Python est génial pour la manipulation de données
- ✅ Les listes et comment les utiliser
- ✅ Les différences et similitudes entre strings et listes
- ✅ Les méthodes les plus courantes des listes
- ✅ Comment utiliser les listes comme des stacks et des queues
- ✅ Les list comprehensions et comment les utiliser
- ✅ Les tuples et comment les utiliser
- ✅ Quand utiliser tuples vs listes
- ✅ Les séquences en Python
- ✅ Le tuple unpacking
- ✅ La séquence `del` statement

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
