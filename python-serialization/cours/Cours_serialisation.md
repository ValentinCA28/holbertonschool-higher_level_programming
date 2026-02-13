# Cours Complet : Sérialisation de Données en Python

## 📚 Table des Matières
1. [Introduction à la Sérialisation](#intro)
2. [JSON - Format Universel](#json)
3. [Pickle - Sérialisation Python](#pickle)
4. [CSV - Données Tabulaires](#csv)
5. [XML - Format Hiérarchique](#xml)
6. [Sockets - Communication Réseau](#sockets)
7. [Applications Pratiques](#applications)

---

## 1. INTRODUCTION À LA SÉRIALISATION <a name="intro"></a>

### Qu'est-ce que la sérialisation ?

La **sérialisation** est la conversion d'objets Python en formats stockables/transmissibles :

```
Objet Python  →  [Sérialisation]  →  Format (fichier/réseau)  →  [Désérialisation]  →  Objet Python
```

**Cas d'usage :**
- 💾 Sauvegarder la configuration d'une application
- 🌐 Transmettre des données client ↔ serveur
- 📊 Exporter des données vers Excel/CSV
- 🔄 Créer des points de sauvegarde (checkpoints)

---

## 2. JSON - FORMAT LÉGER ET UNIVERSEL <a name="json"></a>

### Pourquoi JSON ?
- ✅ Lisible par l'humain
- ✅ Indépendant du langage (JavaScript, Python, Java, etc.)
- ✅ Léger et rapide
- ❌ Types limités (pas de date, set, etc.)

### Correspondance Python ↔ JSON

| Python | JSON |
|--------|------|
| dict | object |
| list | array |
| str | string |
| int, float | number |
| True/False | true/false |
| None | null |


### Exemple 1 : Sérialisation JSON Basique

```python
import json

# ÉTAPE 1 : Créer des données Python
personne = {
    "nom": "Alice",
    "age": 30,
    "ville": "Paris",
    "competences": ["Python", "JavaScript", "SQL"],
    "actif": True
}

# ÉTAPE 2 : Convertir en chaîne JSON
json_string = json.dumps(personne)
print(json_string)
# Résultat : {"nom": "Alice", "age": 30, "ville": "Paris", ...}

# ÉTAPE 3 : Formater joliment
json_joli = json.dumps(personne, indent=4, ensure_ascii=False)
print(json_joli)

# ÉTAPE 4 : Reconvertir en Python
personne_restauree = json.loads(json_string)
print(personne_restauree["nom"])  # Alice
```

**Explication détaillée :**
- `json.dumps()` : "dump string" - convertit objet → chaîne JSON
- `indent=4` : ajoute indentation pour lisibilité
- `ensure_ascii=False` : permet caractères accentués
- `json.loads()` : "load string" - chaîne JSON → objet Python

### Exemple 2 : Sauvegarder et Charger depuis un Fichier

```python
import json

# ÉTAPE 1 : Données à sauvegarder
utilisateurs = [
    {"id": 1, "nom": "Jean", "email": "jean@example.com"},
    {"id": 2, "nom": "Marie", "email": "marie@example.com"}
]

# ÉTAPE 2 : Écrire dans fichier JSON
with open("utilisateurs.json", "w", encoding="utf-8") as f:
    json.dump(utilisateurs, f, indent=4, ensure_ascii=False)

print("✓ Fichier créé")

# ÉTAPE 3 : Lire depuis fichier JSON
with open("utilisateurs.json", "r", encoding="utf-8") as f:
    utilisateurs_charges = json.load(f)

# ÉTAPE 4 : Utiliser les données
for user in utilisateurs_charges:
    print(f"{user['nom']}: {user['email']}")
```

**Logique :**
1. `with open()` : ouvre et ferme automatiquement
2. Mode `"w"` : écriture (écrase si existe)
3. Mode `"r"` : lecture seule
4. `json.dump()` : écrit directement dans fichier
5. `json.load()` : lit directement depuis fichier

### Exemple 3 : Objets Personnalisés avec JSON

```python
import json
from datetime import datetime

class Employe:
    def __init__(self, nom, poste, date_embauche):
        self.nom = nom
        self.poste = poste
        self.date_embauche = date_embauche

# ÉTAPE 1 : Créer un encodeur personnalisé
class EmployeEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, Employe):
            return {
                "nom": obj.nom,
                "poste": obj.poste,
                "date_embauche": obj.date_embauche.isoformat()
            }
        if isinstance(obj, datetime):
            return obj.isoformat()
        return super().default(obj)

# ÉTAPE 2 : Sérialiser avec encodeur
employe = Employe("Sophie", "Dev", datetime(2023, 1, 15))
json_employe = json.dumps(employe, cls=EmployeEncoder, indent=2)
print(json_employe)

# ÉTAPE 3 : Désérialiser avec fonction personnalisée
def decoder_employe(dct):
    if "nom" in dct and "poste" in dct:
        return Employe(
            nom=dct["nom"],
            poste=dct["poste"],
            date_embauche=datetime.fromisoformat(dct["date_embauche"])
        )
    return dct

employe_restaure = json.loads(json_employe, object_hook=decoder_employe)
```

**Concepts clés :**
- `JSONEncoder.default()` : appelée pour types non-standard
- `isinstance()` : vérifie le type d'objet
- `isoformat()` : format ISO 8601 pour dates
- `object_hook` : fonction appliquée à chaque objet décodé

---

## 3. PICKLE - SÉRIALISATION NATIVE PYTHON <a name="pickle"></a>

### Qu'est-ce que Pickle ?

**Pickle** sérialise TOUS les types Python :
- ✅ Tous objets Python (classes, fonctions, etc.)
- ✅ Très rapide
- ❌ Format binaire (illisible)
- ❌ Python uniquement
- ⚠️ **DANGER** : N'utilisez JAMAIS pickle avec données non fiables !

### Exemple 1 : Pickle Basique

```python
import pickle

# ÉTAPE 1 : Données complexes
data = {
    "liste": [1, 2, 3],
    "tuple": (10, 20),
    "set": {100, 200},
    "fonction": lambda x: x * 2  # Même les fonctions !
}

# ÉTAPE 2 : Sérialiser en bytes
pickle_bytes = pickle.dumps(data)
print(f"Taille : {len(pickle_bytes)} bytes")

# ÉTAPE 3 : Désérialiser
data_restauree = pickle.loads(pickle_bytes)
print(data_restauree)

# ÉTAPE 4 : Tester la fonction
f = data_restauree["fonction"]
print(f(5))  # 10
```

**Points importants :**
- `pickle.dumps()` : retourne bytes
- Préserve TOUS les types Python
- Même les fonctions lambda sont conservées

### Exemple 2 : Sauvegarder Objets Complexes

```python
import pickle
from datetime import datetime

class JeuVideo:
    def __init__(self, joueur, niveau):
        self.joueur = joueur
        self.niveau = niveau
        self.score = 0
        self.inventaire = []
        self.date = datetime.now()
    
    def ajouter_objet(self, objet):
        self.inventaire.append(objet)
        self.score += 10

# ÉTAPE 1 : Créer session de jeu
session = JeuVideo("Alice", 5)
session.ajouter_objet("Épée")
session.score += 100

# ÉTAPE 2 : Sauvegarder
with open("save.pkl", "wb") as f:  # wb = write binary
    pickle.dump(session, f)

print("✓ Sauvegarde créée")

# ÉTAPE 3 : Charger
with open("save.pkl", "rb") as f:  # rb = read binary
    session_chargee = pickle.load(f)

print(f"Joueur : {session_chargee.joueur}")
print(f"Score : {session_chargee.score}")
print(f"Inventaire : {session_chargee.inventaire}")
```

**Logique :**
1. Mode `"wb"` = write binary (obligatoire pour pickle)
2. Mode `"rb"` = read binary
3. Pickle sauvegarde TOUT l'état de l'objet
4. Objets restaurés avec méthodes intactes

### Exemple 3 : Protocoles et Compression

```python
import pickle
import gzip

# ÉTAPE 1 : Grandes données
big_data = {"nombres": list(range(100000))}

# ÉTAPE 2 : Tester protocoles
pickle_v0 = pickle.dumps(big_data, protocol=0)  # ASCII
pickle_v4 = pickle.dumps(big_data, protocol=4)  # Binaire
pickle_v5 = pickle.dumps(big_data, protocol=5)  # Moderne

print(f"Protocol 0: {len(pickle_v0):,} bytes")
print(f"Protocol 4: {len(pickle_v4):,} bytes")
print(f"Protocol 5: {len(pickle_v5):,} bytes")

# ÉTAPE 3 : Pickle + Compression
with gzip.open("data.pkl.gz", "wb") as f:
    pickle.dump(big_data, f, protocol=pickle.HIGHEST_PROTOCOL)

# ÉTAPE 4 : Charger compressé
with gzip.open("data.pkl.gz", "rb") as f:
    data_restauree = pickle.load(f)

print("✓ Données compressées restaurées")
```

**Protocoles :**
- Protocol 0 : ASCII (compatible anciennes versions)
- Protocol 4+ : binaire optimisé
- `pickle.HIGHEST_PROTOCOL` : meilleur protocole disponible

### ⚠️ SÉCURITÉ PICKLE - CRITIQUE

```python
# ❌ DANGER - Ne JAMAIS unpickler données non fiables !
# Pickle peut exécuter du code arbitraire

# ✅ Solution : Unpickler sécurisé
class SafeUnpickler(pickle.Unpickler):
    def find_class(self, module, name):
        # Autoriser uniquement types de base
        if module == "builtins":
            return super().find_class(module, name)
        raise pickle.UnpicklingError(f"Interdit: {module}.{name}")
```

**Règle d'or :** Pickle = uniquement pour VOS données, JAMAIS données externes !

---

## 4. CSV - DONNÉES TABULAIRES <a name="csv"></a>

### Qu'est-ce que CSV ?

**CSV** (Comma-Separated Values) = format texte pour tableaux :
- ✅ Simple et universel
- ✅ Compatible Excel
- ❌ Pas de types (tout en texte)
- ❌ Pas de structure hiérarchique

### Exemple 1 : CSV Basique

```python
import csv

# ÉTAPE 1 : Données tabulaires
employes = [
    ["ID", "Nom", "Poste", "Salaire"],
    [1, "Alice", "Dev", 50000],
    [2, "Bob", "Designer", 45000]
]

# ÉTAPE 2 : Écrire CSV
with open("employes.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(employes)

print("✓ CSV créé")

# ÉTAPE 3 : Lire CSV
with open("employes.csv", "r", encoding="utf-8") as f:
    reader = csv.reader(f)
    for ligne in reader:
        print(ligne)  # Chaque ligne = liste
```

**Points clés :**
- `newline=""` : évite lignes vides sur Windows
- `csv.writer()` : écrit des lignes
- `writerows()` : écrit plusieurs lignes
- `csv.reader()` : lit ligne par ligne

### Exemple 2 : DictReader/DictWriter (Recommandé)

```python
import csv

# ÉTAPE 1 : Données avec clés
produits = [
    {"id": 1, "nom": "Laptop", "prix": 999.99, "stock": 15},
    {"id": 2, "nom": "Souris", "prix": 25.50, "stock": 100}
]

# ÉTAPE 2 : Écrire avec DictWriter
with open("produits.csv", "w", newline="", encoding="utf-8") as f:
    colonnes = ["id", "nom", "prix", "stock"]
    writer = csv.DictWriter(f, fieldnames=colonnes)
    
    writer.writeheader()  # Écrire en-tête
    writer.writerows(produits)

# ÉTAPE 3 : Lire avec DictReader
with open("produits.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)  # Utilise 1ère ligne comme en-têtes
    
    for produit in reader:
        # Chaque ligne = dictionnaire
        print(f"{produit['nom']}: {produit['prix']}€")
```

**Avantages DictReader/Writer :**
- Plus lisible (noms de colonnes)
- Évite erreurs d'index
- Ordre des colonnes garanti

### Exemple 3 : CSV → JSON

```python
import csv
import json

# ÉTAPE 1 : Lire CSV
with open("produits.csv", "r", encoding="utf-8") as f:
    reader = csv.DictReader(f)
    produits = list(reader)

# ÉTAPE 2 : Convertir types (CSV = tout en string)
for p in produits:
    p["id"] = int(p["id"])
    p["prix"] = float(p["prix"])
    p["stock"] = int(p["stock"])

# ÉTAPE 3 : Sauver en JSON
with open("produits.json", "w", encoding="utf-8") as f:
    json.dump(produits, f, indent=4)

print("✓ CSV → JSON terminé")
```

**Important :** CSV lit TOUT en string, il faut convertir manuellement !

---

## 5. XML - FORMAT HIÉRARCHIQUE <a name="xml"></a>

### Qu'est-ce que XML ?

**XML** (eXtensible Markup Language) :
- ✅ Structure hiérarchique riche
- ✅ Auto-descriptif
- ❌ Verbeux
- ❌ Plus complexe que JSON

### Exemple 1 : Créer un XML

```python
import xml.etree.ElementTree as ET

# ÉTAPE 1 : Créer racine
biblio = ET.Element("bibliotheque")

# ÉTAPE 2 : Ajouter livres
livre1 = ET.SubElement(biblio, "livre", id="1")
ET.SubElement(livre1, "titre").text = "1984"
ET.SubElement(livre1, "auteur").text = "George Orwell"
ET.SubElement(livre1, "annee").text = "1949"

livre2 = ET.SubElement(biblio, "livre", id="2")
ET.SubElement(livre2, "titre").text = "Le Petit Prince"
ET.SubElement(livre2, "auteur").text = "Saint-Exupéry"

# ÉTAPE 3 : Créer arbre
arbre = ET.ElementTree(biblio)

# ÉTAPE 4 : Formater et sauvegarder
ET.indent(arbre, space="  ")
arbre.write("biblio.xml", encoding="utf-8", xml_declaration=True)

print("✓ XML créé")
```

**Structure XML résultante :**
```xml
<?xml version='1.0' encoding='utf-8'?>
<bibliotheque>
  <livre id="1">
    <titre>1984</titre>
    <auteur>George Orwell</auteur>
    <annee>1949</annee>
  </livre>
  ...
</bibliotheque>
```

### Exemple 2 : Lire un XML

```python
import xml.etree.ElementTree as ET

# ÉTAPE 1 : Charger XML
arbre = ET.parse("biblio.xml")
racine = arbre.getroot()

print(f"Racine : {racine.tag}")

# ÉTAPE 2 : Parcourir livres
for livre in racine.findall("livre"):
    livre_id = livre.get("id")  # Attribut
    titre = livre.find("titre").text  # Sous-élément
    auteur = livre.find("auteur").text
    annee = livre.find("annee").text
    
    print(f"[{livre_id}] {titre} - {auteur} ({annee})")

# ÉTAPE 3 : Recherche XPath
livres_anciens = racine.findall(".//livre[annee<'1950']")
print(f"Livres avant 1950 : {len(livres_anciens)}")
```

**Méthodes clés :**
- `parse()` : charge fichier XML
- `getroot()` : obtient racine
- `findall()` : trouve tous les éléments
- `find()` : trouve premier élément
- `.get()` : récupère attribut
- `.text` : récupère contenu

### Exemple 3 : XML → JSON

```python
import xml.etree.ElementTree as ET
import json

def xml_to_dict(element):
    result = {}
    
    # Attributs
    if element.attrib:
        result["@attributes"] = element.attrib
    
    # Enfants
    children = list(element)
    if children:
        child_dict = {}
        for child in children:
            child_data = xml_to_dict(child)
            
            # Gérer doublons (créer liste)
            if child.tag in child_dict:
                if not isinstance(child_dict[child.tag], list):
                    child_dict[child.tag] = [child_dict[child.tag]]
                child_dict[child.tag].append(child_data)
            else:
                child_dict[child.tag] = child_data
        
        result.update(child_dict)
    
    # Texte
    if element.text and element.text.strip():
        if len(result) == 0:
            return element.text.strip()
        result["#text"] = element.text.strip()
    
    return result

# Utilisation
arbre = ET.parse("biblio.xml")
racine = arbre.getroot()
data = {racine.tag: xml_to_dict(racine)}

with open("biblio.json", "w", encoding="utf-8") as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print("✓ XML → JSON terminé")
```

---

## 6. SOCKETS - COMMUNICATION RÉSEAU <a name="sockets"></a>

### Qu'est-ce qu'un Socket ?

**Socket** = point de communication réseau :
- Communication client ↔ serveur
- TCP (fiable) ou UDP (rapide)
- Local ou Internet

### Architecture Client-Serveur

```
SERVEUR                    CLIENT
  |                          |
  | 1. socket()              | 1. socket()
  | 2. bind(port)            |
  | 3. listen()              |
  | 4. accept() --------→    | 2. connect()
  |                          |
  | 5. recv/send  ←-------→  | 3. send/recv
  |                          |
  | 6. close()               | 4. close()
```

### Exemple 1 : Serveur Simple

```python
import socket
import json

def serveur():
    # ÉTAPE 1 : Créer socket TCP
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    # ÉTAPE 2 : Réutilisation adresse
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    
    # ÉTAPE 3 : Bind (lier) à adresse:port
    s.bind(("127.0.0.1", 5000))
    
    # ÉTAPE 4 : Écouter (max 5 en attente)
    s.listen(5)
    print("🚀 Serveur démarré sur 127.0.0.1:5000")
    
    while True:
        # ÉTAPE 5 : Accepter connexion
        client, addr = s.accept()
        print(f"✓ Client connecté : {addr}")
        
        # ÉTAPE 6 : Recevoir données
        data = client.recv(4096)
        
        if data:
            message = json.loads(data.decode("utf-8"))
            print(f"Reçu : {message}")
            
            # ÉTAPE 7 : Répondre
            reponse = {
                "status": "ok",
                "message": f"Bonjour {message.get('nom')}"
            }
            client.sendall(json.dumps(reponse).encode("utf-8"))
        
        client.close()

# Lancer : serveur()
```

**Paramètres importants :**
- `AF_INET` : IPv4
- `SOCK_STREAM` : TCP (fiable)
- `SO_REUSEADDR` : redémarrage rapide
- `recv(4096)` : buffer de 4096 bytes

### Exemple 2 : Client Simple

```python
import socket
import json

def client():
    # ÉTAPE 1 : Créer socket
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    try:
        # ÉTAPE 2 : Se connecter
        s.connect(("127.0.0.1", 5000))
        print("✓ Connecté au serveur")
        
        # ÉTAPE 3 : Envoyer données
        message = {"nom": "Alice", "action": "bonjour"}
        s.sendall(json.dumps(message).encode("utf-8"))
        print(f"Envoyé : {message}")
        
        # ÉTAPE 4 : Recevoir réponse
        reponse = s.recv(4096)
        data = json.loads(reponse.decode("utf-8"))
        print(f"Réponse : {data}")
        
    except ConnectionRefusedError:
        print("❌ Serveur non démarré")
    finally:
        s.close()

# Lancer : client()
```

### Exemple 3 : Communication avec Pickle

```python
import socket
import pickle

# === SERVEUR ===
def serveur_pickle():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind(("127.0.0.1", 5001))
    s.listen(5)
    
    print("🚀 Serveur pickle sur port 5001")
    
    client, addr = s.accept()
    print(f"✓ Client : {addr}")
    
    # ÉTAPE 1 : Recevoir taille
    taille_bytes = client.recv(8)
    taille = int.from_bytes(taille_bytes, byteorder="big")
    
    # ÉTAPE 2 : Recevoir données complètes
    data = b""
    while len(data) < taille:
        packet = client.recv(4096)
        if not packet:
            break
        data += packet
    
    # ÉTAPE 3 : Unpickler
    objet = pickle.loads(data)
    print(f"Reçu : {objet}")
    
    client.close()
    s.close()

# === CLIENT ===
def client_pickle():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("127.0.0.1", 5001))
    
    # Objet complexe
    class Personne:
        def __init__(self, nom, age):
            self.nom = nom
            self.age = age
        def __repr__(self):
            return f"Personne({self.nom}, {self.age})"
    
    objet = {"personne": Personne("Bob", 30), "data": [1, 2, 3]}
    
    # Pickler
    data_pickle = pickle.dumps(objet)
    taille = len(data_pickle)
    
    # Envoyer taille puis données
    s.sendall(taille.to_bytes(8, byteorder="big"))
    s.sendall(data_pickle)
    
    print(f"✓ Envoyé ({taille} bytes)")
    s.close()
```

**Protocole de communication :**
1. Envoyer taille (8 bytes)
2. Envoyer données
3. Recevoir taille
4. Recevoir données complètes

---

## 7. APPLICATIONS PRATIQUES <a name="applications"></a>

### Application 1 : Gestionnaire de Configuration

```python
import json
import os

class ConfigManager:
    def __init__(self, fichier="config.json"):
        self.fichier = fichier
        self.config = self.charger()
    
    def charger(self):
        if os.path.exists(self.fichier):
            with open(self.fichier, "r", encoding="utf-8") as f:
                return json.load(f)
        return {
            "app": {"nom": "MonApp", "version": "1.0"},
            "database": {"host": "localhost", "port": 5432}
        }
    
    def sauver(self):
        with open(self.fichier, "w", encoding="utf-8") as f:
            json.dump(self.config, f, indent=4)
    
    def get(self, cle, defaut=None):
        # Ex: get("database.host")
        parties = cle.split(".")
        valeur = self.config
        for p in parties:
            if isinstance(valeur, dict) and p in valeur:
                valeur = valeur[p]
            else:
                return defaut
        return valeur
    
    def set(self, cle, valeur):
        parties = cle.split(".")
        config = self.config
        for p in parties[:-1]:
            if p not in config:
                config[p] = {}
            config = config[p]
        config[parties[-1]] = valeur
        self.sauver()

# Utilisation
cfg = ConfigManager()
print(cfg.get("app.nom"))
cfg.set("app.version", "2.0")
cfg.set("logging.level", "DEBUG")
```

### Application 2 : Cache avec Expiration

```python
import pickle
import time
from datetime import datetime, timedelta

class Cache:
    def __init__(self, fichier="cache.pkl"):
        self.fichier = fichier
        self.cache = self._charger()
    
    def _charger(self):
        try:
            with open(self.fichier, "rb") as f:
                return pickle.load(f)
        except:
            return {}
    
    def _sauver(self):
        with open(self.fichier, "wb") as f:
            pickle.dump(self.cache, f)
    
    def set(self, cle, valeur, ttl=3600):
        exp = datetime.now() + timedelta(seconds=ttl)
        self.cache[cle] = {
            "valeur": valeur,
            "expiration": exp
        }
        self._sauver()
    
    def get(self, cle, defaut=None):
        if cle not in self.cache:
            return defaut
        
        entree = self.cache[cle]
        if datetime.now() > entree["expiration"]:
            del self.cache[cle]
            self._sauver()
            return defaut
        
        return entree["valeur"]
    
    def nettoyer(self):
        now = datetime.now()
        a_supprimer = [k for k, v in self.cache.items()
                      if now > v["expiration"]]
        for k in a_supprimer:
            del self.cache[k]
        if a_supprimer:
            self._sauver()
        return len(a_supprimer)

# Utilisation
cache = Cache()
cache.set("user:123", {"nom": "Alice"}, ttl=60)
user = cache.get("user:123")
print(user)
time.sleep(2)
supprimes = cache.nettoyer()
```

### Application 3 : Mini API REST

```python
import socket
import json
import threading

class APIServeur:
    def __init__(self, port=8000):
        self.port = port
        self.routes = {}
        self.data = {"users": [{"id": 1, "nom": "Alice"}]}
    
    def route(self, path, method="GET"):
        def decorator(func):
            self.routes[(method, path)] = func
            return func
        return decorator
    
    def demarrer(self):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        s.bind(("127.0.0.1", self.port))
        s.listen(5)
        
        print(f"🚀 API sur http://127.0.0.1:{self.port}")
        
        while True:
            client, addr = s.accept()
            threading.Thread(target=self._gerer, args=(client,)).start()
    
    def _gerer(self, client):
        try:
            req = client.recv(4096).decode()
            if not req:
                return
            
            ligne = req.split("\n")[0].split()
            if len(ligne) < 2:
                return
            
            method, path = ligne[0], ligne[1]
            handler = self.routes.get((method, path))
            
            if handler:
                data = handler()
                json_data = json.dumps(data)
                resp = (
                    "HTTP/1.1 200 OK\r\n"
                    "Content-Type: application/json\r\n"
                    f"Content-Length: {len(json_data)}\r\n"
                    "\r\n"
                    f"{json_data}"
                )
            else:
                json_data = json.dumps({"error": "Not found"})
                resp = (
                    "HTTP/1.1 404 Not Found\r\n"
                    "Content-Type: application/json\r\n"
                    f"Content-Length: {len(json_data)}\r\n"
                    "\r\n"
                    f"{json_data}"
                )
            
            client.sendall(resp.encode())
        finally:
            client.close()

# Utilisation
api = APIServeur()

@api.route("/", "GET")
def index():
    return {"message": "API v1.0"}

@api.route("/users", "GET")
def get_users():
    return api.data["users"]

# api.demarrer()
```

---

## 📊 TABLEAU COMPARATIF

| Format | Lisible | Universel | Types | Vitesse | Usage |
|--------|---------|-----------|-------|---------|-------|
| JSON | ✅ Oui | ✅ Oui | ❌ Limité | ⚡ Moyen | APIs, configs |
| Pickle | ❌ Non | ❌ Python | ✅ Tous | ⚡⚡ Rapide | Cache Python |
| CSV | ✅ Oui | ✅ Oui | ❌ String | ⚡ Lent | Excel, data |
| XML | ✅ Oui | ✅ Oui | ❌ Limité | ⚡ Lent | Standards |

---

## ✅ BONNES PRATIQUES

### Choix du Format
- **API web** → JSON
- **Cache interne** → Pickle
- **Export Excel** → CSV
- **Échange standardisé** → XML

### Sécurité
1. ✅ JSON : sûr pour données externes
2. ⚠️ Pickle : JAMAIS avec données non fiables
3. ✅ CSV : sûr (attention injections formules)
4. ✅ XML : sûr (attention XML bombs)

### Performance
```python
import timeit

# Benchmark
data = {"key": "value"} * 1000

json_time = timeit.timeit(lambda: json.dumps(data), number=1000)
pickle_time = timeit.timeit(lambda: pickle.dumps(data), number=1000)

# Pickle = 2-3x plus rapide
```

---

## 🎯 EXERCICES

### Exercice 1 : TODO List
Créez un système TODO avec :
- Sauvegarde JSON
- Export CSV
- Ajout/suppression/modification

### Exercice 2 : Cache Intelligent
Créez un décorateur qui :
- Cache résultats avec Pickle
- Expiration automatique
- Arguments comme clés

### Exercice 3 : Chat Client/Serveur
Application chat avec :
- Serveur multi-clients
- Messages en JSON
- Historique en CSV

---

## 🎓 CONCLUSION

Vous maîtrisez maintenant :
- ✅ JSON pour interopérabilité
- ✅ Pickle pour persistance Python
- ✅ CSV pour tableaux
- ✅ XML pour hiérarchies
- ✅ Sockets pour réseau
- ✅ Applications pratiques

**Prochaines étapes :**
- Bases de données (SQLite, PostgreSQL)
- Frameworks web (Flask, FastAPI)
- Protocols modernes (gRPC, WebSocket)