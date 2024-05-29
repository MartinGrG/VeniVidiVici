# Ce code va réaliser un décryptage par la méthode brute force.

from DecrypterCrypter import decrypter
def brute_force(text):
    resultat = 0
    clef_supposee = 1
    compteur = 0

    while (resultat<0.15 and compteur<26):
        compteur += 1  # compte le nombre de tour de boucle
        clef_supposee = -clef_supposee

        message = decrypter(text, clef_supposee)

        resultat = analyse_text(message[0])


        if (compteur % 2 == 0):
            clef_supposee += 1

    if(clef_supposee>0):
        clef_supposee-=1


    return clef_supposee

def analyse_text(text):
    dictionnaire = ['le','la','les','de','un','une','et','a','il','ils','elles',
                    'elle','avoir','etre','je','tu','nous','vous','que','qui',
                    'son','se','ce','dans','en','du','sur']
    texte_liste = text.split(' ')
    nombre_mots = len(texte_liste)

#Des qu'un mot est trouvé représente plus de 20% des mots du texte on prend
    occurence_mots=[]
    for x in dictionnaire:
        occurence_mots.append((texte_liste.count(x)))
    return sum(occurence_mots)/nombre_mots

brute_force("Nazvagd Ymdfuz, fg qe gz bqfuf oaz, vq egue pqeaxq")