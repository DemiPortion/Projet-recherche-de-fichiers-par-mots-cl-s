# Projet : Gestion d'une Bibliothèque 📚

---

## 1. MCD de la Bibliothèque

### **Entités et Attributs**

- **LIVRE** :  
  `Titre_Livre`, `ISBN`, `Langue`, `Annee_Publication`, `Resume`, `Nombre_Exemplaires`, `Date_Ajout`, `Prix_Livre`
- **AUTEUR** :  
  `Nom_Auteur`, `Prenom_Auteur`, `Nationalite_Auteur`, `Date_Naissance`, `Bibliographie`
- **EDITEUR** :  
  `Nom_Editeur`, `Adresse_Editeur`, `Contact_Editeur`, `Site_Web`
- **CATEGORIE** :  
  `Nom_Categorie`, `Description_Categorie`
- **GENRE** :  
  `Nom_Genre`
- **USAGER** :  
  `Nom_Usager`, `Prenom_Usager`, `Adresse_Usager`, `Telephone_Usager`, `Email_Usager`, `Date_Inscription`, `Statut`, `Date_Dernier_Emprunt`
- **EMPLOYE** :  
  `Nom_Employe`, `Prenom_Employe`, `Poste_Employe`, `Contact_Employe`, `Identifiant_Employe`, `Mot_de_Passe`, `Date_Embauche`, `Salaire`
- **SOCIETE** :  
  `Nom_Societe`, `Raison_Sociale`, `Adresse_Societe`

---

### **Relations**

- **ECRIT_PAR** : 0,N AUTEUR ↔ 1,N LIVRE  
- **PUBLIE_PAR** : 1,N LIVRE ↔ 1,N EDITEUR  
- **CATEGORISE_DANS** : 1,N LIVRE ↔ 1,N CATEGORIE  
- **LIE_AU_GENRE** : 1,N LIVRE ↔ 0,N GENRE  
- **EMPRUNTER** : 1,N USAGER ↔ 0,N LIVRE (`Date_Emprunt`, `Date_Retour_Prevu`, `Date_Retour_Reel`, `Statut_Emprunt`, `Frais_Retard`)  
- **RESERVER** : 1,N USAGER ↔ 0,N LIVRE (`Date_Reservation`, `Statut_Reservation`, `Date_Expiration`)  
- **VEND** : 1,N EMPLOYE ↔ 0,N LIVRE  
- **TRAVAILLER_DANS** : 0,N EMPLOYE ↔ 1,N SOCIETE  

---

## 2. Création des Tables SQL 🛠️

```sql
CREATE TABLE LIVRE (
    ID_Livre INT PRIMARY KEY AUTO_INCREMENT,
    Titre_Livre VARCHAR(255) NOT NULL,
    ISBN VARCHAR(20) NOT NULL UNIQUE,
    Langue VARCHAR(50),
    Annee_Publication YEAR,
    Resume TEXT,
    Nombre_Exemplaires INT DEFAULT 1,
    Date_Ajout DATE,
    Prix_Livre DECIMAL(10, 2)
);

Table AUTEUR
sql


CREATE TABLE AUTEUR (
    ID_Auteur INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Auteur VARCHAR(100) NOT NULL,
    Prenom_Auteur VARCHAR(100),
    Nationalite_Auteur VARCHAR(50),
    Date_Naissance DATE,
    Bibliographie TEXT
);
Table EDITEUR
sql


CREATE TABLE EDITEUR (
    ID_Editeur INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Editeur VARCHAR(100) NOT NULL,
    Adresse_Editeur TEXT,
    Contact_Editeur VARCHAR(100),
    Site_Web VARCHAR(255)
);
Table CATEGORIE
sql


CREATE TABLE CATEGORIE (
    ID_Categorie INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Categorie VARCHAR(100) NOT NULL,
    Description_Categorie TEXT
);
Table GENRE
sql


CREATE TABLE GENRE (
    ID_Genre INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Genre VARCHAR(100) NOT NULL
);
Table USAGER
sql


CREATE TABLE USAGER (
    ID_Usager INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Usager VARCHAR(100) NOT NULL,
    Prenom_Usager VARCHAR(100),
    Adresse_Usager TEXT,
    Telephone_Usager VARCHAR(15),
    Email_Usager VARCHAR(100) UNIQUE,
    Date_Inscription DATE NOT NULL,
    Statut ENUM('Actif', 'Suspendu', 'Inactif') DEFAULT 'Actif',
    Date_Dernier_Emprunt DATE
);
Table EMPLOYE
sql


CREATE TABLE EMPLOYE (
    ID_Employe INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Employe VARCHAR(100) NOT NULL,
    Prenom_Employe VARCHAR(100),
    Poste_Employe VARCHAR(50),
    Contact_Employe VARCHAR(100),
    Identifiant_Employe VARCHAR(50) UNIQUE,
    Mot_de_Passe VARCHAR(255),
    Date_Embauche DATE,
    Salaire DECIMAL(10, 2)
);
Table SOCIETE
sql


CREATE TABLE SOCIETE (
    ID_Societe INT PRIMARY KEY AUTO_INCREMENT,
    Nom_Societe VARCHAR(100) NOT NULL,
    Raison_Sociale VARCHAR(255),
    Adresse_Societe TEXT
);
```

