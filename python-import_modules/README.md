<p align="center">
  <a href="" rel="noopener">
 <img width=200px height=200px src="https://www.holbertonschool.com/holberton-logo.png" alt="Holberton School logo"></a>
</p>

<h3 align="center">Python - Import & Modules</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![Python](https://img.shields.io/badge/python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Maîtriser les imports de modules et l'utilisation de fonctions externes en Python.
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Usage](#usage)
- [Files](#files)
- [Learning Objectives](#learning_objectives)
- [Built Using](#built_using)
- [Authors](#authors)

## 🧐 About <a name = "about"></a>

Ce projet fait partie du programme **Holberton School** et couvre les fondamentaux de l'importation de modules en Python. À travers différents exercices pratiques, nous apprenons à :

- Organiser notre code en modules réutilisables
- Importer et utiliser des fonctions depuis d'autres fichiers
- Gérer les arguments de ligne de commande
- Utiliser les bonnes pratiques d'imports en Python

Ce projet constitue une base essentielle pour structurer des applications Python de manière modulaire et maintenable.

## 🏁 Getting Started <a name = "getting_started"></a>

Ces instructions vous permettront d'obtenir une copie du projet et de l'exécuter sur votre machine locale.

### Prerequisites

Pour exécuter ce projet, vous aurez besoin de :

```
Python 3.12.x
pycodestyle (pour vérifier le style de code)
```

### Installation

Clonez le repository :

```bash
git clone https://github.com/votre-username/holbertonschool-higher_level_programming.git
cd holbertonschool-higher_level_programming/python-import_modules
```

Rendez tous les fichiers exécutables :

```bash
chmod +x *.py
```

### Requirements

- ✅ Python 3.12.x
- ✅ Tous les fichiers sont exécutables
- ✅ Code conforme au guide PEP8 (pycodestyle)
- ✅ Tous les fichiers se terminent par une nouvelle ligne
- ✅ Première ligne de tous les fichiers : `#!/usr/bin/python3`

## 🎈 Usage <a name="usage"></a>

Chaque fichier peut être exécuté directement :

### Exemple 1 : Addition simple

```bash
./0-add.py
```
```
1 + 2 = 3
```

### Exemple 2 : Calculatrice

```bash
./1-calculation.py
```
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
```

### Exemple 3 : Arguments en ligne de commande

```bash
./2-args.py Hello World Python
```
```
3 arguments:
1: Hello
2: World
3: Python
```

### Exemple 4 : Addition infinie

```bash
./3-infinite_add.py 10 20 30 40 50
```
```
150
```

### Exemple 5 : Charger une variable

```bash
./5-variable_load.py
```
```
98
```

## 📚 Files <a name = "files"></a>

### Mandatory Tasks

| Fichier | Description |
|---------|-------------|
| `0-add.py` | Importe la fonction `add(a, b)` depuis `add_0.py` et affiche le résultat |
| `1-calculation.py` | Importe des fonctions depuis `calculator_1.py` et effectue des opérations |
| `2-args.py` | Affiche le nombre et la liste des arguments passés au programme |
| `3-infinite_add.py` | Affiche la somme de tous les arguments passés |
| `4-hidden_discovery.py` | Affiche tous les noms définis dans le module compilé `hidden_4.pyc` |
| `5-variable_load.py` | Importe la variable `a` depuis `variable_load_5.py` et affiche sa valeur |

### Module Files

| Fichier | Description |
|---------|-------------|
| `add_0.py` | Module contenant la fonction `add()` |
| `calculator_1.py` | Module contenant les fonctions de calculatrice (add, sub, mul, div) |
| `variable_load_5.py` | Module contenant une variable `a` |

## 🎯 Learning Objectives <a name = "learning_objectives"></a>

À la fin de ce projet, vous serez capable d'expliquer :

- ✅ Comment importer des fonctions depuis un autre fichier
- ✅ Comment utiliser les fonctions importées
- ✅ Comment créer un module
- ✅ Comment utiliser la fonction built-in `dir()`
- ✅ Comment empêcher l'exécution de code lors d'un import
- ✅ Comment utiliser les arguments de ligne de commande avec Python

## ⛏️ Built Using <a name = "built_using"></a>

- [Python](https://www.python.org/) - Langage de programmation
- [PEP 8](https://pep8.org/) - Guide de style Python (pycodestyle)

## ✍️ Authors <a name = "authors"></a>

- **Alison Amblard** - [@github](https://github.com/alison-amblard)
- **Damien Rossi** - [@github](https://github.com/damien-rossi)
- **Yanis Leroy** - [@github](https://github.com/yanis-leroy)
- **Valentin Planchon** - [@github](https://github.com/valentin-planchon)

---

<p align="center">
  Projet réalisé dans le cadre de la formation <strong>Holberton School</strong>
  <br>
  © 2026 Alison Amblard, Damien Rossi, Yanis Leroy, Valentin Planchon
</p>
