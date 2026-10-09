# -*- coding: utf-8 -*-

from random import shuffle

### Version POO simplifiée
### Fichier à compléter
### Volontairement, les signatures de certaines fonctions sont incomplètes, à vous de les compléter !

class Carte():
    """Objet représentant une carte d'un jeu de 52 cartes
    valeur entière de 2 à 14, 11 pour le Valet, 12 pour la Dame,
    13 pour le Roi et 14 pour l'As"""

    def __init__(...):
        """Constructeur"""

    def __str__(self):
        """Methode permettant de visualiser une carte sous forme lisible, 
        comme 2 de Pique ou Dame de Coeur"""
        ...

    def __repr__(self):
        """Fournit une représentation en chaîne de caractères officielle, 
        souvent utile pour le débogage et la reconstruction de l'objet. Deja codee"""
        return self.__str__()

    def __gt__(self, other):
        """Surcharge de l'opérateur >"""
        ...

    def __eq__(self, other):
        """Surcharge de l'opérateur =="""
        ...


class JeuDeCartes():
    """Objet représentant un jeu de 52 cartes"""

    def __init__(self):
        """Constructeur. Créé les 52 cartes des 4 couleurs et les ajoute à l'attribut paquet"""
        ...

    def melange(self):
        """Mélange le paquet. Méthode terminée"""
        shuffle(self.paquet)


class Joueur():
    """Objet représentant un joueur de cartes"""

    def __init__(...):
        """Constructeur"""


    def __str__(self):
        """Doit convertir la première lettre d'une chaîne de caractères en majuscule et toutes les autres lettres en minuscules."""
        ...

    def __repr__(self):
        """Appelle __str__"""
        ...


class Partie():
    """Objet représentant une partie de Bataille"""

    def __init__(...):
        """Constructeur"""
        # Création des 2 joueurs
        
        # Création et mélange du jeu de carte
        
        # Distribution des cartes aux deux joueurs

        # Statistiques

    def joue(self):
        """Tant que les 2 joueurs ont encore des cartes, on compare celle du haut du tas que l'on enlève (pop)
         S'il y a bataille, on appelle la méthode concernée
         Si la partie est finie, on affiche les informations requises"""
        ...

    def joue_bataille(self, carte_1, carte_2):
        """Méthode appelée par 'joue' Il faut tirer une carte masquée et une carte visible. Peut redéclancher une bataille """
        print("Bataille !")
        ...

if __name__ == "__main__":
    p = Partie("Toto", "Titi")
    p.joue()
