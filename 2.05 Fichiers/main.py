import os

#gestion du répertoire
os.chdir("/Users/tatopoulos/Documents/")

# Afficher le répertoire en cours
print(os.getcwd())

# Ouvrir un fichier en lecture
fichierread = open("Fichier2.txt","r")
print(fichierread.read())

# Cloture du dataset
fichierread.close()

# Acces en ecriture mode a pour append et w pour ecrasement
fichierwrite = open("Fichier2.txt","w")
fichierwrite.write("Ceci esr mon contenu")
fichierwrite.close()

# Traitement du fichier au sein d'un bloc (cloture auto)
with open("Fichier2.txt","r") as mavariable:
    print(mavariable.read())