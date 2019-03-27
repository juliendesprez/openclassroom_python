"""module multipli contenant la fonction table_multiplication"""
import os

def table_multiplication(nombre,maxOccurence=10):
    """Fonction affichant la table de multiplication par nb
    de 1*nb à max*nb
    
    (max >= 0)"""    
    i = 0 # Notre compteur ! L'auriez-vous oublié ?
    while i < maxOccurence: # Tant que i est strictement inférieure à 10,
        print(i + 1, "*", nombre, "=", (i + 1) * nombre)
        i += 1 # On incrémente i de 1 à chaque tour de boucle.

# test de la fonction table uniquement via le module
if __name__ == "__main__":
    table_multiplication(4)
    os.system("pause")        