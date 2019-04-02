import os

# Exemple 1 utilisation d'une variable externe mais non globale
# la variable n'est alors modifiable que pendant la durée de l'execution de la fonction
# elle reprend sa valeur d'origine à la sortie
i = 4 # Une variable, nommée i, contenant un entier
def inc_i():
    """Fonction chargée d'incrémenter i de 1"""
    i = 1
 

inc_i()
print(i)

# Exemple 2 utilisation d'une variable globale
j = 4 # Une variable, nommée i, contenant un entier
def inc_j():
    """Fonction chargée d'incrémenter i de 1"""
    global j # Python recherche i en dehors de l'espace local de la fonction
    j += 1
 
inc_j()
print(j)