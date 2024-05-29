# Ce code met en place l'interface utilisateur
from DecrypterCrypter import *
from gestionFichier import *


def verifier_int(chaine):
    """Cette fonction sert à vérifier qu'une chaîne de caractère contient un entier"""
    # Entrée : chaîne de caractère
    # Sorite : booléen
    liste_int = ['-', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    for idx, elem in enumerate(chaine):
        if elem not in liste_int:
            return False
        elif elem == '-' and idx != 0:
            return False
    return True


def verifier_binaire(choix1, choix2):
    """Cette fonction sert à s'assurer que l'utilisateur a entré une réponse parmi 2 choix"""
    # Entrée : des chaînes de caractères
    # Sortie : une chaîne de caractère
    choix = input("--> ")
    taille_fenetre = 39
    espace_gauche1 = (taille_fenetre - len(choix1)) // 2
    espace_droite1 = taille_fenetre - len(choix1) - espace_gauche1
    espace_gauche2 = (taille_fenetre - len(choix2)) // 2
    espace_droite2 = taille_fenetre - len(choix2) - espace_gauche2
    liste_choix = [choix1, choix2]
    while choix not in liste_choix:
        print("| La réponse entrée n'est pas correcte. |")
        print("|                                       |")
        print("|       Veuillez choisir entre :        |")
        print(f"|{espace_gauche1 * ' '}{choix1}{espace_droite1 * ' '}|")
        print(f"|{espace_gauche2 * ' '}{choix2}{espace_droite2 * ' '}|")
        print("|                                       |")
        choix = input("--> ")
    return choix


def verifier_clef():
    """Cette fonction sert à vérifier que l'utilisateur entre une clef valide s'il en a une"""
    # Sortie : un entier ou une chaîne de caractère 'non' si l'utilisateur n'a pas de clé
    clef = verifier_binaire('oui', 'non')
    if clef == 'oui':
        print("|                                       |")
        print("|        Quelle est votre clef ?        |")
        valeur_clef = input("--> ")
        print("")
        while not verifier_int(valeur_clef):
            print("|                                       |")
            print("|   La clef entrée n'est pas correcte   |")
            print("|        Quelle est votre clef ?        |")
            valeur_clef = input("--> ")
        return int(valeur_clef)
    else:
        return 'non'


def interface():
    print("┌---------------------------------------┐")
    print("|               Bonjour                 |")
    print("| Bienvenue sur l'encrypteur/décrypteur |")
    print("|                                       |")
    print("|     Faites vite, le temps presse      |")
    print("└---------------------------------------┘")

    print("|    Avez vous une clef de cryptage     |")
    print("|                sur vous ?             |")
    print("|    oui(entrer oui)   non(entrer non)  |")
    clef = verifier_clef()

    if clef == 'non':  # non : pas de clef : mode brut-force
        print("pas traité")

    # On vérifie d'abord 'non' parce que clef is int ne fonctionne
    # pas donc impossible de verifier si on a un entier ou pas
    else:  # On a la clef de cryptage : mode normal
        print("|    Vous avez une clef d'encryptage    |")
        print("|      vous entrez en mode normal       |")

        print("|    sous quel forme souhaitez vous     |")
        print("|          entrer votre texte           |")
        print("|    fichier(fichier)   input(input)    |")
        forme = verifier_binaire('fichier', 'input')

        if forme == "fichier":  # extraire le texte via un fichier

            print("|        entrer le nom du fichier       |")
            print("|              sous la forme            |")
            print("|            [mon_fichier.txt]          |")
            fichier_nom = input("--> ")
            texte = lecture(fichier_nom)

        else:  # extraire le texte via un input

            print("|       entrer le texte ci-dessous      |")
            texte = input("--> ")

        print("|   Souhaitez vous encoder ou decoder   |")
        print("|                                       |")
        print("|  encrypter(encry)   decrypter(decry)  |")
        choix = verifier_binaire('encry', 'decry')

        if choix == "encry":
            ecriture(crypter(texte, clef))
            return crypter(texte, clef)
        else:
            ecriture(crypter(texte, clef))
            return decrypter(texte, clef)
