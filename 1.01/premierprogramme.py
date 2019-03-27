# Test de la fonction input
anneeSaisie = input("Saisissez une année : ")

anneeSaisie = int(anneeSaisie)

if anneeSaisie%4 == 0 or anneeSaisie%100 == 0 and anneeSaisie%400 == 0:
    print("L\'année est bisextile")
else:
    print("L\'année n\'est pas bisextile")
