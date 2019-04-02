import os


def afficher_flottant(flottant):
    """Fonction prenant en paramètre un flottant et renvoyant une chaîne de caractères représentant la troncature de ce nombre. La partie flottante doit avoir une longueur maximum de 3 caractères.

    De plus, on va remplacer le point décimal par la virgule"""
    
    if type(flottant) is not float:
        raise TypeError("Le paramètre attendu doit être un flottant")
    flottant = str(flottant)
    partie_entiere, partie_flottante = flottant.split(".")
    # La partie entière n'est pas à modifier
    # Seule la partie flottante doit être tronquée
    return ",".join([partie_entiere, partie_flottante[:3]])


machaine = list()
machaine = afficher_flottant(3.99999999999998)
print(machaine)

# transformer une liste en une nouvelle en changeant les éléments
liste_origine = [0, 1, 2, 3, 4, 5]
liste_origine2 = [nb * nb for nb in liste_origine]
print(liste_origine2)

# Filtrer le contenu d'une liste dans une nouvelle
liste_origine = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
liste_origine2 = [nb for nb in liste_origine if nb % 2 == 0]
print(liste_origine2)


inventaire = [
    ("pommes", 22),
    ("melons", 4),
    ("poires", 18),
    ("fraises", 76),
    ("prunes", 51),
]

print(inventaire)
# On change le sens de l'inventaire, la quantité avant le nom
liste_inversee = [( nb, fruit ) for fruit,nb in inventaire ]
inventaire = [( fruit,nb ) for nb, fruit in sorted(liste_inversee, reverse = True ) ] 
print(inventaire)
