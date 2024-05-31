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
    print(f"|{espace_gauche * ' '}{phrase}{espace_droite * ' '}|")


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

