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
    valeur entière de 0 à 12 : 0 pour le 2, ..., 11 pour le Roi
    et 12 pour l'As"""
    valeurCarte = {
        0: "2",
        1: "3",
        2: "4",
        3: "5",
        4: "6",
        5: "7",
        6: "8",
        7: "9",
        8: "10",
        9: "Valet",
        10: "Dame",
        11: "Roi",
        12: "As",
    }

    def __init__(self, valeur, couleur):
        self.valeur = valeur
        self.couleur = couleur

    def __str__(self):
        """Methode permettant de visualiser une carte sous forme lisible, 
        comme 2 de Pique ou Dame de Coeur"""
        return self.valeurCarte[self.valeur] + " de " + self.couleur    

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
            for valeur in range(13):
                self.paquet.append(Carte(valeur, couleur))

    def melange(self):
        shuffle(self.paquet)


class Joueur():
    """Objet représentant un joueur de cartes"""

    def __init__(self, id):
        self.id = id
        self.jeu = []
        self.gain = []

    def __str__(self):
        return self.id.capitalize()

    def __repr__(self):
        return self.__str__()


class Partie():
    """Objet représentant une partie de Bataille"""
    nb_tours = 0
    nb_batailles = 0
    

    def __init__(self, joueur1, joueur2):
        """Constructeur"""
        # Création des 2 joueurs
        self.joueurs = (Joueur(joueur1), Joueur(joueur2))

        # Création et mélange du jeu de carte
        self.jeu = JeuDeCartes()
        self.jeu.melange()

        # Distribution des cartes aux deux joueurs
        for i in range(26):
            self.joueurs[0].jeu.append(self.jeu.paquet.pop())
            self.joueurs[1].jeu.append(self.jeu.paquet.pop())

        # Statistiques
        #TODO c'est quoi que je criss la

    def joue(self):
        """Tant que les 2 joueurs ont encore des cartes, on compare celle du haut du tas que l'on enlève (pop)
         S'il y a bataille, on appelle la méthode concernée
         Si la partie est finie, on affiche les informations requises"""
        print("Début de la partie...")
        print(f"{self.joueurs[0]} --------- {self.joueurs[1]}")
        while self.joueurs[0].jeu and self.joueurs[1].jeu:
            print("...")
            self.nb_tours += 1
            carte_1 = self.joueurs[0].jeu.pop()
            carte_2 = self.joueurs[1].jeu.pop()
            
            print(f"{carte_1} --------- {carte_2}")
            if carte_1 > carte_2:
                print(f"{self.joueurs[0]} l'emporte!")
                self.joueurs[0].gain.append(carte_1)
                self.joueurs[0].gain.append(carte_2)
            elif carte_2 > carte_1:
                print(f"{self.joueurs[1]} l'emporte!")
                self.joueurs[1].gain.append(carte_1)
                self.joueurs[1].gain.append(carte_2)
            else:
                self.joue_bataille([carte_1, carte_2])
            #TODO WTf
            print(f"{self.joueurs[0]} a {len(self.joueurs[0].gain)} cartes et {self.joueurs[1]} a {len(self.joueurs[1].gain)} cartes.")
            
        #dire qui a gagné
        print("partie terminée en ", self.nb_tours, "tours et", self.nb_batailles, "batailles.")
        if len(self.joueurs[0].gain) > len(self.joueurs[1].gain):
            print(f"Victoir de {self.joueurs[0]}!")
        elif len(self.joueurs[1].gain) > len(self.joueurs[0].gain):
            print(f"Victoir de {self.joueurs[1]}!")
        else:
            print("La partie est terminée en égalité.")
            print(f"{self.joueurs[0]} a {len(self.joueurs[0].gain)} cartes et {self.joueurs[1]} a {len(self.joueurs[1].gain)} cartes.")

    def joue_bataille(self, cartes):
        """Méthode appelée par 'joue' Il faut tirer une carte masquée et une carte visible. Peut redéclancher une bataille """
        print("...")
        print("Bataille !")
        self.nb_batailles += 1

        carte_1 = self.joueurs[0].jeu.pop() if self.joueurs[0].jeu else None
        carte_2 = self.joueurs[1].jeu.pop() if self.joueurs[1].jeu else None

        carte_cachee_1 = self.joueurs[0].jeu.pop() if self.joueurs[0].jeu else None
        carte_cachee_2 = self.joueurs[1].jeu.pop() if self.joueurs[1].jeu else None

        if carte_1 and carte_2 and carte_cachee_1 and carte_cachee_2:
            print("Carte cachée --------- Carte cachée")
            print(f"{carte_1} --------- {carte_2}")
            if carte_1 > carte_2:
                print(f"{self.joueurs[0]} gagne la bataille!")
                self.joueurs[0].gain.append(cartes)
                self.joueurs[0].gain.append(carte_1)
                self.joueurs[0].gain.append(carte_2)
                self.joueurs[0].gain.append(carte_cachee_1)
                self.joueurs[0].gain.append(carte_cachee_2)
                
            elif carte_2 > carte_1:
                print(f"{self.joueurs[1]} gagne la bataille!")
                self.joueurs[1].gain.append(cartes)
                self.joueurs[1].gain.append(carte_1)
                self.joueurs[1].gain.append(carte_2)
                self.joueurs[1].gain.append(carte_cachee_1)
                self.joueurs[1].gain.append(carte_cachee_2)
            else:
                cartes.extend([carte_1, carte_2, carte_cachee_1, carte_cachee_2])
                self.joue_bataille(cartes)

if __name__ == "__main__":
    p = Partie("Toto", "Titi")
    p.joue()

    
