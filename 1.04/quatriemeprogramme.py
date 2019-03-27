
# -*-coding:utf-8 -*
# import d'un module python contenant des fonctions
# import complet du module math
# import math
# le as <chaine> permet d'aliaser le namespace
# import math as math
# import d'un partie du module
from math import sqrt

import os # On importe le module os qui dispose de variables 
          # et de fonctions utiles pour dialoguer avec votre 
          # système d'exploitation

#Definition d'une fonction pour les tables de multiplication avec affichage (routine)
def table_multiplication(nombre,maxOccurence=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""    
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < maxOccurence: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nombre, "=", (i + 1) * nombre)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

# Définition d'une fonction avec résultat via l'utilisation de return
def carre(valeur):
    return valeur * valeur

# Définition d'une lambda (fonction courte stockée dans une variable)
fonctionCarre = lambda x: x * x

table_multiplication(nombre=11)

variable = carre(5)
print(variable)

variable2 = fonctionCarre(6)
print(variable2)

print(sqrt(16)) # dans un import complet ajouter le namespace ou l'alias devant l'appel de la fonction