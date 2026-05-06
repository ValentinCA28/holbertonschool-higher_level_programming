# SQL - More Queries

![MySQL](https://img.shields.io/badge/Language-MySQL-4479A1.svg?logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/Concept-Advanced%20SQL-orange.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Approfondir MySQL : gestion des privileges, contraintes, cles etrangeres, sous-requetes et jointures.

---

## Objectifs d'apprentissage

- Gerer les utilisateurs et leurs privileges MySQL (GRANT, SHOW GRANTS)
- Utiliser les contraintes : NOT NULL, UNIQUE, DEFAULT, PRIMARY KEY, FOREIGN KEY
- Creer des tables avec des relations entre elles
- Effectuer des sous-requetes et des jointures (INNER JOIN, LEFT JOIN)
- Agreger des donnees avec GROUP BY et COUNT

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) | 8.0 | SGBD relationnel | `sudo apt install mysql-server` |

---

## Taches

### 0. My privileges!
> **Objectif** : Lister les privileges de deux utilisateurs MySQL

```sql
-- lists all privileges of user_0d_1 and user_0d_2
SHOW GRANTS FOR 'user_0d_1'@'localhost';
SHOW GRANTS FOR 'user_0d_2'@'localhost';
```

### 1. Root user
> **Objectif** : Creer un utilisateur avec tous les privileges

```sql
-- creates the user user_0d_1 with all privileges
CREATE USER IF NOT EXISTS 'user_0d_1'@'localhost' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1'@'localhost';
```

### 2. Read user
> **Objectif** : Creer un utilisateur avec uniquement le privilege SELECT

```sql
-- creates user_0d_2 with SELECT privilege on hbtn_0d_2
CREATE DATABASE IF NOT EXISTS hbtn_0d_2;
CREATE USER IF NOT EXISTS 'user_0d_2'@'localhost' IDENTIFIED BY 'user_0d_2_pwd';
GRANT SELECT ON hbtn_0d_2.* TO 'user_0d_2'@'localhost';
```

### 3. Always a name
> **Objectif** : Creer une table avec une contrainte NOT NULL et DEFAULT

```sql
-- creates table force_name with name that can't be NULL
CREATE TABLE IF NOT EXISTS force_name (
    id INT,
    name VARCHAR(256) NOT NULL
);
```

### 4. ID can't be null
> **Objectif** : Creer une table avec une valeur par defaut pour id

```sql
-- creates table id_not_null with id defaulting to 1
CREATE TABLE IF NOT EXISTS id_not_null (
    id INT DEFAULT 1,
    name VARCHAR(256)
);
```

### 5. Unique ID
> **Objectif** : Creer une table avec un id unique et une valeur par defaut

```sql
-- creates table unique_id with UNIQUE constraint on id
CREATE TABLE IF NOT EXISTS unique_id (
    id INT DEFAULT 1 UNIQUE,
    name VARCHAR(256)
);
```

### 6. States table
> **Objectif** : Creer une base de donnees et une table states avec cle primaire auto-increment

```sql
-- creates database hbtn_0d_usa and table states
CREATE DATABASE IF NOT EXISTS hbtn_0d_usa;
USE hbtn_0d_usa;
CREATE TABLE IF NOT EXISTS states (
    id INT NOT NULL AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id)
);
```

### 7. Cities table
> **Objectif** : Creer une table cities avec une cle etrangere vers states

```sql
-- creates table cities with foreign key referencing states
CREATE TABLE IF NOT EXISTS cities (
    id INT NOT NULL AUTO_INCREMENT,
    state_id INT NOT NULL,
    name VARCHAR(256) NOT NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (state_id) REFERENCES states(id)
);
```

### 8. Cities of California
> **Objectif** : Lister les villes de Californie avec une sous-requete

```sql
-- lists all cities of California using a subquery
SELECT id, name FROM cities
WHERE state_id = (SELECT id FROM states WHERE name = 'California')
ORDER BY id ASC;
```

### 9. Cities by States (JOIN)
> **Objectif** : Lister toutes les villes avec leur etat en utilisant un JOIN

```sql
-- lists all cities with their state name using JOIN
SELECT cities.id, cities.name, states.name
FROM cities
INNER JOIN states ON cities.state_id = states.id
ORDER BY cities.id ASC;
```

### 10. Genre ID by show
> **Objectif** : Lister les shows TV avec au moins un genre (INNER JOIN)

```sql
-- lists all shows with at least one genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
INNER JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
```

### 11. Genre ID for all shows
> **Objectif** : Lister tous les shows avec leur genre_id (LEFT JOIN)

```sql
-- lists all shows with their genre_id (NULL if no genre)
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
ORDER BY tv_shows.title ASC, tv_show_genres.genre_id ASC;
```

### 12. No genre
> **Objectif** : Lister les shows sans genre associe

```sql
-- lists all shows without a genre linked
SELECT tv_shows.title, tv_show_genres.genre_id
FROM tv_shows
LEFT JOIN tv_show_genres ON tv_shows.id = tv_show_genres.show_id
WHERE tv_show_genres.genre_id IS NULL
ORDER BY tv_shows.title ASC;
```

### 13. Number of shows by genre
> **Objectif** : Compter le nombre de shows par genre

```sql
-- lists all genres and the number of shows linked to each
SELECT tv_genres.name AS genre, COUNT(tv_show_genres.show_id) AS number_of_shows
FROM tv_genres
INNER JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.name
ORDER BY number_of_shows DESC;
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-SQL%20More%20Queries-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
