# -*- coding: utf-8 -*-

from random import shuffle

### Version POO simplifiée
### Fichier à compléter
### Volontairement, les signatures de certaines fonctions sont incomplètes, à vous de les compléter !

"""
valeur des cartes selon leur face
As: 12 
Roi: 11 
Dame: 10 
Valet: 9 
10: 8 
9: 7 
8: 6 
7: 5 
6: 4 
5: 3 
4: 2 
3: 1
2: 0




"""
class Carte():
    """Objet représentant une carte d'un jeu de 52 cartes
    valeur entière de 2 à 14, 11 pour le Valet, 12 pour la Dame,
    13 pour le Roi et 14 pour l'As"""
    valeurCarte = {
        "0": "2",
        "1": "3",
        "2": "4",
        "3": "5",
        "4": "6",
        "5": "7",
        "6": "8",
        "7": "9",
        "8": "10",
        "9": "Valet",
        "10": "Dame",
        "11": "Roi",
        "12": "As",
    }

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        """Methode permettant de visualiser une carte sous forme lisible, 
        comme 2 de Pique ou Dame de Coeur"""
        return self.valeurCarte[str(self.valeur)] + " de " + self.couleur    

    def __repr__(self):
        return self.__str__()

    def __gt__(self, other):
        """Surcharge de l'opérateur >"""
        return self.valeur > other.valeur

    def __eq__(self, other):
        """Surcharge de l'opérateur =="""
        return self.valeur == other.valeur


class JeuDeCartes():
    paquet = []

    def __init__(self):
        for couleur in ["Coeur", "Carreau", "Trèfle", "Pique"]:
            for valeur in range(2, 15):
                self.paquet.append(Carte(valeur, couleur))

    def melange(self):
        shuffle(self.paquet)


class Joueur():
    """Objet représentant un joueur de cartes"""

    def __init__(self):
        """Constructeur"""


    def __str__(self):
        """Doit convertir la première lettre d'une chaîne de caractères en majuscule et toutes les autres lettres en minuscules."""
        ...

    def __repr__(self):
        """Appelle __str__"""
        ...


class Partie():
    """Objet représentant une partie de Bataille"""

    def __init__(self):
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

    
