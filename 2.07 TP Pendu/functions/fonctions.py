import pickle
import os
import data.donnees as donnees
from random import randrange


def chooseNewWord():
    indexMot = randrange(len(donnees.listeMots))

    return donnees.listeMots[indexMot]


def saisieLettre(nbEssais):
    while 1:
        inviteSaisie = "Saisissez une lettre (essais restants {0}) : ".format(nbEssais)
        lettreSaisie = input(inviteSaisie)
        try:
            assert len(lettreSaisie) == 1
            if lettreSaisie in "0123456789":
                raise ValueError
            return lettreSaisie
        except AssertionError:
            print("Saisissez un seul caractère")
        except ValueError:
            print("Saisissez un caractère")


def validateChoice(lettre, mot):
    assert lettre in mot


def initNewFile(pseudo):
    os.chdir(donnees.dataPath)

    playersScore = {}
    playersScore[pseudo] = 0

    try:
        with open("scorefile", "wb") as mydatafile:
            # appel de la classe Pickler
            myPickler = pickle.Pickler(mydatafile)
            myPickler.dump(playersScore)
    except OSError:
        print("erreur initialisation du fichier")

    return playersScore


def saisiePseudo():
    # saisie du pseudo et récupération du score
    pseudo = input("Veuillez saisir votre pseudo de joueur : ")

    return pseudo


def initPlayerData(pseudo):
    os.chdir(donnees.dataPath)
    playersScore = {}

    # lecture du score en cours dans le fichier
    try:
        with open('scorefile', 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            playersScore = mon_depickler.load()
    except OSError:
        playersScore = initNewFile(pseudo)

    score = playersScore[pseudo]

    return score


def savePlayerData(pseudo, score):
    os.chdir(donnees.dataPath)
    playersScore = {}

    # lecture du score en cours dans le fichier
    try:
        with open('scorefile', 'rb') as fichier:
            mon_depickler = pickle.Unpickler(fichier)
            playersScore = mon_depickler.load()

            playersScore[pseudo] = score
    except OSError as erreurEcriture:
        print("Erreur lors de la sauvegarde du fichier", erreurEcriture.strerror)
        return

    try:
        with open('scorefile', 'wb') as fichier:
            myPickler = pickle.Pickler(fichier)
            myPickler.dump(playersScore)
            print("Fichier sauvegardé avec succès dans {0}".format(donnees.dataPath))
    except OSError as erreurEcriture:
        print("Erreur lors de la sauvegarde du fichier", erreurEcriture.strerror)