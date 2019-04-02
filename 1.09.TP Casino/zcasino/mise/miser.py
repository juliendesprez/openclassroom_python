"""module contenante la gestion de la mise"""
import os


def miser(sommePlafond):
    while 1:
        mise = input("Combien voulez vous miser ? ")
        try:
            mise = int(mise)
            # Respect du montant max disponible
            assert mise <= sommePlafond

            # Somme correcte exigee
            if mise <= 0:
                raise ValueError
            return mise
        except AssertionError as montantTropGros:
            print("Vous n'avez plus assez d'argent pour miser cette somme. \n \
                saisissez une somme maximale de ", sommePlafond)
        except ValueError:
            print("Saisissez un montant correct")


def parierNumero():
    while 1:
        numeroChoisi = input("Choisissez un numéro entre 0 et 49 : ")
        try:
            numeroChoisi = int(numeroChoisi)
            assert numeroChoisi >= 0 and numeroChoisi <= 49
            return numeroChoisi
        except AssertionError:
            print("Vous devez saisir un chiffre en 0 et 49")
        except ValueError:
            print("Saisissez un chiffre correct")
