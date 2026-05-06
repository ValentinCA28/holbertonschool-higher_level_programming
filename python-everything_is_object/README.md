# Python - Everything is object

![Python](https://img.shields.io/badge/Language-Python-3776AB.svg?logo=python&logoColor=white)
![Concept](https://img.shields.io/badge/Concept-Objects%20%26%20References-blue.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Comprendre le modele objet de Python : mutabilite, identite, aliasing et comportement des references.

---

## Objectifs d'apprentissage

- Comprendre la difference entre `id()`, `type()` et `==` vs `is`
- Maitriser la mutabilite et l'immutabilite des types Python
- Comprendre l'aliasing et ses consequences sur les objets mutables
- Savoir quand Python cree un nouvel objet ou reutilise une reference
- Differencier copie superficielle et copie par reference

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white) | 3.12.x | Langage de programmation | `sudo apt install python3` |

---

## Taches

### 0-28. Questions sur les objets Python
> **Objectif** : Repondre a des questions conceptuelles sur le comportement des objets

Chaque fichier `X-answer.txt` contient la reponse a une question sur les types, l'identite, la mutabilite ou les references en Python. Exemples de sujets :

- Quel est le type d'un objet ? (`type()`)
- Deux variables pointent-elles vers le meme objet ? (`is`)
- Que se passe-t-il quand on modifie une liste aliasee ?
- Les entiers sont-ils mis en cache par Python (interning) ?
- Les tuples sont-ils mutables ou immutables ?

### 19. Copy a list
> **Objectif** : Copier une liste sans creer un alias

```python
def copy_list(a_list):
    """Return a copy of the list using slicing."""
    return a_list[:]
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-Python%20Everything%20Is%20Object-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
