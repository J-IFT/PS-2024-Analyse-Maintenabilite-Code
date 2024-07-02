"""Module : Fibonacci Tests """

import unittest
from fonction_iterative_ameliorations import fibonacci_iteratif

class TestFibonacciIteratif(unittest.TestCase):
    """
    Classe de tests unitaires pour la fonction fibonacci_iteratif.

    Cette classe teste différentes situations d'entrée pour s'assurer que la fonction
    fibonacci_iteratif calcule correctement les nombres de Fibonacci de manière itérative.
    """

    def test_fibonacci_positif(self):
        """
        Teste les valeurs positives correctes pour la fonction fibonacci_iteratif.
        """
        self.assertEqual(fibonacci_iteratif(1), 0)
        self.assertEqual(fibonacci_iteratif(2), 1)
        self.assertEqual(fibonacci_iteratif(3), 1)
        self.assertEqual(fibonacci_iteratif(4), 2)
        self.assertEqual(fibonacci_iteratif(5), 3)
        self.assertEqual(fibonacci_iteratif(6), 5)
        self.assertEqual(fibonacci_iteratif(10), 34)
        self.assertEqual(fibonacci_iteratif(15), 377)

    def test_fibonacci_zero_et_negatif(self):
        """
        Teste les valeurs zéro et négatives pour la fonction fibonacci_iteratif.
        """
        self.assertEqual(fibonacci_iteratif(0), 0)
        self.assertEqual(fibonacci_iteratif(-1), "Entrée invalide, nombre doit être un entier positif.")
        self.assertEqual(fibonacci_iteratif(-10), "Entrée invalide, nombre doit être un entier positif.")

    def test_fibonacci_non_entier(self):
        """
        Teste les valeurs non entières pour la fonction fibonacci_iteratif.
        """
        self.assertEqual(fibonacci_iteratif(1.5), "Entrée invalide, nombre doit être un entier positif.")
        self.assertEqual(fibonacci_iteratif("abc"), "Entrée invalide, nombre doit être un entier positif.")
        self.assertEqual(fibonacci_iteratif([]), "Entrée invalide, nombre doit être un entier positif.")
        self.assertEqual(fibonacci_iteratif({}), "Entrée invalide, nombre doit être un entier positif.")

    def test_fibonacci_type_none(self):
        """
        Teste le paramètre None pour la fonction fibonacci_iteratif.
        """
        self.assertEqual(fibonacci_iteratif(None), "Entrée invalide, nombre doit être un entier positif.")

if __name__ == '__main__':
    unittest.main()
