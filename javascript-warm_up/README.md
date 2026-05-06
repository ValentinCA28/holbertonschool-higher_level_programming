# JavaScript - Warm up

![JavaScript](https://img.shields.io/badge/Language-JavaScript-F7DF1E.svg?logo=javascript&logoColor=black)
![Node.js](https://img.shields.io/badge/Runtime-Node.js-339933.svg?logo=nodedotjs&logoColor=white)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Decouvrir les bases de JavaScript avec Node.js : variables, conditions, boucles, fonctions et arguments en ligne de commande.

---

## Objectifs d'apprentissage

- Utiliser `const` et `let` pour declarer des variables
- Manipuler `process.argv` pour lire les arguments CLI
- Ecrire des conditions avec `if/else`
- Utiliser les boucles `for` et `while`
- Definir et appeler des fonctions (y compris recursives)
- Convertir des types avec `parseInt` et `isNaN`

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![Node.js](https://img.shields.io/badge/Node.js-339933?logo=nodedotjs&logoColor=white) | 14.x | Runtime JavaScript | `sudo apt install nodejs` |

---

## Taches

### 0. JavaScript is amazing
> **Objectif** : Stocker une chaine dans une constante et l'afficher

```javascript
#!/usr/bin/node
const myVar = 'JavaScript is amazing';
console.log(myVar);
```

### 1. 3 languages
> **Objectif** : Afficher trois lignes avec differents langages

```javascript
#!/usr/bin/node
console.log('C is fun');
console.log('Python is cool');
console.log('JavaScript is amazing');
```

### 2. Arguments
> **Objectif** : Afficher un message selon le nombre d'arguments passes

```javascript
#!/usr/bin/node
const argc = process.argv.length - 2;
if (argc === 0) console.log('No argument');
else if (argc === 1) console.log('Argument found');
else console.log('Arguments found');
```

### 3. Value of my argument
> **Objectif** : Afficher le premier argument ou "No argument"

```javascript
#!/usr/bin/node
const arg = process.argv[2];
if (arg === undefined) console.log('No argument');
else console.log(arg);
```

### 4. Create a sentence
> **Objectif** : Concatener deux arguments dans une phrase

```javascript
#!/usr/bin/node
console.log(process.argv[2] + ' is ' + process.argv[3]);
```

### 5. An Integer
> **Objectif** : Convertir et afficher un entier, ou "Not a number"

```javascript
#!/usr/bin/node
const num = parseInt(process.argv[2]);
if (isNaN(num)) console.log('Not a number');
else console.log('My number: ' + num);
```

### 6. Loop to languages
> **Objectif** : Afficher trois langages en utilisant un tableau et une boucle

```javascript
#!/usr/bin/node
const langs = ['C is fun', 'Python is cool', 'JavaScript is amazing'];
for (let i = 0; i < langs.length; i++) {
  console.log(langs[i]);
}
```

### 7. I love C
> **Objectif** : Afficher "C is fun" x fois selon l'argument

```javascript
#!/usr/bin/node
const x = parseInt(process.argv[2]);
if (!isNaN(x)) {
  for (let i = 0; i < x; i++) console.log('C is fun');
}
```

### 8. Square
> **Objectif** : Afficher un carre de 'X' de taille donnee

```javascript
#!/usr/bin/node
const size = parseInt(process.argv[2]);
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) console.log('X'.repeat(size));
}
```

### 9. Add
> **Objectif** : Additionner deux entiers passes en arguments

```javascript
#!/usr/bin/node
function add (a, b) {
  return a + b;
}
console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
```

### 10. Factorial
> **Objectif** : Calculer la factorielle d'un nombre de maniere recursive

```javascript
#!/usr/bin/node
function factorial (n) {
  if (isNaN(n) || n <= 1) return 1;
  return n * factorial(n - 1);
}
console.log(factorial(parseInt(process.argv[2])));
```

### 11. Second biggest
> **Objectif** : Trouver le deuxieme plus grand nombre dans les arguments

```javascript
#!/usr/bin/node
const args = process.argv.slice(2).map(Number);
if (args.length <= 1) console.log(0);
else {
  args.sort((a, b) => b - a);
  console.log(args[1]);
}
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-JavaScript%20Warm%20Up-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
