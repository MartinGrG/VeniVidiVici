""" Ce code met en place l'interface utilisateur"""
from DecrypterCrypter import *
from gestionFichier import *
from verifications import *
from bruteForce import brute_force


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

