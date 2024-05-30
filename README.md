# Projet de Crawleur Web Multithreadé

Ce projet est un crawleur web multithreadé développé en Python. Le crawleur explore des sites web, extrait les titres des pages, et enregistre ces titres dans un fichier CSV. Il est conçu pour crawler un nombre limité d'URLs et utilise plusieurs threads pour améliorer l'efficacité et la vitesse du crawling.

## Fonctionnalités

- **Exploration des URLs** : Exploration de pages web à partir d'URLs initiales.
- **Extraction des Titres** : Extraction des titres des pages HTML.
- **Respect des Règles de Robots** : Respect des directives des fichiers `robots.txt` des sites web.
- **Multithreading** : Utilisation de plusieurs threads pour accélérer le processus de crawling.
- **Stockage des Résultats** : Enregistrement des résultats dans un fichier CSV.
- **Calcul du Temps d'Exécution** : Mesure du temps total d'exécution du script.

## Prérequis

- Python 3.x
- Bibliothèques : `requests`, `beautifulsoup4`

## Installation

1. **Cloner le repository** :

    ```bash
    git clone https://github.com/votre-nom-utilisateur/web-crawler-project.git
    cd web-crawler-project
    ```

2. **Installer les dépendances** :

    ```bash
    pip install -r requirements.txt
    ```

## Utilisation

1. **Exécuter le script principal** pour lancer le crawleur :

    ```bash
    python long_crawler.py
    ```

    Le script commencera à explorer les URLs spécifiées et enregistrera les titres des pages dans un fichier CSV nommé `crawl_results.csv`.

## Détails du Code

### Variables et Initialisation

- **NUM_THREADS** : Nombre de threads utilisés pour le crawling.
- **MAX_URLS** : Limite le nombre total d'URLs à crawler à 50 pour limiter le temps d'exécution.
- **url_queue** : Une file d'attente pour stocker les URLs à crawler.
- **visited_urls** : Un ensemble pour suivre les URLs déjà visitées et éviter les doublons.
- **initial_urls** : Une liste d'URLs de départ pour commencer le crawling.
- **output_file** : Nom du fichier CSV où les résultats seront enregistrés.

### Fonction `can_fetch`

Vérifie les directives du fichier `robots.txt` d'un site web pour déterminer si le crawling est autorisé pour une URL donnée.

### Fonction `crawl`

1. Vérifie si le crawling est autorisé avec `can_fetch`.
2. Télécharge le contenu de la page avec `requests.get`.
3. Analyse le HTML pour extraire le titre de la page avec `BeautifulSoup`.
4. Utilise un verrou (`threading.Lock`) pour écrire de manière sûre dans le fichier CSV depuis plusieurs threads.
5. Trouve les liens internes sur la page et les ajoute à la file d'attente si elles n'ont pas encore été visitées et que le nombre total d'URLs visitées est inférieur à `MAX_URLS`.

### Fonction `worker`

1. Récupère une URL de la file d'attente.
2. Appelle la fonction `crawl` pour traiter l'URL.
3. Introduit un délai de 0.5 seconde entre les requêtes pour réduire la charge sur les serveurs web.
4. Indique que la tâche pour cette URL est terminée.

### Fonction `main`

1. Capture le temps de début de l'exécution.
2. Crée et démarre plusieurs threads (NUM_THREADS).
3. Ajoute les URLs initiales à la file d'attente et les marque comme visitées.
4. Attend que toutes les tâches dans la file d'attente soient complétées.
5. Met un `None` dans la file d'attente pour chaque thread pour les arrêter.
6. Calcule et affiche le temps total d'exécution du script.

## Exemples d'Utilisation

1. **Exploration de Wikipédia et Reddit** :

    Les URLs initiales incluent des sites populaires comme Wikipédia et Reddit, ce qui permet de démontrer le fonctionnement du crawleur sur des sites web bien connus.

2. **Extension et Adaptation** :

    Vous pouvez facilement adapter ce projet pour crawler d'autres sites web en modifiant la liste `initial_urls` et en ajustant les paramètres de crawling selon vos besoins.

## Auteurs

- Imtinen (https://github.com/votre-nom-utilisateur)



