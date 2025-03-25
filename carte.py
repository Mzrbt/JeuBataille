# Dans l'éditeur PYTHON : fichier carte.py
# Variables globales

couleurs = ('CARREAU', 'COEUR', 'TREFLE', 'PIQUE')

noms = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']

valeurs = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10':
           10, 'Valet': 11, 'Dame': 12, 'Roi': 13, 'As': 14}

# Classe Carte :
'''donne un nom, une couleur et une valeur a un objet carte et permet de tester
egalités des valeurs des cartes'''
class Carte:
    def __init__(self, nom, couleur):
        # Affectation des attributs nom et couleur avec contrôle.
        self.nom = nom
        self.couleur = couleur
        self.valeur = valeurs[nom]
        if not self.couleur in couleurs:
            print('La couleur de la carte est incorrect:', self.couleur )#affiche message d'erreur si la couleur n'existe pas 
        if not self.nom in noms:
            print('Le nom de la carte est incorrect:', self.nom )#affiche message d'erreur si le nom n'existe pas
            
    def __str__(self):
        return f'{self.nom} de {self.couleur}'

################# Définition des méthodes d'instances avec contrôle #######

    def setNom(self, nom):# setter
        self.nom = nom
        self.valeur = valeurs[nom]

    def getNom(self):# getter
        if self.nom in noms:#pour ne pas renvoyer le nom si il n'existe pas  
            return self.nom

    def getCouleur(self):# getterDescription
        if self.couleur in couleurs:#pour ne pas renvoyer la couleur si elle n'existe pas  
            return self.couleur
        

    def getValeur(self): # getter
        return self.valeur

    def egalite(self, carte):
        ''' Renvoie True si les cartes ont même valeur, False sinon
        pre: carte est un objet de type Carte
        post : renvoie un booléen'''
        return carte.getValeur() == self.valeur
    
    def estSuperieureA(self, carte):
        ''' Renvoie True si la valeur de self est supérieure à celle de
            carte, False sinon
            pre : carte est un objet de type Carte
            post : renvoie un booléen'''
        return self.valeur > carte.getValeur()
    
    def estInferieureA(self, carte):
        ''' Renvoie True si la valeur de self est inferieure à celle de
            carte, False sinon
            pre : carte est un objet de type Carte
            post : renvoie un booléen '''
        return self.valeur < carte.getValeur()
    
        
########################################################
#################### Test de la classe Carte ###########
########################################################
def testCarte():
    valetCoeur = Carte('Valet', 'COEUR')
    print('Nom:', valetCoeur.getNom())
    print('Couleur:', valetCoeur.getCouleur())
    print('Valeur:', valetCoeur.getValeur())
    valetCoeur.setNom('Dame')
    print('Nom modifie:', valetCoeur.getNom())
    print('Valeur modifiee:', valetCoeur.getValeur())
    # Essai des exceptions: cette instruction conduit à une erreur
    dameCoeur = Carte('Dame', 'COooEUR')
