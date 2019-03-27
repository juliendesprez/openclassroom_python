"""module contenante la gestion de la partie"""
import os
from random import randrange
from math import ceil
import zcasino.mise.miser as casino

def runGame(argentJoueur):
    print("Vous avez joué ", argentJoueur, " dollars.")
    while argentJoueur > 0:
        sommeMisee = casino.miser(argentJoueur)
        print("vous avez misé : ", sommeMisee)

        numeroParie = casino.parierNumero()
        print("vous avez parié sur le : ", numeroParie)

        argentJoueur += faiteVosJeux(sommeMisee, numeroParie )

        if argentJoueur <= 0:
            print("Une autre fois peut être")
            break
        print("Il vous reste en banque : ", argentJoueur)
def faiteVosJeux(sommeMisee, numeroParie):
    print("Faites vos jeux rien ne va plus!")

    numeroFinal  = randrange(50)
    print("Le numéro tombé est le ", numeroFinal)

    if numeroFinal == numeroParie:
        print("Félicitation vous avez gagné 3 fois la mise")
        return sommeMisee * 3
    elif numeroFinal%2 == numeroParie%2:
        print("Pas de bol mais tout n\'est pas perdu")
        return ceil( sommeMisee * -0.5 )
    else:
        print("Désolé c'est perdu")
        return sommeMisee * -1
