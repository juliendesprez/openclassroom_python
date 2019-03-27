import os
from zcasino.jouer.jouer import runGame

variable = 2.8

if variable >= 3:
    print("1")
elif variable < -1:
    print("2")
else:
    print("3")

while 1:
    try:
        sommeInitiale = input("Saisir une somme de base : ")
        sommeInitiale = int(sommeInitiale)
        assert sommeInitiale > 10 # comme en ABAP un assert remonte une exception
        break
    except ValueError:
        print("Vous n'avez pas saisi une somme.")
    except AssertionError:
        print("Le montant saisie > 10 dols")

print("que la partie commence")
runGame(sommeInitiale)   

# On met en pause le système (Windows)
os.system("pause")