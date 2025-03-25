# Dans l'éditeur PYTHON : fichier jeucartes.py

from carte import * # Il faut importer la classe Carte et les variables globales
import random # Nécessaire pour mélanger le jeu

class JeuCartes():
    def __init__(self, nbCartes=52):
        # Le jeu doit comporter 32 ou 52 cartes, effectuer un contrôle
        self.jeu = [] # self.jeu est une liste des self.nbCartes
        ...# à compléter

    #####################################################################
    ############## Définition des méthodes d'instances ##################
    #####################################################################
    def getTailleJeu(self):
        ''' Fonction qui retourne le nombre de cartes du jeu
        post : renvoie un nombre entier'''
        return len(self.jeu)
        
    def creerJeu(self): # utilise des objet
        '''Crée la liste des cartes de l'attribut self.jeu '''
        for val in noms:
            for coul in couleurs:
                self.jeu.append(Carte(val,coul))

    def getJeu(self):
        '''Renvoie la liste des cartes correspondant à l'attribut self.jeu
        post : renvoie une liste '''
        return self.jeu

    def melanger(self): # utiliser le module random ...
        '''Mélange sur place les cartes de la liste des cartes associée au champ
        self.jeu
        post : renvoie une liste'''
        return random.shuffle(self.jeu)
        
        

    def distribuerCarte(self):
        ''' Cette fonction permet de distribuer une carte à un joueur. Elle
        retourne la carte
        post : renvoie un objet de type carte '''
        return self.jeu.pop()
    

    def distribuerJeu(self, nbJoueurs, nbCartes):
        ''' Cette méthode distribue nbCartes à chacun des nbJoueurs,
        post : renvoie une liste de sous-listes'''
        jeuxJoueurs = []
        if (nbJoueurs*nbCartes)>len(self.jeu):
            print('Pas assez de cartes dans le jeu')
            return 
        for i in range(nbJoueurs):
            jeuxJoueurs.append([])
            for j in range(nbCartes):
                jeuxJoueurs[i].append(self.distribuerCarte())
        return jeuxJoueurs
        
                
#################### Test de la classe JeuCartes #######

def testJeuCartes():

    jeu52 = JeuCartes(52)
    jeu52.creerJeu()
    jeu52.melanger()
    
    L=jeu52.getJeu()
    carte = L[2] # la 3e carte
    print('Nom:', carte.getNom())
    print('Couleur:', carte.getCouleur())
    print('Valeur:', carte.getValeur())

    # Distribution de 4 cartes à 3 joueurs
    distribution_3j_4c = jeu52.distribuerJeu(3, 4)
    for i in range(3):
        print('Joueur', i+1, ':')
        listeCartes = distribution_3j_4c[i]
        for c in listeCartes:
            print(c.getNom(), 'de', c.getCouleur())

    # Distribution de 10 cartes à 6 joueurs pour générer une exception (6X10 > 52)
    distribution_6_joueurs_10_cartes_par_joueur = jeu52.distribuerJeu(6, 10)