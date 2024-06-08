""" Ce code met en place l'interface utilisateur et permet de faire le lien entre lui et le script"""

from DecrypterCrypter import *
from gestionFichier import *
from verifications import *
from bruteForce import brute_force


def interface():
    print("┌---------------------------------------┐")
    afficher("Bonjour")
    afficher("Bienvenue sur l'encrypteur/décrypteur")
    afficher("de code César")
    afficher("Faites vite, le temps presse")
    print("└---------------------------------------┘")

    # Demande si l'utilisateur a une clef :
    afficher("Avez vous une clef de cryptage")
    afficher("sur vous ?")

    afficher("oui(entrer oui)   non(entrer non)")
    # On s'assure que la réponse est dans les possibilités
    dispo_clef = verifier_binaire('oui', 'non')

    if dispo_clef == 'oui':  # On a la clef de cryptage : mode normal
      
        afficher("Vous avez une clef d'encryptage")
        afficher("vous entrez en mode normal")
        afficher("")

        # On demande à l'utilisateur d'entrer une clef + vérification de sa validité
        clef = verifier_clef()

        # On demande à l'utilisateur le format d'entrée du message à traiter
        afficher("Sous quelle forme souhaitez vous")
        afficher("entrer votre texte")
        afficher("fichier(fichier)   input(input)")
        # On s'assure que la réponse est dans les possibilités
        forme = verifier_binaire('fichier', 'input')

        if forme == "fichier":  # extraire le texte via un fichier

            afficher("entrer le nom du fichier")
            afficher("sous la forme")
            afficher("[mon_fichier.txt]")
            fichier_nom = input("--> ")
            # On vérifie que le fichier existe + lecture si c'est le cas
            texte = lecture(fichier_nom)

        else:  # extraire le texte via un input

            afficher("entrer le texte ci-dessous")
            afficher("en une seule ligne")
            texte = input("--> ")

        # On demande à l'utilisateur s'il souhaite encrypter ou decrypter
        afficher("Souhaitez vous encrypter ou décrypter")
        afficher("")
        afficher("encrypter(encry)   decrypter(decry)")
        # On s'assure que la réponse est dans les possibilités
        choix = verifier_binaire('encry', 'decry')

        # On va encrypter avec la clef !
        if choix == "encry":
            ecriture(crypter(texte, clef)[0])
            afficher("Le résultat est : ")
            print(f"{crypter(texte, clef)[0]}")
            afficher("Le résultat se trouve dans message.txt")

        # On va decrypter avec la clef !
        else:
            ecriture(decrypter(texte, clef)[0])
            afficher("Le résultat est : ")
            print(f"{decrypter(texte, clef)[0]}")
            afficher("Le résultat se trouve dans message.txt")

    else:  # 'non' : pas de clef, on entre en mode brut-force
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
        # On lance le décryptage par force brute et on récupère le résultat
        resultat = brute_force(texte,0)

        # Si malgré tous les efforts, la méthode par force brute n'a rien donné :
        if resultat == "None":
            afficher("Le message n'est pas en Français")
            afficher("ou bien n'est pas codé en César")

        # Si la méthode a convergé vers un bon résultat !
        else:
            afficher(f"Pour la clef : {resultat[1]}")
            afficher("La méthode par force brute a convergé")
            afficher(f"le message résultant est le suivant :")
            print('')
            print(resultat[0])
            print('')

            # Dans le cas de la méthode force brute, on demande à l'utilisateur s'il souhaite
            # enregistrer le résultat sur un fichier texte, ici, message.txt
            afficher("Voulez-vous enregistrer la réponse")
            afficher("sous la forme d'un fichier ?")
            afficher("(oui) ou (non)")
            choix_enregistrer = verifier_binaire('oui', 'non')
            if choix_enregistrer == 'oui':
                ecriture(resultat[0])
                afficher("Le résultat se trouve dans message.txt")
            else:
                afficher("À bientôt")
