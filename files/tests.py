# Dans l'éditeur PYTHON : fichier tests.py
# ============================================================================
# Import des modules ou classes nécessaires
# ============================================================================
from joueur import *
from jeucartes import *
from carte import *
from bataille import *
import unittest
# ============================================================================
# Fichier ayant pour objectif de tester la réaction de la fonction
# "jouer_bataille()" pour vérifier que la fonction ne comporte pas de bug
# et qu'elle fonctionne dans tout les cas de figure
# ============================================================================

## Fonction permettant le renvoi de success si la condition n'est pas levée ##

def test_assertion(condition, message="Success"):
    try:
        assert condition
        print(message)
    except AssertionError:
        print("AssertionError: Condition non respectée!")
        
########## Assertions ##########
        
test_assertion(jouer_bataille())
        
