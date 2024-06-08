"""Ce code va réaliser un décryptage par la méthode brute force."""

from DecrypterCrypter import decrypter
from verifications import verifier_binaire
from verifications import afficher

# création d'une liste globale pour le cas de mauvais résultats : pour stocker les clefs à ne plus tester.
# Nécéssité de définir cette variable en globale car on souhaite garder en mémoire les données malgré
# l'appel récursif de la fonction.
liste_clef_to_delete = []

def brute_force(text, clef_to_delete):
    resultat = 0
    clef_supposee = 1
    compteur = 0
    liste_clef_probable = []

    # On ajoute les clefs à ne plus tester dans le cas de mauvais premiers résultats
    global liste_clef_to_delete
    liste_clef_to_delete.append(clef_to_delete)

    # Boucle principale testant sur le message toutes les clefs (sauf celles enlevées).
    while resultat < 0.15 and compteur < 26:
        compteur += 1  # compte le nombre de tours de boucle
        clef_supposee = -clef_supposee # On alterne entre une clef positive et une clef négative

        if not(clef_supposee in liste_clef_to_delete):
            message = decrypter(text, clef_supposee)
            resultat = analyse_text(message[0]) # Analyse pour obtenir la probabilité de décodage effectif
            liste_clef_probable.append([resultat, message]) # On stocke les clefs et leur probabilité
            if compteur % 2 == 0:
                clef_supposee += 1 # Dès qu'une clef et son opposée sont testées, on incrémente

    # Si on dépasse un taux de probabilité de 15% alors le message est dit décrypté
    # Cas où l'algo a convergé, on vérifie si c'est bon avec l'utilisateur
    if resultat > 0.15:
        afficher("l'algorithme par force brute")
        afficher("a convergé en donnant")
        afficher("le résultat suivant")
        print(f"{message[0]}")
        afficher("Est-ce correct ?")
        afficher("(oui) ou (non)")
        reponse1 = verifier_binaire("oui","non")
        if reponse1 == "oui":
            print(message)
            return message
        else: # Si l'aglorithme s'est trompé, alors il se relance avec la mauvaise clef proposée en moins
            clef_to_delete = message[1]
            return brute_force(text, clef_to_delete)

    # Si on dépasse toutes les clefs une fois, pas de convergence, on passe en mode itératif
    else: # l'algo a testé toutes les clefs sans succès (pas de convergence)
        afficher("l'algorithme par force brute")
        afficher(f"n'a pas convergé")
        afficher("nous sommes contraints de passer")
        afficher("par manière itérative")
        afficher(" ")
        afficher("L'algorithme va vous proposer")
        afficher("itérativement des décryptages")
        afficher("du plus probable au moins probable")
        afficher("répondez par oui ou non si le texte")
        afficher("semble décrypté")

        # On va présenter les messages décryptés par chaque clef un par un dans
        # l'ordre des probabilités décroissantes
        liste_clef_probable.sort(key=lambda prob: prob[0], reverse=True)
        reponse2 = "non"
        compteur_iteratif = 0

        while reponse2 == "non" and compteur_iteratif<len(liste_clef_probable):
            afficher(liste_clef_probable[compteur_iteratif][1][0])
            afficher("semble décrypté ?")
            afficher("oui ou non")
            reponse2 = verifier_binaire("oui", "non")
            compteur_iteratif+=1

        if reponse2 == "oui": # Si on trouve un message correctement décrypté
            print(type(liste_clef_probable[compteur_iteratif-1][1][1]))
            return liste_clef_probable[compteur_iteratif-1][1]
        else: # Si pour finir, après toutes les tentatives, il n'y a toujours pas de solution
            return "None"


# Cette fonction permet d'analyser un texte et de retourner la
# probaibilité qu'il soit écrit en français correct
def analyse_text(text):
    # On crée un dictionnaire avec certains mots les plus utilisés dans la langue française :
    dictionnaire = ['le', 'la', 'les', 'de', 'un', 'une', 'et', 'a', 'il', 'ils', 'elles',
                    'elle', 'avoir', 'etre', 'je', 'tu', 'nous', 'vous', 'que', 'qui',
                    'son', 'se', 'ce', 'dans', 'en', 'du', 'sur']
    texte_liste = text.split(' ')
    nombre_mots = len(texte_liste)

    # On compte le nombre de mots du dictionnaire utilisés dans le message
    # et on divise par le nomre de mots total du texte. Cela forme la probabilité
    # Après plusieurs tests, au-dessus de 15%, le mot est normalement décrypté.
    occurence_mots = []
    for x in dictionnaire:
        occurence_mots.append((texte_liste.count(x)))
    return sum(occurence_mots) / nombre_mots

