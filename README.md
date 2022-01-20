# Démo pour Vincent: upload de données et choix des colonnes à afficher

<object width="425" height="344"><param name="movie" value="https://www.youtube.com/v/mycMVp-ggTE&hl=en&fs=1"></param><param name="allowFullScreen" value="true"></param><embed src="https://www.youtube.com/v/mycMVp-ggTE&hl=en&fs=1" type="application/x-shockwave-flash" allowfullscreen="true" width="425" height="344"></embed></object>

Ce projet est une démonstration pour montrer une manière de faire possible pour uploader un fichier
CSV et laisser à l'utilisateur le soin de sélectionner les colonnes du fichier à afficher.

## Installation des dépendances

La procédure d'installation est classique:

1. Cloner ce projet depuis github
2. Créer et activer un environnement virtuel
3. Depuis la racine du projet, exécuter la commande `$ pip install -r requirements.txt`
4. Exécuter les migrations avec la commande `$ python manage.py migrate`
5. Lancer le serveur de développement avec `$ python manage.py runserver`
6. Rendez-vous sur http://localhost:8000 et suivez les instructions (le fichier à uploader pour le test est createurs.csv)
