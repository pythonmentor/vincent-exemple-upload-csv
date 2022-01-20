# Démo pour Vincent: upload de données et choix des colonnes à afficher

Ce projet est une démonstration pour montrer une manière de faire possible pour uploader un fichier
CSV et laisser à l'utilisateur le soin de sélectionner les colonnes du fichier à afficher.

## Installation des dépendances

La procédure d'installation est classique:

1. cloner ce projet depuis github
2. créer et activer un environnement virtuel
3. depuis la racine du projet, exécuter la commande `$ pip install -r requirements.txt`
4. Exécuter les migrations avec la commande `$ python manage.py migrate`
5. Lancer le serveur de développement avec `$ python manage.py runserver`
6. Rendez-vous sur http://localhost:8000 et suivez les instructions (le fichier à uploader pour le test est createurs.csv)