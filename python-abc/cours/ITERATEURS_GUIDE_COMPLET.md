# 📘 Guide Complet : Les Itérateurs en Python et CountedIterator

## 📌 Table des Matières
1. Introduction aux Itérateurs
2. Les Relations et Concepts Clés
3. Implémentation de CountedIterator
4. Diagrammes et Explications
5. Exemples Pratiques

---

## 🎯 1. Introduction aux Itérateurs

### Qu'est-ce qu'un Itérateur ?

Un **itérateur** est un objet qui implémente le protocole d'itération, permettant de parcourir une séquence d'éléments un par un.

**Analogie** :
```
Livre (Itérable)     →  Peut être lu
├── Marque-page      →  Itérateur (sait où on en est)
└── Tourner la page  →  __next__() (avancer d'un élément)
```

### Différence Itérable vs Itérateur

```python
# ITÉRABLE : Objet qu'on PEUT parcourir
liste = [1, 2, 3]        # Liste = itérable
texte = "Hello"          # String = itérable
tuple = (1, 2, 3)        # Tuple = itérable

# ITÉRATEUR : Objet qui FAIT le parcours
iterateur = iter(liste)  # Crée un itérateur à partir de la liste
```

**Important** :
- Tout itérateur est itérable
- Tous les itérables ne sont PAS des itérateurs
- Un itérable devient itérateur via `iter()`

---

## 🔗 2. Les Relations et Concepts Clés

### A. Le Protocole d'Itération

Python définit deux méthodes magiques pour l'itération :

```python
__iter__()   # Retourne un itérateur
__next__()   # Retourne l'élément suivant
```

**Schéma du flux** :
```
[1, 2, 3]  →  iter()  →  Itérateur  →  next()  →  1
                             ↓         next()  →  2
                             ↓         next()  →  3
                             ↓         next()  →  StopIteration
```

### B. La Relation de Composition

**CountedIterator** utilise la **composition** :

```
CountedIterator
├── _iterator   (itérateur interne - COMPOSITION)
└── _count      (compteur)
```

**Pourquoi composition et pas héritage ?**

❌ **Mauvaise approche** : Hériter de list_iterator
```python
# IMPOSSIBLE : on ne peut pas hériter directement
class CountedIterator(list_iterator):  # list_iterator n'est pas accessible
    pass
```

✅ **Bonne approche** : Envelopper un itérateur existant
```python
class CountedIterator:
    def __init__(self, iterable):
        self._iterator = iter(iterable)  # COMPOSITION
        self._count = 0
```

### C. Le Pattern Decorator (Décorateur)

CountedIterator implémente le **Decorator Pattern** :

```
Itérateur de base      CountedIterator
     [A, B, C]              |
        ↓                   |
    __next__()  ←──────  Ajoute comptage
        ↓                   ↓
    Retourne A          Retourne A + count=1
```

