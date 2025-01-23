# Documentation : Application de Gestion de Fichiers

## Introduction
Cette application de gestion de fichiers est un outil conçu pour rechercher et visualiser vos fichiers à travers différents répertoires de manière efficace. Elle permet également d'ajouter des fichiers en favoris, d'explorer l'historique des recherches et de filtrer les résultats en fonction de critères tels que le type de fichier.

## Objectifs de l'application
L'objectif principal est de fournir une interface simple et intuitive pour :

- **Rechercher** des fichiers dans un répertoire donné ou sur le disque entier.
- **Filtrer** les résultats par type de fichier.
- **Accéder rapidement** à des fichiers souvent utilisés grâce aux favoris.
- **Enregistrer et réutiliser** des recherches grâce à l'historique.
- **Simplifier** la gestion des fichiers pour les utilisateurs n'ayant pas besoin de manipulations complexes.

## Fonctionnalités principales
1. **Recherche de fichiers** :
   - Permet de rechercher des fichiers par mot-clé.
   - Possibilité de filtrer par type de fichier : PDF, Word, Excel, texte, etc.
   - Recherche dans le contenu des fichiers (indexation).

2. **Gestion des favoris** :
   - Ajouter des fichiers en favoris.
   - Les consulter dans une section dédiée.
   - Ouvrir les fichiers directement depuis la liste des favoris.

3. **Historique des recherches** :
   - Suivi des mots-clés utilisés dans les recherches précédentes.
   - Rechercher à nouveau en un clic.

4. **Interface intuitive** :
   - Présentation claire des favoris, des résultats et de l'historique.
   - Utilisation d'un design moderne et accessible.

---

## Comment utiliser l'application

### 1. **Lancer l'application**
1. Assurez-vous que Python est installé sur votre machine.
2. Installez les bibliothèques nécessaires (si ce n'est pas déjà fait) en exécutant :
   ```bash
   pip install flask
   ```
3. Lancez le serveur avec :
   ```bash
   python main.py
   ```
4. Accédez à l'application via votre navigateur à l'adresse suivante :
   ```
   http://localhost:5000
   ```

### 2. **Rechercher des fichiers**
1. Entrez un mot-clé dans la barre de recherche.
2. Utilisez le menu déroulant pour sélectionner un type de fichier (facultatif).
3. Cliquez sur **Rechercher** pour afficher les résultats.

### 3. **Gérer les favoris**
1. Dans les résultats de recherche, cliquez sur **Ajouter aux favoris** pour conserver un fichier.
2. Accédez à vos favoris dans la barre latérale gauche.
3. Ouvrez ou supprimez un fichier favori directement depuis cette liste.

### 4. **Consulter l'historique**
1. La barre latérale droite affiche les recherches récentes.
2. Cliquez sur un élément de l'historique pour relancer une recherche avec le même mot-clé.

---

## Structure du projet

### Fichiers principaux
- **`main.py`** :
  - Point d'entrée de l'application Flask.
  - Gère les routes principales, les actions de recherche et la gestion des favoris.

- **`search.py`** :
  - Contient la logique pour rechercher dans les fichiers indexés.
  - Inclut les fonctionnalités de filtrage par type et date.

- **`indexer.py`** :
  - Lit le contenu des fichiers pour créer un index JSON.
  - Permet une recherche rapide dans le contenu des fichiers.

- **`favorites.py`** :
  - Ajoute et supprime des fichiers dans une liste de favoris sauvegardée en JSON.

- **Dossiers importants** :
  - **`static/`** : Contient les fichiers CSS pour le style de l'application.
  - **`templates/`** : Regroupe les fichiers HTML pour l'interface utilisateur.
  - **`index/`** : Stocke les fichiers d'indexation et les données persistantes comme les favoris.

---

## Pourquoi ces choix ?

1. **Flask** :
   - Léger et rapide à mettre en place.
   - Parfait pour une application locale ou un prototype simple.

2. **Indexation JSON** :
   - Utiliser un fichier JSON pour indexer les fichiers permet une recherche rapide sans base de données.
   - Facile à sauvegarder et à partager.

3. **Favoris et historique** :
   - Conçus pour améliorer la productivité en gardant une trace des fichiers et des recherches.

4. **Interface utilisateur** :
   - Basée sur HTML et CSS simples pour garantir une bonne compatibilité.
   - Design moderne et minimaliste pour une expérience agréable.

---

## Améliorations possibles
1. **Support des fichiers compressés** :
   - Ajouter la capacité de rechercher dans les fichiers ZIP ou autres archives.

2. **Affichage avancé** :
   - Inclure des aperçus pour certains types de fichiers (PDF, images).

3. **Recherche multi-critères** :
   - Permettre la recherche par taille ou date directement depuis l'interface.

4. **Notifications visuelles** :
   - Ajouter des notifications contextuelles pour informer l'utilisateur (succès, erreurs).

5. **Support multi-utilisateur** :
   - Sauvegarder des favoris et des historiques spécifiques à un utilisateur.

---

## Conclusion
Cette application fournit une solution simple mais puissante pour la gestion des fichiers. Grâce à ses fonctionnalités d'indexation et de filtrage, elle permet de gagner du temps et d'améliorer l'organisation personnelle. Avec quelques améliorations, elle pourrait devenir un outil indispensable pour les utilisateurs ayant de nombreux fichiers à gérer.

