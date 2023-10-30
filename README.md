# TP Flask

## Introduction
Ce projet consistait à créer une application web codée en Flask. Ce travail était individuel et nous pouvions reprendre le travail que nous avions réalisé lors des cours de TD.

## L'application web
Cette application peut être considérée comme une bibliothèque en ligne.
Nous avions à notre disposition un fichier .yml contenant des livres et leurs auteurs.
L'utilisateur pourra donc consulter les informations concernant les livres : 
- le nom de l'auteur
- l'image de couverture
- le prix
- un lien vers un site externe si jamais l'utilisateur souhaite se procurer ce livre

Mais il pourra également consulter les informations relatives à l'auteur d'une oeuvre qui lui aurait plu :
- son nom
- la liste des livres que l'auteur a écrit

L'application possède un système de connexion qui permet plusieurs choses à son utilisateur. Il lui sera possible de modifier un auteur, d'en ajouter un ou d'ajouter un livre.

## Implémentation
Je me suis mise en retard sur ce tp puisque j'ai recommencé un bon nombre de fois les td à cause de problèmes dont je ne trouvais pas la solution.

J'ai cependant essayé de faire en sorte que l'application puisse permettre à un utilisateur de modifier un auteur, d'ajouter un auteur ou un livre et de se connecter (et de pouvoir accéder aux fonctionnalités qui sont réservées aux utilisateurs authentifiés).

## Installations nécessaires au préalable

Pour s'assurer que l'application web fonctionne correctement, vous pouvez créer un environnement virtuel avec cette commande : `virtualenv -p python3 venv`

Pour démarrer cet environnement, suivant votre système d'exploitation la commande diffère un peu :
- Sous Windows : `source venv/Scripts/activate`
- Sous Linux : `source venv/bin/activate`

Ensuite, il vous faudra installer plusieurs extensions :
- flask
- python-dotenv
- flask-sqlalchemy
- flask-wtf
- flask-login
- pyYAML

Il faudra charger une base de données à partir du fichier data.yml à l'aide de la commande suivante : `flask loaddb data.yml`
(Assurez vous que la commande loaddb s'affiche lorsque que entrez `flask` dans votre terminal).
