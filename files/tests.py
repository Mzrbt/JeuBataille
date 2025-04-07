# Dans l'éditeur PYTHON : fichier tests.py
# ============================================================================
# Import des modules ou classes nécessaires
# ============================================================================
from bataille import *
import unittest
# ============================================================================
# Fichier ayant pour objectif de tester la réaction de la fonction
# "jouer_bataille()" pour vérifier que la fonction ne comporte pas de bug
# et qu'elle fonctionne dans tout les cas de figure
# ============================================================================

class TestBataille(unittest.TestCase):

    def test_jouer_param_partie_terminee(self):
        bataille = Bataille()
        resultat = bataille.jouer_param("Alice", "Bob", 1000)
        self.assertIn("a perdu", resultat) or self.assertIn("a gagné", resultat)

    def test_jouer_param_egalite(self):
        bataille = Bataille()
        resultat = bataille.jouer_param("Alice", "Bob", 0)
        self.assertEqual(resultat, "Les deux joueurs ont 26 cartes")

    def test_resultat_contient_nom(self):
        bataille = Bataille()
        resultat = bataille.jouer_param("Alice", "Bob", 3)
        self.assertTrue("Alice" in resultat or "Bob" in resultat)

if __name__ == "__main__":
    unittest.main()

        
