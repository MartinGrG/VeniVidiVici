# VeniVidiVici
Algorithme pour encoder/décoder un texte via le chiffrement Cesar

## Fonctionnement:
L'utilisteur peut cypter ou décrypter:
- un message qu'il écrit directement dans le terminal 
- un fichier texte  
Il lui suffit ensuite de rentrer la clef de cryptage et il obtient le message crypté/décrypté.
Dans le cas où l'utilisateur ne connait pas la clef de cryptage, il est possible de l'estimer par la méthode brute force.




## Composition
Le projet est composé de 4 fichiers:
- main.py : fichier à "run" pour lancer le projet
- Interface.py : programme mettant en place l'interface utilisateur 
- GestionFichier.py : programme gérant l'ouverture, la lecture  et l'écriture de fichier textes
- DecrypterCrypter.py : algorithmes de cryptage et décryptage

![Architecture code](architecture_code.png) 