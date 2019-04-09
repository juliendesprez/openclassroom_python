import os
import data.donnees as donnees
import functions.fonctions as fonc

print("Début du jeu")

# Initialisation des variables du jeu
nouveauMot = fonc.chooseNewWord()
nbEssais = 0
score = 0
saisieCorrecte = str()

pseudo = fonc.saisiePseudo()
score = fonc.initPlayerData(pseudo)
print("Bienvenue {0}, votre score actuel est de : {1}".format(pseudo, score))

print("Le mot choisi est : " + nouveauMot)
while nbEssais < donnees.nbChances:
    # Saisir lettre
    essaisRestants = donnees.nbChances - nbEssais
    lettre = fonc.saisieLettre(essaisRestants)

    # Contrôle lettre
    try:
        fonc.validateChoice(lettre, nouveauMot)
        saisieCorrecte += lettre
    except AssertionError:
        print("Mauvaise pioche :)")
        nbEssais += 1

    # Afficher mot
    victory = True
    for lettre in nouveauMot:
        if lettre in saisieCorrecte: 
            print(lettre)
        else: 
            print("*")
            victory = False

    # Fin du game ?
    if victory is True:
        print("Félicitations vous avez gagné")
        # ajout du score
        score += essaisRestants
        print("votre score final est : {0}".format(score))
        break

# Sauvegarde des scores
fonc.savePlayerData(pseudo, score)

os.system("pause")
