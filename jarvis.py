import speech_recognition as sr
import win32com.client
import ctypes
import winshell
from nltk.tokenize import word_tokenize as wtk
from nltk.tokenize import sent_tokenize as srtk
import random as ran
import os
import cv2
import pyautogui
import pywhatkit
import wikipedia

# J.A.R.V.I.S Modules
import extra_system_feature as esf
import open_app_feature as oaf
import random_music_play_feature as rmpf
import wolframalpha_feature as wf
import wikipedia_feature as wkf
import news_api as nap
import browser_feature as bf
import youtube_feature as yf
import book_api as bap

# Changing current working directory
os.chdir('D:\\Python\\Intelligent-Personnel-Assistance\\J.A.R.V.I.S')

# Global list
opening_phrases = ['Bienvenue M. Super abel', 'Comment puis-je vous aider M. Super abel', 'Bienvenue Monsieur, comment puis-je vous aider', 'à votre service monsieur']
exit_when_done = ['c\'est tout jarvis', 'quitte', 'quitte maintenant jarvis', 'ferme jarvis', 'merci jarvis']

# Function to determine the task performing word
def task_performing_word(input_sent):
    input_list = wtk(input_sent)
    task_word = ''
    for i in input_list:
        if i == 'livre':
            task_word = 'livre'
            break
        elif i == 'recycler':
            task_word = 'vider'
            break
        elif i == 'verrouiller':
            task_word = 'verrouiller'
            break
        elif i == 'actualités':
            task_word = 'actualités'
            break
        elif i == 'ouvrir':
            task_word = 'ouvrir'
            break
        elif (i == 'chercher' or i == 'regarder') and ('wikipedia' in input_list):
            task_word = 'wikipedia'
            break
        elif i == 'chanson' or i == 'ennuyé':
            task_word = 'chanson'
            break
        elif i == 'jouer' and input_list[1] == 'youtube':
            task_word = 'youtube'
            break
        elif i == 'chercher' or i == 'regarder':
            task_word = 'navigateur'
            break
    if task_word == '':
        task_word = 'loup'
    return task_word

def take_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot.png")
    speaker.Speak('Capture d\'écran prise')
def click_photo():
    cap = cv2.VideoCapture(0)
    ret, frame = cap.read()
    if ret:
        cv2.imwrite("photo.png", frame)
        speaker.Speak('Photo prise')
    cap.release()
    cv2.destroyAllWindows()
# Function to wake up JARVIS
def wake_jarvis_up(re_text):
    re_text = re_text.lower()
    text_list = wtk(re_text)
    for i in text_list:
        if i == 'jarvis' or i == 'ami':
            return 'jarvis'
    return

active_check = False
active_text = 'jarvis'

speaker = win32com.client.Dispatch('SAPI.SpVoice')
def jarvis_command():
    with sr.Microphone() as source:
        print("listening...")
        listener.pause_threshold = 5
        voice = listener.listen(source)
        command = listener.recognize_google(voice, language="fr-FR")
        command = command.lower()
        print(command)
        if 'alexa' in command:
            command = command.replace('alexa', '')
            print(command)
    return command

rs = sr.Recognizer()
with sr.Microphone() as source:
    print("######### CALIBRATION #############")
    rs.adjust_for_ambient_noise(source, duration=2)
    # Conversation loop
    while True:
        print("######### CALIBRATION #############")
        rs.adjust_for_ambient_noise(source, duration=2)
        if active_check == False:
            print('Dites JARVIS pour activer')
        else:
            print('J.A.R.V.I.S Ecoute....')
        audi = rs.listen(source)
        print('Enregistrement terminé')

        try:
            print('Traitement des données')
            command = jarvis_command()
            text_recieved = rs.recognize_google(audi, language="fr-FR")  # Specify French language
            text_recieved = text_recieved.lower()
            print(text_recieved)
            if active_check == False:
                text_recieved = wake_jarvis_up(text_recieved)
            print('Données reçues')
            if text_recieved == 'jarvis':
                active_check = True
                speaker.Speak(ran.choice(opening_phrases))
            elif text_recieved.lower() in exit_when_done:
                speaker.Speak('Sortie maintenant')
                break
            else:
                finl_task = task_performing_word(text_recieved)
                print(text_recieved)
                if finl_task == 'vider':
                    speaker.Speak('Bien sûr, monsieur')
                    esf.empty_recycle_bin()
                    speaker.Speak('La corbeille doit être vide maintenant')

                elif finl_task == 'verrouiller':
                    speaker.Speak('Verrouillage de l\'écran de l\'ordinateur portable, monsieur')
                    esf.lock_desktop_screen()

                elif finl_task == 'ouvrir':
                    task_value = oaf.give_me_app_name(text_recieved)
                    if task_value == 1:
                        app_n = text_recieved[5:len(text_recieved)]
                        speaker.Speak('Ouverture de ' + app_n)
                    else:
                        print('Impossible d\'effectuer la tâche')

                elif finl_task == 'chanson':
                    rmpf.play_random_music()
                    speaker.Speak('J\'espère que vous aimerez la chanson')

                elif 'capture' in command:
                    take_screenshot()

                elif finl_task == 'loup':
                    answer = wf.wolframalpha_questions(text_recieved)
                    if answer == 0 or answer == 'aucun':
                        speaker.Speak('Je ne sais pas, monsieur')
                    else:
                        speaker.Speak(answer)

                elif 'Lire chanson de' in command or 'nasheed' in command or 'chanson' in command:
                    # Code for playing music
                    speaker.Speak("Je lance la chanson.")
                    pywhatkit.playonyt(command)
                
                elif 'photo' in command:
                    click_photo()

                elif finl_task == 'wikipedia':
                    topic = wkf.give_me_topic_name(text_recieved)
                    short_summary = wkf.get_short_summary(topic)
                    print(short_summary)
                    speaker.Speak('Affichage des résultats sur votre écran, monsieur')

                elif finl_task == 'navigateur':
                    bf.browser_search(text_recieved)
                    speaker.Speak('Affichage des résultats de recherche sur le navigateur, monsieur')

                elif 'qui est' in command:
                    person = command.replace("qui est", "")
                    wikipedia.set_lang("fr")
                    info = wikipedia.summary(person, 1)
                    print(info)
                    speaker.Speak(info)

                elif finl_task == 'youtube':
                    yf.open_video_youtube(text_recieved)
                    speaker.Speak('Pourquoi pas, monsieur')

                elif finl_task == 'actualités':
                    news_cat, news_name = nap.give_me_news_name(text_recieved)
                    if news_cat == 'catégorie':
                        nap.get_by_category(news_name)
                    elif news_cat == 'source':
                        nap.get_by_source(news_name)
                    elif news_cat == 'recherche':
                        nap.get_by_query(news_name)
                    else:
                        speaker.Speak('Désolé, monsieur, je n\'ai pas trouvé de nouvelles pertinentes')

        except:
            print('Parlez encore une fois, monsieur')

