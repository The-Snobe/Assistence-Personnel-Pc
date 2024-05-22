""" Ce module est utilisé pour jouer un fichier musical aléatoire à partir du répertoire sélectionné
    lorsque l'utilisateur demande de jouer une chanson aléatoire """

import os
import random as ran
import webbrowser as wb


def play_random_music():
    song_list = os.listdir('D:\\Music\\Enya')
    i = ran.choice(song_list)
    wb.open('D:\\Music\\Enya\\'+i)
    return
