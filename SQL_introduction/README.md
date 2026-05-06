# SQL - Introduction

![MySQL](https://img.shields.io/badge/Language-MySQL-4479A1.svg?logo=mysql&logoColor=white)
![SQL](https://img.shields.io/badge/Concept-SQL-orange.svg)
![Holberton](https://img.shields.io/badge/School-Holberton-red.svg)

> Decouvrir les bases de MySQL : creation de bases et tables, insertion de donnees, requetes SELECT et fonctions d'agregation.

---

## Objectifs d'apprentissage

- Creer et supprimer des bases de donnees et des tables
- Inserer, mettre a jour et supprimer des enregistrements
- Effectuer des requetes SELECT avec filtres et tri
- Utiliser les fonctions d'agregation : COUNT, AVG, GROUP BY
- Comprendre les types de donnees MySQL (INT, VARCHAR)

---

## Stack technique

| Outil | Version | Role | Installation |
|-------|---------|------|-------------|
| ![MySQL](https://img.shields.io/badge/MySQL-4479A1?logo=mysql&logoColor=white) | 8.0 | SGBD relationnel | `sudo apt install mysql-server` |

---

## Taches

### 0. List databases
> **Objectif** : Lister toutes les bases de donnees du serveur MySQL

```sql
-- lists all databases of the MySQL server
SHOW DATABASES;
```

### 1. Create a database
> **Objectif** : Creer une base de donnees si elle n'existe pas

```sql
-- creates the database hbtn_0c_0 if it does not already exist
CREATE DATABASE IF NOT EXISTS hbtn_0c_0;
```

### 2. Delete a database
> **Objectif** : Supprimer une base de donnees si elle existe

```sql
-- removes the database hbtn_0c_0
DROP DATABASE IF EXISTS hbtn_0c_0;
```

### 3. List tables
> **Objectif** : Lister toutes les tables d'une base de donnees

```sql
-- lists all tables in the current database
SHOW TABLES;
```

### 4. First table
> **Objectif** : Creer une table avec des colonnes id et name

```sql
-- creates the table first_table if it does not already exist
CREATE TABLE IF NOT EXISTS first_table (
    id INT,
    name VARCHAR(256) NOT NULL
);
```

### 5. Full description
> **Objectif** : Afficher la description complete d'une table

```sql
-- displays the full description of first_table
SHOW CREATE TABLE first_table;
```

### 6. List all in table
> **Objectif** : Lister tous les enregistrements d'une table

```sql
-- lists all rows in first_table
SELECT * FROM first_table;
```

### 7. First add
> **Objectif** : Inserer un nouvel enregistrement dans une table

```sql
-- inserts a new row in first_table
INSERT INTO first_table (id, name) VALUES (89, 'Best School');
```

### 8. Count 89
> **Objectif** : Compter les enregistrements avec un id specifique

```sql
-- counts records with id = 89
SELECT COUNT(*) FROM second_table WHERE id = 89;
```

### 9. Full creation
> **Objectif** : Creer une table et inserer plusieurs enregistrements

```sql
-- creates second_table and inserts 4 rows
CREATE TABLE IF NOT EXISTS second_table (
    id INT, name VARCHAR(256), score INT
);
INSERT INTO second_table (id, name, score) VALUES (1, 'John', 10);
INSERT INTO second_table (id, name, score) VALUES (2, 'Alex', 3);
INSERT INTO second_table (id, name, score) VALUES (3, 'Bob', 14);
INSERT INTO second_table (id, name, score) VALUES (4, 'George', 8);
```

### 10. List by best
> **Objectif** : Lister les enregistrements tries par score decroissant

```sql
-- lists all records ordered by score (top first)
SELECT score, name FROM second_table ORDER BY score DESC;
```

### 11. Select the best
> **Objectif** : Afficher les enregistrements avec un score >= 10

```sql
-- lists records with score >= 10, ordered by score DESC
SELECT score, name FROM second_table WHERE score >= 10 ORDER BY score DESC;
```

### 12. Cheating is bad
> **Objectif** : Mettre a jour le score d'un enregistrement specifique

```sql
-- updates the score of Bob to 10 (without using id)
UPDATE second_table SET score = 10 WHERE name = 'Bob';
```

### 13. Score too low
> **Objectif** : Supprimer les enregistrements avec un score <= 5

```sql
-- removes records with score <= 5
DELETE FROM second_table WHERE score <= 5;
```

### 14. Average
> **Objectif** : Calculer la moyenne des scores

```sql
-- displays the average score
SELECT AVG(score) AS average FROM second_table;
```

### 15. Number by score
> **Objectif** : Compter les enregistrements par score avec GROUP BY

```sql
-- displays the score and number of records for each score
SELECT score, COUNT(*) AS number FROM second_table
GROUP BY score ORDER BY number DESC;
```

### 16. Say my name
> **Objectif** : Lister les enregistrements avec un nom non vide

```sql
-- displays score and name where name is not NULL and not empty
SELECT score, name FROM second_table
WHERE name IS NOT NULL AND name != ''
ORDER BY score DESC;
```

---

## Auteur

- **Valentin Planchon**

---

<div align="center">

![Holberton School](https://img.shields.io/badge/HOLBERTON%20SCHOOL-SQL%20Introduction-white?style=for-the-badge&logo=data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTYiIGhlaWdodD0iMTYiIHZpZXdCb3g9IjAgMCAxNiAxNiIgZmlsbD0ibm9uZSIgeG1sbnM9Imh0dHA6Ly93d3cudzMub3JnLzIwMDAvc3ZnIj4KPHBhdGggZD0iTTE0LjY2NyA4QzE0LjY2NyA0LjY4NiAxMi4zMTQgMi4zMzMzIDkgMi4zMzMzQzUuNjg2NyAyLjMzMzMgMy4zMzMzIDQuNjg2IDMuMzMzIDhDMi4xNDYgOCAyIDguMTQ2IDAgOEMwIDEyLjMxNCAyLjM1NCAxNC42NjcgNi42NjcgMTQuNjY3QzYuNjY3IDE1LjE4NiA2LjkzMyAxNS41MzMgNy4zMzMzIDE1Ljc4N0M3LjczMzMgMTYuMDMzIDguMTMzMyAxNi4xNiA4LjY2NjcgMTYuMTYgOS4yIDkuNTMzMyAxMC4xMzMgMTYuMTYgMTAuNjY3IDE2LjE2QzExLjIgMTYuMTYgMTEuNiAxNi4wMzMgMTIuMDY3IDE1Ljc4N0MxMi41MzMgMTUuNTMzIDEyLjggMTUuMTg2IDEyLjggMTQuNjY3QzE0LjY2NyAxNC42NjcgMTQuNjY3IDguNjY3IDE0LjY2NyA4WiIgZmlsbD0iI0ZGRkZGRiIvPgo8L3N2Zz4K&labelColor=c41e3a&color=36393f) <img src="../images/holberton_logo.png" alt="Holberton Logo" width="34">

[Retour au projet principal](../)

</div>
