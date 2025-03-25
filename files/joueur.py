# Dans l'éditeur PYTHON : fichier joueur.py

from jeucartes import *


# Classe Joueur
class Joueur:
    def __init__(self, nom):
        self.nom = nom
        self.mainJoueur = []
        self.nbCartes = len(self.mainJoueur)
        
        
################# Définition des méthodes d'instances avec contrôle #######
        
    def setMain(self,jeuCartes):
        '''définit la main du joueur au début du jeu
        post : renvoie une liste d'objet'''
        for i in range(26):
            self.mainJoueur.append(jeuCartes.distribuerCarte())
        return self.mainJoueur
        
    def getNom(self):
        '''renvoie le nom du joueur
        post : renvoie une str'''
        return self.nom
        
    def getNbCartes(self):
        '''renvoie le nb de cartes dans la main du joueur
        post : renvoie un entier'''
        return len(self.mainJoueur)
        
    def jouerCarte(self):
        '''renvoie la derniere carte de la main du joueur pour la jouer et l'enleve
        post : renvoie un objet de type Carte ou None si la liste self.mainJoueur
        est vide '''
        carte_jouée = self.mainJoueur[0]
        del self.mainJoueur[0]
        return carte_jouée
         
         
    def insererMain(self,liste_gagnées):
        ''' insere les cartes de la liste des cartes gagnées dans la main du Joueur
        pre : rentre la carte jouée du joueur et la carte de l'autre joueur
        post : les ajoute a la liste self.mainJoueur '''
        self.mainJoueur += liste_gagnées
        
#################### Test de la classe Joueur #######
        
        
def test():
    jeu52 = JeuCartes(52)
    jeu52.creerJeu()
    jeu52.melanger()
    
    J1 = Joueur("Martin")
    print(J1.getNom())
    J1.setMain(jeu52)
    print(J1.jouerCarte())