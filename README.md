# Documentation : Application de Gestion de Fichiers

## Introduction

Cette application de gestion de fichiers est un outil conçu pour rechercher et visualiser vos fichiers à travers différents répertoires de manière efficace. Elle permet également d'ajouter des fichiers en favoris, d'explorer l'historique des recherches et de filtrer les résultats en fonction de critères tels que le type de fichier.

## Objectifs de l'application

L'objectif principal est de fournir une interface simple et intuitive pour :

- Rechercher des fichiers dans un répertoire donné ou sur le disque entier.
- Filtrer les résultats par type de fichier.
- Accéder rapidement à des fichiers souvent utilisés grâce aux favoris.
- Enregistrer et réutiliser des recherches grâce à l'historique.
- Simplifier la gestion des fichiers pour les utilisateurs n'ayant pas besoin de manipulations complexes.

## Fonctionnalités principales

### Recherche de fichiers :

- Permet de rechercher des fichiers par mot-clé.
- Possibilité de filtrer par type de fichier : PDF, Word, Excel, texte, etc.
- Recherche dans le contenu des fichiers (indexation).

### Gestion des favoris :

- Ajouter des fichiers en favoris.
- Les consulter dans une section dédiée.
- Ouvrir les fichiers directement depuis la liste des favoris.

### Historique des recherches :

- Suivi des mots-clés utilisés dans les recherches précédentes.
- Rechercher à nouveau en un clic.

### Interface intuitive :

- Présentation claire des favoris, des résultats et de l'historique.
- Utilisation d'un design moderne et accessible.

## Comment utiliser l'application

### 1. Lancer l'application

1. Assurez-vous que Python est installé sur votre machine.
2. Installez les bibliothèques nécessaires :
   ```bash
   pip install flask
   ```
3. Lancez le serveur avec la commande suivante :
   ```bash
   python main.py
   ```