**Avantages** :
- ✅ Ajoute une fonctionnalité sans modifier l'original
- ✅ Réutilisable avec n'importe quel itérable
- ✅ Respecte le principe Open/Closed (ouvert à l'extension, fermé à la modification)

### D. La Délégation

**Délégation** = "Je ne sais pas faire, mais je connais quelqu'un qui sait"

```python
def __next__(self):
    item = next(self._iterator)  # DÉLÉGATION à l'itérateur interne
    self._count += 1
    return item
```

**Schéma** :
```
CountedIterator.next()
    │
    ├─→ Demande à self._iterator.next()  (DÉLÉGATION)
    │       │
    │       └─→ Retourne l'élément
    │
    └─→ Incrémente _count
    │
    └─→ Retourne l'élément
```

---

## 💻 3. Implémentation de CountedIterator

### Code Complet Annoté

```python
class CountedIterator:
    """Itérateur qui compte les éléments parcourus."""
    
    def __init__(self, iterable):
        """
        ÉTAPE 1 : Initialisation
        
        On crée :
        - Un itérateur interne (via iter())
        - Un compteur initialisé à 0
        """
        self._iterator = iter(iterable)  # Composition
        self._count = 0                   # État interne
    
    def __iter__(self):
        """
        ÉTAPE 2 : Retourner l'itérateur
        
        Cette méthode permet à CountedIterator d'être
        utilisé dans les boucles for.
        """
        return self  # On est notre propre itérateur
    
    def __next__(self):
        """
        ÉTAPE 3 : Récupérer le prochain élément
        
        Ordre important :
        1. Récupérer l'élément (peut lever StopIteration)
        2. Si réussi, incrémenter le compteur
        3. Retourner l'élément
        """
        item = next(self._iterator)  # Délégation
        self._count += 1              # Comptage
        return item                   # Retour
    
    def get_count(self):
        """
        ÉTAPE 4 : Accéder au compteur
        
        Encapsulation : on donne accès au compteur
        de manière contrôlée.
        """
        return self._count
```

### Pourquoi cet ordre dans __next__() ?

```python
# ✅ CORRECT
def __next__(self):
    item = next(self._iterator)  # Si échoue → StopIteration
    self._count += 1              # N'est jamais atteint si échec
    return item

# ❌ INCORRECT
def __next__(self):
    self._count += 1              # Incrémente même si liste vide !
    return next(self._iterator)   # StopIteration après incrémentation
```

**Test avec liste vide** :
```python
empty = []
counted = CountedIterator(empty)

# Avec ordre CORRECT :
next(counted)  # StopIteration, count reste à 0 ✓

# Avec ordre INCORRECT :
next(counted)  # StopIteration, mais count = 1 ✗
```

---

## 📊 4. Diagrammes et Explications

### Diagramme de Séquence

```
User              CountedIterator         Itérateur Interne
  |                      |                        |
  |--next()------------->|                        |
  |                      |--next()--------------->|
  |                      |                        |
  |                      |<------retourne 'A'----|
  |                      |                        |
  |                      |  _count += 1           |
  |                      |  (count = 1)           |
  |                      |                        |
  |<-----retourne 'A'----|                        |
  |                      |                        |
  |--get_count()-------->|                        |
  |<-----retourne 1------|                        |
```

### Cycle de Vie d'un CountedIterator

```
1. CRÉATION
   ┌─────────────────────────────┐
   │ CountedIterator([1, 2, 3]) │
   └─────────────────────────────┘
              ↓
   ┌─────────────────────────────┐
   │ _iterator = iter([1,2,3])  │
   │ _count = 0                  │
   └─────────────────────────────┘

2. PREMIÈRE ITÉRATION
   next() appelé
              ↓
   _iterator.next() → retourne 1
              ↓
   _count += 1  (count = 1)
              ↓
   retourne 1

3. DEUXIÈME ITÉRATION
   next() appelé
              ↓
   _iterator.next() → retourne 2
              ↓
   _count += 1  (count = 2)
              ↓
   retourne 2

4. FIN
   next() appelé
              ↓
   _iterator.next() → StopIteration
              ↓
   Propagation de StopIteration
   (count reste à 3)
```

---

## 🧪 5. Exemples Pratiques

### Exemple 1 : Utilisation Basique

```python
data = [1, 2, 3, 4]
counted = CountedIterator(data)

# Méthode 1 : next() manuel
print(next(counted))  # 1, count=1
print(next(counted))  # 2, count=2
print(counted.get_count())  # 2

# Méthode 2 : Boucle for
for item in counted:  # Continue de 3
    print(f"{item} - total: {counted.get_count()}")
# Affiche :
# 3 - total: 3
# 4 - total: 4
```

### Exemple 2 : Avec Try/Except

```python
data = [1, 2, 3]
counted = CountedIterator(data)

try:
    while True:
        item = next(counted)
        print(f"Got {item}, count={counted.get_count()}")
except StopIteration:
    print(f"Done! Total: {counted.get_count()}")

# Sortie :
# Got 1, count=1
# Got 2, count=2
# Got 3, count=3
# Done! Total: 3
```

### Exemple 3 : Itération Partielle

```python
data = range(1, 11)  # 1 à 10
counted = CountedIterator(data)

# On ne prend que les 5 premiers
for _ in range(5):
    next(counted)

print(f"Parcouru : {counted.get_count()}/10")
# Sortie : Parcouru : 5/10

# On peut continuer plus tard
for item in counted:
    print(item)
# Affiche : 6, 7, 8, 9, 10
```

### Exemple 4 : Avec Différents Types

```python
# Avec une string
text = CountedIterator("Python")
for char in text:
    print(f"{char} - position {text.get_count()}")

# Avec un tuple
coords = CountedIterator((10, 20, 30))
x = next(coords)  # 10, count=1
y = next(coords)  # 20, count=2

# Avec un générateur
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

fib = CountedIterator(fibonacci(10))
for num in fib:
    if fib.get_count() == 5:
        break
print(f"Premiers 5 nombres de Fibonacci générés")
```

---

## 🎓 Concepts Importants Récapitulatifs

### 1. **Composition > Héritage**
   - On "possède" un itérateur au lieu d'en "être" un
   - Plus flexible et réutilisable

### 2. **Délégation**
   - On délègue le travail complexe à l'itérateur interne
   - On se concentre sur notre fonctionnalité (comptage)

### 3. **Protocole d'Itération**
   - `__iter__()` : retourne self
   - `__next__()` : retourne l'élément suivant ou lève StopIteration

### 4. **Encapsulation**
   - Attributs privés (`_iterator`, `_count`)
   - Accès contrôlé via `get_count()`

### 5. **Exception StopIteration**
   - Signal de fin d'itération
   - Doit être propagée, pas capturée dans `__next__()`

---

## ✅ Checklist de Compréhension

- [ ] Je comprends la différence entre itérable et itérateur
- [ ] Je sais pourquoi on utilise composition plutôt qu'héritage
- [ ] Je comprends le rôle de `__iter__()` et `__next__()`
- [ ] Je sais pourquoi l'ordre dans `__next__()` est important
- [ ] Je comprends le concept de délégation
- [ ] Je peux expliquer quand StopIteration est levée
- [ ] Je peux créer mes propres itérateurs personnalisés

---

## 🚀 Pour Aller Plus Loin

### Exercices Supplémentaires :

1. **FilteredIterator** : Itérateur qui filtre les éléments
2. **ReversedIterator** : Itérateur qui parcourt à l'envers
3. **ChainIterator** : Itérateur qui chaîne plusieurs itérables
4. **ZipIterator** : Itérateur qui combine plusieurs itérables

### Pattern Avancé : Générateurs

```python
def counted_generator(iterable):
    """Alternative avec un générateur."""
    count = 0
    for item in iterable:
        count += 1
        yield item, count

# Utilisation
for item, count in counted_generator([1, 2, 3]):
    print(f"{item} - count: {count}")
```

---

## 📚 Ressources

- [Documentation Python - Iterators](https://docs.python.org/3/tutorial/classes.html#iterators)
- [PEP 234 - Iterators](https://www.python.org/dev/peps/pep-0234/)
- [Real Python - Iterators and Iterables](https://realpython.com/python-iterators-iterables/)

---

**Fait avec ❤️ pour comprendre les itérateurs en Python**
