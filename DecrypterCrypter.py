"""Algorithmes de cryptages et décryptage en Cesar"""

import unicodedata

alphabet_min = ('a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z')
alphabet_maj = ('A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U',
                'V', 'W', 'X', 'Y', 'Z')
chiffres = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9')

def crypter(texte, clef):
    texte = unicodedata.normalize('NFD', texte).encode(encoding='ASCII', errors='ignore').decode('utf8')
    texte_crypte = ''
    for i in texte:
        if i in alphabet_min:
            idx = alphabet_min.index(i)
            idx_crypte = (idx + clef) % 26
            lettre_cryptee = alphabet_min[idx_crypte]
        elif i in alphabet_maj:
            idx = alphabet_maj.index(i)
            idx_crypte = (idx + clef) % 26
            lettre_cryptee = alphabet_maj[idx_crypte]
        elif i in chiffres:
            idx = chiffres.index(i)
            idx_crypte = (idx + clef) % 9
            lettre_cryptee = chiffres[idx_crypte]
        else:
            lettre_cryptee = i
        texte_crypte += lettre_cryptee
    return texte_crypte, clef


def decrypter(texte, clef):
    return crypter(texte, -clef)[0], -crypter(texte, -clef)[1]
