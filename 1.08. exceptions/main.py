import os

while 1:
    try:
        annee = input("Saisir une année : ")
        annee = int(annee)
        assert annee > 0 # comme en ABAP un assert remonte une exception

        if annee<=2000:
            raise ValueError("l'année saisie est trop dans le passé")

        break
    except ValueError:
        print("Vous n'avez pas saisi un nombre.")
    except AssertionError:
        print("L'année saisie est inférieure ou égale à 0.")


try:
    resultat = annee / denominateur
except NameError as nameException:
    print("La variable numerateur ou denominateur n'a pas été définie.")
    print(nameException)
except TypeError as typeException:
    print("La variable numerateur ou denominateur possède un type incompatible avec la division.")
    print(typeException)
except ZeroDivisionError as zeroDivideException:
    print("La variable denominateur est égale à 0.")
    print(zeroDivideException)
else:
    print("Le résultat obtenu est", resultat)
    pass
finally:
    print("C\'est la fin")