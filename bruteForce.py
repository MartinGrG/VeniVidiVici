# Ce code va réaliser un décryptage par la méthode brute force.

from DecrypterCrypter import decrypter
from verifications import verifier_binaire

def brute_force(text, clef_to_delete):
    resultat = 0
    clef_supposee = 1
    compteur = 0
    liste_clef_probable = []

    if not "liste_clef_to_delete" in locals():
        liste_clef_to_delete = []
    liste_clef_to_delete.append(clef_to_delete)

    while resultat < 0.15 and compteur < 26:
        compteur += 1  # compte le nombre de tours de boucle
        clef_supposee = -clef_supposee

        if not(clef_supposee in liste_clef_to_delete):
            message = decrypter(text, clef_supposee)

            resultat = analyse_text(message[0])
            liste_clef_probable.append([resultat, message])
            if compteur % 2 == 0:
                clef_supposee += 1

    # Cas où l'algo a convergé, on vérifie si c'est bon avec l'utilisateur
    if resultat > 0.15:
        print("|     l'algorithme par force brute     |")
        print(f"|        a convergé en donnant          |")
        print("|           le résultat suivant        |\n")
        print(f"{message[0]}\n")
        print("|             Est-correct ?             |")
        print("|             (oui) ou (non)            |")
        reponse1 = verifier_binaire("oui","non")
        if reponse1 == "oui":
            return message
        else:
            clef_to_delete = message[1]
            brute_force(text, clef_to_delete)
    else: # l'algo a testé toutes les clefs sans succès (pas de convergence)
        print("|     l'algorithme par force brute     |")
        print(f"|          n'a pas convergé           |")
        print("|   nous sommes contraints de passer   |")
        print("|         par manière itérative        |")
        print("|                                      |")
        print("|    L'algorithme va vous proposer     |")
        print("|    itérativement des décryptages     |")
        print("|  du plus probable au moins probable  |")
        print("|  répondez par oui ou non si le texte |")
        print("|            semble décrypté           |")

        liste_clef_probable.sort(key=lambda prob: prob[0], reverse=True)
        reponse2 = "non"
        compteur_iteratif = 0
        while reponse2 == "non" and compteur_iteratif<len(liste_clef_probable):
            print(liste_clef_probable[compteur_iteratif][1][0])
            print("|           semble décrypté ?           |")
            print("|              oui ou non               |")
            reponse2 = verifier_binaire("oui", "non")
            compteur_iteratif+=1
        if reponse2 == "oui":
            return liste_clef_probable[compteur_iteratif-1][1]
        else:
            return "Le message n'est pas en Français ou bien pas codé en César"





def analyse_text(text):
    dictionnaire = ['le', 'la', 'les', 'de', 'un', 'une', 'et', 'a', 'il', 'ils', 'elles',
                    'elle', 'avoir', 'etre', 'je', 'tu', 'nous', 'vous', 'que', 'qui',
                    'son', 'se', 'ce', 'dans', 'en', 'du', 'sur']
    texte_liste = text.split(' ')
    nombre_mots = len(texte_liste)

    # Des qu'un mot est trouvé représente plus de 20% des mots du texte on prend
    occurence_mots = []
    for x in dictionnaire:
        occurence_mots.append((texte_liste.count(x)))
    return sum(occurence_mots) / nombre_mots

