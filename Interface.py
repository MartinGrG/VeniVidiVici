""" Ce code met en place l'interface utilisateur"""
from DecrypterCrypter import *
from gestionFichier import *
from bruteForce import brute_force
def interface():
    print("┌---------------------------------------┐")
    print("|               Bonjour                 |")
    print("| bienvenue sur l'encrypteur/décrypteur |")
    print("|                                       |")
    print("|     Faites vite, le temps presse      |")
    print("└---------------------------------------┘")

    print("|    Avez vous une clef de cryptage     |")
    print("|                sur vous ?             |")
    print("|   oui(entrer la)   non(laisser vide)  |")
    clef = input("-->")

    if clef !=" ": #pas vide: clef : mode normal, on a la clef de cryptage
        clef = int(clef)
        print("|    Vous avez une clef d'encryptage    |")
        print("|      vous entrez en mode normal       |")

        print("|   sous quelle forme souhaitez vous    |")
        print("|          entrer votre texte           |")
        print("|    fichier(fichier)   input(input)    |")
        forme = input("-->")

        if forme =="fichier": # extraire le texte via un fichier

            print("|        entrer le nom du fichier       |")
            print("|              sous la forme            |")
            print("|            [mon_fichier.txt]          |")
            fichier_nom = input("-->")
            texte = lecture(fichier_nom)

        else: # extraire le texte via un input

            print("|       entrer le texte ci-dessous      |")
            texte = input("-->")

        print("|   Souhaitez vous encoder ou decoder   |")
        print("|                                       |")
        print("|  encrypter(encry)  decryptage(decry)  |")
        choix = input("-->")

        if choix == "encry":
            ecriture(crypter(texte, clef)[0])
            return crypter(texte, clef)
        else:
            ecriture(crypter(texte, clef))
            return decrypter(texte, clef)


    else: #vide : pas de clef : mode brut-force
        print("|  Vous n'avez pas de clef d'encryptage |")
        print("|    vous entrez en mode force brute    |")

        print("|   sous quelle forme souhaitez vous    |")
        print("|          entrer votre texte           |")
        print("|    fichier(fichier)   input(input)    |")
        forme = input("-->")

        if forme == "fichier":  # extraire le texte via un fichier

            print("|        entrer le nom du fichier       |")
            print("|              sous la forme            |")
            print("|            [mon_fichier.txt]          |")
            fichier_nom = input("-->")
            texte = lecture(fichier_nom)

        else:  # extraire le texte via un input

            print("|       entrer le texte ci-dessous      |")
            texte = input("-->")

        print("|Démarrage du décryptage par force brute|")
        print("|                                       |")
        resultat = brute_force(texte)

        print(f"|       entrer le texte ci-dessous      |")
        print(f"|       pour la clef : {resultat[1]}     |")
        print(f"|la méthode par force brute a décrypté |")
        print(f"| le message résultant est le suivant :|")
        print(resultat[0])
