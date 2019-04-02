import pickle
import os

#gestion du répertoire
os.chdir("/Users/tatopoulos/Documents/")

# Afficher le répertoire en cours
print(os.getcwd())

meinscore = {"FC Visiteur":1, "AS":2}
print("Score")
print(meinscore)
# ouverture via open e  mode wb (écriture binaire)
with open("datafile", "wb") as mydatafile:
    # appel de la classe Pickler
    myPickler = pickle.Pickler(mydatafile)
    myPickler.dump(meinscore)

meinscore = {}
print("Score")
print(meinscore)

# lecture binaire
with open('datafile', 'rb') as fichier:
    mon_depickler = pickle.Unpickler(fichier)
    meinscore = mon_depickler.load()
print("Score")
print(meinscore)