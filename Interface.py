""" Ce code met en place l'interface utilisateur"""
from DecrypterCrypter import *
from gestionFichier import *
from bruteForce import brute_force


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


def afficher(phrase):
    taille_fenetre = 39
    espace_gauche = (taille_fenetre - len(phrase)) // 2
    espace_droite = taille_fenetre - len(phrase) - espace_gauche
    print(f"|{espace_gauche * ' '}{phrase}{espace_droite* ' '}|")


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
        afficher("La réponse entrée n'est pas correcte.")
        afficher("")
        afficher("Veuillez choisir entre :")
        afficher(choix1)
        afficher(choix2)
        afficher('')

        choix = input("--> ")
    return choix


def verifier_clef():
    """Cette fonction sert à vérifier que l'utilisateur entre une clef valide s'il en a une"""
    # Sortie : un entier : la valeur de la clef
    
    afficher("")
    afficher("Quelle est votre clef ?")
    valeur_clef = input("--> ")
    afficher("")
    while not verifier_int(valeur_clef):
        afficher("")
        afficher("La clef entrée n'est pas correcte")
        afficher("Quelle est votre clef ?")
        valeur_clef = input("--> ")
    return int(valeur_clef)


def interface():
    print("┌---------------------------------------┐")
    afficher("Bonjour")
    afficher("Bienvenue sur l'encrypteur/décrypteur")
    afficher("")
    afficher("Faites vite, le temps presse")
    print("└---------------------------------------┘")

    afficher("Avez vous une clef de cryptage")
    afficher("sur vous ?")

    afficher("oui(entrer oui)   non(entrer non)")
    dispo_clef = verifier_binaire('oui','non')

    # On vérifie d'abord 'non' parce que clef is int ne fonctionne
    # pas donc impossible de verifier si on a un entier ou pas
    if dispo_clef == 'oui':  # On a la clef de cryptage : mode normal
      
        afficher("Vous avez une clef d'encryptage")
        afficher("vous entrez en mode normal")
        afficher("")
        
        clef = verifier_clef()
        
        afficher("Sous quelle forme souhaitez vous")
        afficher("entrer votre texte")
        afficher("fichier(fichier)   input(input)")
        forme = verifier_binaire('fichier', 'input')

        if forme == "fichier":  # extraire le texte via un fichier

            afficher("entrer le nom du fichier")
            afficher("sous la forme")
            afficher("[mon_fichier.txt]")
            fichier_nom = input("--> ")
            texte = lecture(fichier_nom)

        else:  # extraire le texte via un input

            afficher("entrer le texte ci-dessous")
            texte = input("--> ")

        afficher("Souhaitez vous encrypter ou décrypter")
        afficher("")
        afficher("encrypter(encry)   decrypter(decry)")
        choix = verifier_binaire('encry', 'decry')

        if choix == "encry":
            ecriture(crypter(texte, clef)[0])
            return crypter(texte, clef)
        else:
            ecriture(crypter(texte, clef))
            return decrypter(texte, clef)

    else:  # 'non' : pas de clef : mode brut-force
        afficher("Vous n'avez pas de clef d'encryptage")
        afficher("vous entrez en mode force brute")

        afficher("Sous quelle forme souhaitez vous")
        afficher("entrer votre texte")
        afficher("fichier(fichier)   input(input)")
        forme = verifier_binaire('fichier', 'input')

        if forme == "fichier":  # extraire le texte via un fichier

            afficher("entrer le nom du fichier")
            afficher("sous la forme")
            afficher("[mon_fichier.txt]")
            fichier_nom = input("-->")
            texte = lecture(fichier_nom)

        else:  # extraire le texte via un input

            afficher("entrer le texte ci-dessous")
            texte = input("-->")

        afficher("Démarrage du décryptage par force brute")
        afficher("")
        resultat = brute_force(texte)

        afficher(f"Pour la clef : {resultat[1]}")
        afficher("La méthode par force brute a décrypté")
        afficher(f"Le message résultant est le suivant :")
        print('')
        print(resultat[0])

