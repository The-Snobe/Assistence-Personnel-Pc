# J.A.R.V.I.S

J.A.R.V.I.S est un programme intelligent qui vous permet d'interagir avec votre PC en lui parlant. Il possède diverses fonctionnalités qui lui permettent d'exécuter différentes tâches que son maître demande. Les fonctionnalités de J.A.R.V.I.S incluent :

1. Vider la Corbeille
2. Verrouiller l'écran d'accueil de votre PC
3. Répondre aux questions mathématiques et autres questions générales
4. Jouer une chanson lorsque vous vous ennuyez
5. Trouver les dernières nouvelles à partir de sources spécifiées, de catégories ou de tout autre sujet
6. Obtenir des articles de Wikipédia
7. Rechercher des livres que vous aimez ou que vous voulez acheter
8. Permettre de rechercher une vidéo sur YouTube via commande vocale
9. Afficher les résultats de questions générales sur le navigateur

D'autres fonctionnalités seront ajoutées bientôt.

## Installation

Pour exécuter J.A.R.V.I.S sur votre PC, suivez les étapes suivantes :

1. Clonez/téléchargez le dépôt sur votre PC.
2. Vous devez avoir Python 3 ou une version ultérieure installée sur votre PC. Si vous ne l'avez pas, téléchargez-le ici : https://www.python.org/. Assurez-vous d'avoir tous les paquets et modules Python requis installés [utilisez `pip3 install -r requirements.txt`].

Les modules requis sont :
- speech_recognition
- ctypes
- nltk
- wikipedia
- requests

3. Modifiez le chemin des fichiers selon votre système dans les fichiers suivants :
   - jarvis.py : modifiez dans `os.chdir()`
   - book_api.py : modifiez dans `os.chdir()`
   - news_api.py : modifiez dans `os.chdir()` et `api_key` (obtenez la clé API ici : https://newsapi.org/)
   - open_app_feature.py : modifiez dans `os.chdir()`
   - random_music_play_feature.py : modifiez dans `os.listdir('Le dossier de musique va ici')`
   - wikipedia_feature.py : modifiez dans la méthode `get_short_summary()` dans `os.chdir()`
   - wolframalpha_feature.py : modifiez l'`app_id` (obtenez l'identifiant de l'application ici : https://www.wolframalpha.com/)

4. Exécutez le fichier `jarvis.py` et attendez qu'il affiche le message "calibrating the noise level" dans le shell interactif de Python. Parlez vos commandes et questions une à la fois lorsqu'il affiche "jarvis is listening...".