## 3. Création de la Base de Données PostgreSQL

### Instructions SQL

```sql
CREATE DATABASE bibliotheque;
CREATE USER bibliouser WITH PASSWORD '1234';
GRANT ALL PRIVILEGES ON DATABASE bibliotheque TO bibliouser;
```

## 4. Application Flask 🌐
Fichier : app.py

```sql
from flask import Flask, render_template, request
import psycopg2

app = Flask(__name__)

DB_CONFIG = {
    "dbname": "bibliotheque",
    "user": "bibliouser",
    "password": "1234",
    "host": "localhost",
    "port": 5432
}

@app.route("/", methods=["GET", "POST"])
def index():
    search_query = request.form.get("search")
    books = []
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cursor = conn.cursor()

        if search_query:
            query = """
                SELECT livre.titre_livre, auteur.nom_auteur, auteur.prenom_auteur, livre.prix_livre, livre.isbn
                FROM livre
                JOIN ecrit_par ON livre.id_livre = ecrit_par.id_livre
                JOIN auteur ON auteur.id_auteur = ecrit_par.id_auteur
                WHERE livre.titre_livre ILIKE %s OR auteur.nom_auteur ILIKE %s
                ORDER BY livre.titre_livre;
            """
            cursor.execute(query, (f"%{search_query}%", f"%{search_query}%"))
        else:
            query = """
                SELECT livre.titre_livre, auteur.nom_auteur, auteur.prenom_auteur, livre.prix_livre, livre.isbn
                FROM livre
                JOIN ecrit_par ON livre.id_livre = ecrit_par.id_livre
                JOIN auteur ON auteur.id_auteur = ecrit_par.id_auteur
                ORDER BY livre.titre_livre;
            """
            cursor.execute(query)

        books = cursor.fetchall()
        cursor.close()
        conn.close()
    except Exception as e:
        print(f"Erreur : {e}")

    return render_template("index.html", books=books, search_query=search_query)

if __name__ == "__main__":
    app.run(debug=True)
```

## 5. Génération Automatique de Données avec Faker 🛠️

```sql
Fichier : faker_script.py
python
Copier
Modifier
import psycopg2
from faker import Faker
from tqdm import tqdm
import random

DB_CONFIG = {
    "dbname": "bibliotheque",
    "user": "bibliouser",
    "password": "1234",
    "host": "localhost",
    "port": 5432
}

fake = Faker('fr_FR')

def ajouter_livres(nb_livres):
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        cur = conn.cursor()

        for _ in tqdm(range(nb_livres)):
            titre = fake.sentence(nb_words=4)
            isbn = fake.isbn13(separator="-")
            langue = random.choice(["Français", "Anglais", "Espagnol"])
            annee = random.randint(1900, 2023)
            resume = fake.text(max_nb_chars=200)
            prix = round(random.uniform(5.0, 50.0), 2)

            cur.execute("""
                INSERT INTO livre (titre_livre, isbn, langue, annee_publication, resume, prix_livre)
                VALUES (%s, %s, %s, %s, %s, %s);
            """, (titre, isbn, langue, annee, resume, prix))

        conn.commit()
    except Exception as e:
        print(f"Erreur : {e}")
    finally:
        if 'cur' in locals() and cur:
            cur.close()
        if 'conn' in locals() and conn:
            conn.close()

if __name__ == "__main__":
    nb_livres = int(input("Combien de livres voulez-vous ajouter ? "))
    ajouter_livres(nb_livres)

```