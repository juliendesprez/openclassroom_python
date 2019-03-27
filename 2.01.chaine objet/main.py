import os

chaine = str() # Crée une chaîne vide
# On aurait obtenu le même résultat en tapant chaine = ""

while chaine.lower() != "q":
    print("Tapez 'Q' pour quitter...")
    chaine = input()

print("Merci !")


prenom = "Paul"
nom = "Dupont"
age = 21

# Variabiliser à l'interieur d'une chaine
nouvelle_chaine = "Je m'appelle {0} {1} et j'ai {2} ans.".format(prenom, nom, age)
print(nouvelle_chaine)

prenom = "Paul"
message = "Bonjour"
chaine_complete = message + prenom # On utilise le symbole '+' pour concaténer deux chaînes
print(chaine_complete) # Résultat :

# Pas encore parfait, il manque un espace
# Qu'à cela ne tienne !
chaine_complete = message + " " + prenom
print(chaine_complete) # Résultat :


presentation = "salut"
presentation[0:2] # On sélectionne les deux premières lettres
presentation[2:len(presentation)] # On sélectionne la chaîne sauf les deux premières lettres