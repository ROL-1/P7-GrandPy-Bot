# GrandPy Bot, le papy-robot 
Il s'agit d'un projet d'apprentissage.
Projet 7 du parcours développeur d'application d'Openclassrooms
https://openclassrooms.com/fr/paths/322-developpeur-dapplication-python

-----------------
## Cahier des charges
### Fonctionnalités

    Interactions en AJAX : l'utilisateur envoie sa question en appuyant sur entrée et la réponse s'affiche directement dans l'écran, sans recharger la page.
    Vous utiliserez l'API de Google Maps et celle de Media Wiki.
    Rien n'est sauvegardé. Si l'utilisateur charge de nouveau la page, tout l'historique est perdu.
    Vous pouvez vous amuser à inventer plusieurs réponses différentes de la part de GrandPy mais ce n'est pas une obligation. Amusez-vous !

### Parcours utilisateur

L'utilisateur ouvre son navigateur et entre l'URL que vous lui avez fournie. Il arrive devant une page contenant les éléments suivants :

    header : logo et phrase d'accroche
    zone centrale : zone vide (qui servira à afficher le dialogue) et champ de formulaire pour envoyer une question.
    footer : votre prénom & nom, lien vers votre repository Github et autres réseaux sociaux si vous en avez

L'utilisateur tape "Salut GrandPy ! Est-ce que tu connais l'adresse d'OpenClassrooms ?" dans le champ de formulaire puis appuie sur la touche Entrée. Le message s'affiche dans la zone du dessus qui affiche tous les messages échangés. Une icône tourne pour indiquer que GrandPy est en train de réfléchir.

Puis un nouveau message apparaît : "Bien sûr mon poussin ! La voici : 7 cité Paradis, 75010 Paris." En-dessous, une carte Google Maps apparaît également avec un marqueur indiquant l'adresse demandée.

GrandPy envoie un nouveau message : "Mais t'ai-je déjà raconté l'histoire de ce quartier qui m'a vu en culottes courtes ? La cité Paradis est une voie publique située dans le 10e arrondissement de Paris. Elle est en forme de té, une branche débouche au 43 rue de Paradis, la deuxième au 57 rue d'Hauteville et la troisième en impasse.

-----------------
## Utilisation
Posez votre question en demandant une adresse, dans le formulaire prévu à cet effet, et le bot vous répondra.

(Le programme est configuré pour la France, ceci peut être changé dans 
grandPyApp/api/apiconfig.py 
en retirant la ligne : "COUNTRY": "fr" ou en choissant un autre pays.)

## Logiciels, librairies, APIs
- Python 3.8
- Flask
- Ajax (JQuery)
- HTML 5
- CSS 3
- Bootstrap
- PaaS Heroku (WSGI : Gunicorn)
- APIs :
    * Geocoding (Mapbox) 
    https://docs.mapbox.com/

    * Media wiki (Wikipedia) 
    https://www.mediawiki.org/wiki/MediaWiki
- Pytest

## Lien direct vers l'application hébergée sur Heroku :
https://grand-py.herokuapp.com/

## Ou : installation et lancement
- Installation :
    * clone
    * `pipenv install`
    * `pipenv shell`
    * `pipenv install -r requirements.txt`
    * modifier le fichier settings.py pour y ajouter votre clef privée pour l'api Mapbox.

- Lancement :
    * py run.py

Le site sera accessible par défaut à l'adresse : 
http://127.0.0.1:5000/

## Deployer sur heroku
Il est nécessaire d'avoir un compte heroku et d'y définir ce projet comme nouveau projet heroku.
Puis passer la commande :
- `git push heroku`
Il faudra également ajouter la variable d'environnement "MAPBOX_API_KEY" avec comme valeur votre clef pour l'api Mapbox.

-----------------
## Lien vers le Trello :
https://trello.com/b/HvdsLlAh/p7-grandpy-bot



