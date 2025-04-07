# Dans l'éditeur PYTHON : fichier bataille.py
# =============================================================================
# Import des modules ou classes nécessaires
# =============================================================================
from joueur import *
from jeucartes import *
from carte import *
# =============================================================================
# Définition de la classe
# =============================================================================
class Bataille:
    def __init__(self, nbJoueur = 2, jeuCartes = 52):
        self.nbJoueur = nbJoueur
        self.jeuCartes = jeuCartes
        
################# Définition des méthodes d'instances avec contrôle #######

    def unTour(self, Joueur1,Joueur2):
        '''fait tourner un seul tour du jeu
        pre : prend 2 objets de types Joueur
        post : retourne un gagnant du tour, et une main de jeu differente pour les
        2 joueurs'''
        carteJ1 = Joueur1.jouerCarte()
        carteJ2 = Joueur2.jouerCarte()
        liste_gagnées = []#liste des cartes jouées lors du tour qui seront données au gagnant
        print(f'la carte de {Joueur1.getNom()} est {carteJ1}')
        print(f'la carte de {Joueur2.getNom()} est {carteJ2}')
        while carteJ1.egalite(carteJ2): 
            print('Bataille')
            liste_gagnées.append(carteJ1)
            liste_gagnées.append(carteJ2)
            carteJ1 = Joueur1.jouerCarte()
            carteJ2 = Joueur2.jouerCarte()#boucle while : cartes de valeurs egales; bataille
            liste_gagnées.append(carteJ1)
            liste_gagnées.append(carteJ2)
            carteJ1 = Joueur1.jouerCarte()
            carteJ2 = Joueur2.jouerCarte()
            print(f'La carte de {Joueur1.getNom()} apres la bataille est {carteJ1}')
            print(f'La carte de {Joueur2.getNom()} apres la bataille est {carteJ2}')
        if carteJ1.estSuperieureA(carteJ2):
            liste_gagnées.append(carteJ1)
            liste_gagnées.append(carteJ2)
            Joueur1.insererMain(liste_gagnées)
            return f'Le joueur {Joueur1.getNom()} a gagné ce tour.'
        elif carteJ2.estSuperieureA(carteJ1):
            liste_gagnées.append(carteJ1)
            liste_gagnées.append(carteJ2)
            Joueur2.insererMain(liste_gagnées)
            return f'Le joueur {Joueur2.getNom()} a gagné ce tour.'
        
        
    
        
    def jouer(self):
        '''crée un jeu, des joueurs et fait fonctionner le jeu
        post : retourne un gagnant du jeu''' 
        jeu52 = JeuCartes(52)
        jeu52.creerJeu()
        jeu52.melanger()
        nomJ1 = input('Rentrez le nom du premier joueur : ')
        nomJ2 = input('Rentrez le nom du deuxième joueur : ')
        J1 = Joueur(nomJ1)
        J2 = Joueur(nomJ2)
        J1.setMain(jeu52)
        J2.setMain(jeu52)
        nb_tour = int(input('Donnez le nombre de tour maximum que vous voulez faire : '))
        for i in range(nb_tour):
            print(self.unTour(J1,J2))
            print(f'Nombre de cartes de {J1.getNom()} : {J1.getNbCartes()}')
            print(f'Nombre de cartes de {J2.getNom()} : {J2.getNbCartes()}')
            if J1.getNbCartes() == 0:
                 return f"{J1.getNom()} a perdu, il n'a plus de cartes"
            if J1.getNbCartes() == 0:
                 return f"{J1.getNom()} a perdu, il n'a plus de cartes"
        if J1.getNbCartes() < J2.getNbCartes():
            return f'{J2.getNom()} a gagné la partie avec {J2.getNbCartes()} cartes contre {J1.getNbCartes()} cartes'
        elif J1.getNbCartes() > J2.getNbCartes():
            return f'{J1.getNom()} a gagné la partie avec {J1.getNbCartes()} cartes contre {J2.getNbCartes()} cartes'
        else :
            return 'Les deux joueurs ont 26 cartes'
        
    def jouer_param(self, nomJ1, nomJ2, nb_tour):
        '''Même fonction que jouer avec paramètres
        pour les assertions''' 
        jeu52 = JeuCartes(52)
        jeu52.creerJeu()
        jeu52.melanger()
        J1 = Joueur(nomJ1)
        J2 = Joueur(nomJ2)
        J1.setMain(jeu52)
        J2.setMain(jeu52)
        for i in range(nb_tour):
            print(self.unTour(J1,J2))
            print(f'Nombre de cartes de {J1.getNom()} : {J1.getNbCartes()}')
            print(f'Nombre de cartes de {J2.getNom()} : {J2.getNbCartes()}')
            if J1.getNbCartes() == 0:
                 return f"{J1.getNom()} a perdu, il n'a plus de cartes"
            if J1.getNbCartes() == 0:
                 return f"{J1.getNom()} a perdu, il n'a plus de cartes"
        if J1.getNbCartes() < J2.getNbCartes():
            return f'{J2.getNom()} a gagné la partie avec {J2.getNbCartes()} cartes contre {J1.getNbCartes()} cartes'
        elif J1.getNbCartes() > J2.getNbCartes():
            return f'{J1.getNom()} a gagné la partie avec {J1.getNbCartes()} cartes contre {J2.getNbCartes()} cartes'
        else :
            return 'Les deux joueurs ont 26 cartes'
    
# =============================================================================
# Programme principal 
# =============================================================================    
            
def jouer_bataille():
    '''fonction principal qui crée un objet de type Bataille et qui lance le jeu
    pre : retourne toutes les str des methodes et des autres classes'''
    bataille = Bataille()
    print(bataille.jouer_param('a','b',3))
                    
jouer_bataille()             
            
            
            
            
    
        
       
