# JavaScript - DOM Manipulation

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![DOM](https://img.shields.io/badge/Concept-DOM%20API-blue.svg)
![Fetch](https://img.shields.io/badge/Concept-Fetch%20API-green.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Maitriser la manipulation du DOM avec JavaScript : selection d'elements, gestion d'evenements, modification de styles/classes et appels API avec Fetch.

---

## Objectifs d'apprentissage

- Selectionner des elements du DOM avec `querySelector`
- Ajouter des event listeners (`click`, `DOMContentLoaded`)
- Modifier les styles inline et les classes CSS
- Creer et ajouter des elements dynamiquement
- Effectuer des requetes HTTP avec la Fetch API
- Parser et afficher des donnees JSON depuis une API externe

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?logo=javascript&logoColor=black) | ES6 | Langage cote client | Navigateur web |

---

## Taches

### 0. Color Me
> **Objectif** : Modifier la couleur du texte d'un header en rouge

```javascript
document.querySelector('header').style.color = '#FF0000';
```

### 1. Click and Turn Red
> **Objectif** : Changer la couleur du header au clic sur un bouton

```javascript
document.querySelector('#red_header').addEventListener('click', function() {
    document.querySelector('header').style.color = '#FF0000';
});
```

### 2. Add Class
> **Objectif** : Ajouter une classe CSS a un element au clic

```javascript
document.querySelector('#red_header').addEventListener('click', function () {
    document.querySelector('header').classList.add('red');
});
```

### 3. Toggle Classes
> **Objectif** : Basculer entre deux classes CSS au clic

```javascript
document.querySelector('#toggle_header').addEventListener('click', function () {
    document.querySelector('header').classList.toggle('red');
    document.querySelector('header').classList.toggle('green');
});
```

### 4. List of Elements
> **Objectif** : Ajouter un element `<li>` a une liste au clic

```javascript
document.querySelector('#add_item').addEventListener('click', function () {
    const newItem = document.createElement('li');
    newItem.textContent = 'Item';
    document.querySelector('.my_list').appendChild(newItem);
});
```

### 5. Change the Text
> **Objectif** : Modifier le contenu textuel d'un element au clic

```javascript
document.querySelector('header').addEventListener('click', function () {
    document.querySelector('#update_header').textContent = 'New Header!!!';
});
```

### 6. Star Wars Character
> **Objectif** : Recuperer un personnage Star Wars via l'API SWAPI et l'afficher

```javascript
fetch('https://swapi-api.hbtn.io/api/people/5/?format=json')
    .then(response => response.json())
    .then(data => {
        document.querySelector('#character').textContent = data.name;
    });
```

### 7. Star Wars Movies
> **Objectif** : Lister tous les films Star Wars depuis l'API

```javascript
fetch('https://swapi-api.hbtn.io/api/films/?format=json')
    .then(response => response.json())
    .then(data => {
        data.results.forEach(movie => {
            const newLi = document.createElement('li');
            newLi.textContent = movie.title;
            document.querySelector('#list_movies').appendChild(newLi);
        });
    });
```

### 8. Say Hello
> **Objectif** : Recuperer une traduction de "hello" et l'afficher au chargement

```javascript
document.addEventListener('DOMContentLoaded', function () {
    fetch('https://hellosalut.stefanbohacek.com/?lang=fr')
        .then(response => response.json())
        .then(data => {
            document.querySelector('#hello').textContent = data.hello;
        });
});
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-JavaScript%20DOM%20Manipulation-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
