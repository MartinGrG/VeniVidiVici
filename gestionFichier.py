"""Création des fonctions de lecture et écriture des fichiers textes """

from verifications import *
import os
import unicodedata


def lecture(nom_fichier):
    # Entrée : nom du fichier à lire
    # Sortie : le contenu du texte

    # On vérifie que le chemin existe
    while not os.path.exists(nom_fichier):
        afficher("Le fichier indiqué n'existe pas")
        afficher("entrer le nom du fichier")
        afficher("sous la forme")
        afficher("[mon_fichier.txt]")
        nom_fichier = input("-->")

    # Ouvrir le fichier en mode lecture
    with open(nom_fichier, 'r', encoding='utf8') as fio:
        # Lire le contenu du fichier
        contenu = fio.read()
        contenu = unicodedata.normalize('NFD', contenu).encode(encoding='ASCII', errors='ignore').decode('utf8')

    return contenu


def ecriture(contenu):
    # Entrée : contenu que l'on veut écrire
    # Sortie : créé un fichier texte contenant le contenu

    # On crée un fichier texte et on écrit dedans
    with open("message.txt", "w", encoding='utf8') as fio:
        fio.write(contenu)
        return "message.txt"


def modifier(nom_fichier, contenu):
    # Entrées : -nom du fichier à modifier
    #         -contenu à ajouter dans le fichier texte

    # Sortie : aucune, le fichier a été modifié

    # Test si le fichier existe bien
    while not os.path.exists(nom_fichier):
        afficher("Le fichier indiqué n'existe pas")
        afficher("entrer le nom du fichier")
        afficher("sous la forme")
        afficher("[mon_fichier.txt]")
        nom_fichier = input("-->")

    # Ouvrir le fichier texte en mode écriture
    with open(nom_fichier, "w", encoding='utf8') as fio:
        fio.write(contenu)
