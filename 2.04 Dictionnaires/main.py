import os

# création d'un dictionnaire avec des clés de type string
mondictionnaire = {}
mondictionnaire["pseudo"] = "Prolixe"
mondictionnaire["mot de passe"] = "*"
print(mondictionnaire)

# Ca fonctionne aussi avec d'autres type pour les clé
mon_dictionnaire = {}
mon_dictionnaire[0] = "a"
mon_dictionnaire[1] = "e"
mon_dictionnaire[2] = "i"
mon_dictionnaire[3] = "o"
mon_dictionnaire[4] = "u"
mon_dictionnaire[5] = "y"
print(mon_dictionnaire)

# Même des tuples
echiquier = {}
echiquier['a', 1] = "tour blanche" # En bas à gauche de l'échiquier
echiquier['b', 1] = "cavalier blanc" # À droite de la tour
echiquier['c', 1] = "fou blanc" # À droite du cavalier
echiquier['d', 1] = "reine blanche" # À droite du fou
# Première ligne des blancs
echiquier['a', 2] = "pion blanc" # Devant la tour
echiquier['b', 2] = "pion blanc" # Devant le cavalier, à droite du pion
# Seconde ligne des blancs

# encore plus loin avec des references à des fonctions
def fete():
     print("C'est la fête.")
 
def oiseau():
    print("Fais comme l'oiseau...")
...
fonctions = {}
fonctions["fete"] = fete # on ne met pas les parenthèses
fonctions["oiseau"] = oiseau
fonctions["oiseau"]() # on essaye de l'appeler



# Autre syntaxe d'alimentation
placard = {"chemise":3, "pantalon":6, "tee-shirt":7}

# suppression
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
del placard["chemise"]

# ou 
placard = {"chemise":3, "pantalon":6, "tee shirt":7}
placard.pop("chemise")