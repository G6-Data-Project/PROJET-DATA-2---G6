# Projet IA1 - Exploitation de l'API de Football pour l'Identification de Talents

## Équipe
- Abraham RAMAROSANDY (STD 21017)
- Fabien MALALA-ZO Raharison (STD 21101)
- Vohizy ANDRIATSIMIADY Ramiandrisoa (STD 21005)
- Mirado RAHARINAIVOSOA Radintsoa (STD 21081)

## Contexte
Dans le cadre du projet IA1, notre équipe se concentre sur l'exploitation de l'API de football pour affiner la recherche de futurs talents dans le monde du football. L'objectif est de simplifier le processus de recrutement de joueurs en identifiant les talents émergents. L'API ciblée est la suivante : [Lien vers l'API Football](https://apifootball.com/documentation/?gclid=CjwKCAjw8symBhAqEiwAaTA__FHopu1tvtKPyd9Kq2CkYNy4z1voKLIXDjwRvuOmvwmhqVebHnzE-RoC6ngQAvD_BwE)

## Technologies
Nous avons convenu d'utiliser les outils et langages suivants :
- Langage de script : Python
- Visualisation des données : Tableau
- Stockage : Service Amazon S3 d'Amazon Web Services

## Tâches
La répartition des tâches s'est effectuée au sein de notre organisation GitHub, utilisant l'outil Project. Voici la composition de notre équipe :
- Abraham : Full-Stack 
- Fabien : Product Owner
- Vohizy : Opérations (OPS)
- Mirado : Backend

## Processus

### Extraction des Données de l'API
Nous avons créé un code pour extraire les informations nécessaires de l'API football et les convertir en format .csv. Nous avons obtenu les informations en interrogeant les ligues, les équipes et les joueurs, puis les avons stockées dans un fichier .csv.

### Transformation des Données
Nous avons appliqué des filtres pour identifier les caractéristiques générales recherchées chez les joueurs professionnels. Ensuite, nous avons extrait les meilleurs joueurs pour chaque poste et calculé un score basé sur leurs statistiques. Ceci nous a permis de créer un classement des meilleurs joueurs par poste.

### Orchestration via Apache Airflow
Nous avons créé une DAG (Directed Acyclic Graph) pour automatiser l'extraction et la transformation des données toutes les 3 mois. La DAG configure l'exécution des tâches nécessaires, de l'import des dépendances à la connexion avec Amazon S3.

## Lien vers le Projet GitHub
Pour une vue détaillée de notre projet et de la répartition des tâches, vous pouvez consulter le lien suivant : [Projet GitHub - Groupe 6](https://github.com/orgs/G6-Data-Project/projects/1/views/1)

*Ce document a été créé et validé par l'équipe du Projet IA1 - Groupe 6.*