4. Accédez à l'application via votre navigateur à l'adresse suivante :
   [http://localhost:5000](http://localhost:5000).

### 2. Rechercher des fichiers

- Entrez un mot-clé dans la barre de recherche.
- Utilisez le menu déroulant pour sélectionner un type de fichier (facultatif).
- Cliquez sur **Rechercher** pour afficher les résultats.

### 3. Gérer les favoris

- Dans les résultats de recherche, cliquez sur **Ajouter aux favoris** pour conserver un fichier.
- Accédez à vos favoris dans la barre latérale gauche.
- Ouvrez ou supprimez un fichier favori directement depuis cette liste.

### 4. Consulter l'historique

- La barre latérale droite affiche les recherches récentes.
- Cliquez sur un élément de l'historique pour relancer une recherche avec le même mot-clé.

### 5. Changer le répertoire de recherche

- En haut de la page, entrez le chemin d'un répertoire personnalisé dans la barre de chemin.
- Cliquez sur **Appliquer** pour sauvegarder ce chemin et effectuer des recherches dans ce répertoire.

## Structure du projet

### Fichiers principaux

- **main.py** :
  - Point d'entrée de l'application Flask.
  - Gère les routes principales, les actions de recherche et la gestion des favoris.

- **search.py** :
  - Contient la logique pour rechercher dans les fichiers indexés.
  - Inclut les fonctionnalités de filtrage par type et date.

- **indexer.py** :
  - Lit le contenu des fichiers pour créer un index JSON.
  - Permet une recherche rapide dans le contenu des fichiers.

- **favorites.py** :
  - Ajoute et supprime des fichiers dans une liste de favoris sauvegardée en JSON.

### Dossiers importants

- **static/** : Contient les fichiers CSS pour le style de l'application.
- **templates/** : Regroupe les fichiers HTML pour l'interface utilisateur.
- **index/** : Stocke les fichiers d'indexation et les données persistantes comme les favoris.
  
## Défis rencontrés et solutions

### Gestion des filtres
1. **Problème : Les résultats ne respectaient pas toujours les critères de filtrage.**
   - Initialement, les fichiers retournés par la recherche incluaient des types de fichiers non sélectionnés dans les filtres.
   - **Solution :** Une vérification stricte a été ajoutée dans la logique de filtrage (`search_in_index`). Nous avons vérifié si le type de fichier correspondait précisément au critère sélectionné par l'utilisateur. Cette vérification a été faite via l'extension du fichier (`file_ext.lower()`).

2. **Problème : Le filtrage par contenu ne fonctionnait pas correctement.**
   - Les mots-clés n'étaient pas recherchés efficacement dans le contenu des fichiers indexés.
   - **Solution :** L'indexation a été améliorée pour inclure non seulement les chemins des fichiers mais également leur contenu, grâce à une fonction de lecture de fichiers dans `indexer.py`.

### Gestion des favoris
1. **Problème : Ajout et suppression non fonctionnels.**
   - Lorsque l'utilisateur tentait d'ajouter ou de supprimer un favori, l'action ne s'exécutait pas correctement, et parfois rien ne se passait.
   - **Solution :** 
     - L'utilisation de méthodes `POST` avec des boutons spécifiques a été mise en œuvre pour gérer séparément l'ajout et la suppression.
     - Une logique conditionnelle stricte a été introduite pour s'assurer que chaque action est bien exécutée.

2. **Problème : Visualisation des favoris dans l'interface (`index.html`).**
   - Les favoris étaient affichés sous forme d'étoiles (⭐), ce qui n'était pas intuitif pour l'utilisateur.
   - **Solution :** Un bouton "Ouvrir" a été ajouté à chaque favori, rendant l'interface plus claire et plus fonctionnelle.

3. **Problème : Les favoris supprimés réapparaissaient après un rechargement de la page.**
   - Cela se produisait en raison d'une gestion incorrecte du fichier JSON contenant les favoris.
   - **Solution :** La gestion des fichiers JSON a été optimisée pour garantir une lecture et une écriture cohérentes à chaque opération.

### Résumé des solutions techniques
- Les fonctions de recherche ont été renforcées par une validation stricte des critères.
- La gestion des favoris repose sur des fichiers JSON, garantissant une persistance fiable des données.
- L'interface utilisateur a été adaptée pour améliorer l'expérience utilisateur, notamment avec des boutons clairs et des espaces bien gérés.

Ces améliorations permettent désormais une utilisation fluide et intuitive de l'application, tout en s'assurant que chaque fonctionnalité fonctionne comme prévu.

## Pourquoi ces choix ?

### Flask :

- Léger et rapide à mettre en place.
- Parfait pour une application locale ou un prototype simple.

### Indexation JSON :

- Utiliser un fichier JSON pour indexer les fichiers permet une recherche rapide sans base de données.
- Facile à sauvegarder et à partager.

### Favoris et historique :

- Conçus pour améliorer la productivité en gardant une trace des fichiers et des recherches.

### Interface utilisateur :

- Basée sur HTML et CSS simples pour garantir une bonne compatibilité.
- Design moderne et minimaliste pour une expérience agréable.

## Améliorations possibles

### Support des fichiers compressés :

- Ajouter la capacité de rechercher dans les fichiers ZIP ou autres archives.

### Affichage avancé :

- Inclure des aperçus pour certains types de fichiers (PDF, images).

### Recherche multi-critères :

- Permettre la recherche par taille ou date directement depuis l'interface.

### Notifications visuelles :

- Ajouter des notifications contextuelles pour informer l'utilisateur (succès, erreurs).

### Support multi-utilisateur :

- Sauvegarder des favoris et des historiques spécifiques à un utilisateur.

## Conclusion

Cette application fournit une solution simple mais puissante pour la gestion des fichiers. Grâce à ses fonctionnalités d'indexation et de filtrage, elle permet de gagner du temps et d'améliorer l'organisation personnelle. Avec quelques améliorations, elle pourrait devenir un outil indispensable pour les utilisateurs ayant de nombreux fichiers à gérer.
