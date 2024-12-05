import unittest
from fraction import Fraction


class TestFraction(unittest.TestCase):

    def test_init_and_properties(self):
        """Test de l'initialisation et des propriétés."""
        f1 = Fraction(3, 4)
        self.assertEqual(f1.numerator, 3)
        self.assertEqual(f1.denominator, 4)

        f2 = Fraction(-5, 10)
        self.assertEqual(f2.numerator, -1)
        self.assertEqual(f2.denominator, 2)

        f3 = Fraction(0, 7)
        self.assertEqual(f3.numerator, 0)
        self.assertEqual(f3.denominator, 1)

        with self.assertRaises(ValueError):
            Fraction(1, 0)  # Test d'une exception pour un dénominateur nul

    def test_as_mixed_number(self):
        """Test de la conversion en nombre mixte."""
        self.assertEqual(Fraction(7, 2).as_mixed_number(), "3 1/2")
        self.assertEqual(Fraction(-7, 2).as_mixed_number(), "-3 1/2")
        self.assertEqual(Fraction(4, 2).as_mixed_number(), "2")
        self.assertEqual(Fraction(1, 2).as_mixed_number(), "1/2")

    def test_is_proper(self):
        """Test de la méthode is_proper."""
        self.assertTrue(Fraction(1, 2).is_proper())
        self.assertFalse(Fraction(3, 2).is_proper())
        self.assertTrue(Fraction(-1, 2).is_proper())
        self.assertFalse(Fraction(-3, 2).is_proper())

    def test_operations(self):
        """Test des opérations arithmétiques."""
        # Addition
        self.assertEqual(Fraction(1, 2) + Fraction(1, 2), Fraction(1, 1))
        self.assertEqual(Fraction(3, 4) + Fraction(-1, 4), Fraction(1, 2))

        # Soustraction
        self.assertEqual(Fraction(3, 4) - Fraction(1, 4), Fraction(1, 2))
        self.assertEqual(Fraction(1, 2) - Fraction(3, 4), Fraction(-1, 4))

        # Multiplication
        self.assertEqual(Fraction(2, 3) * Fraction(3, 4), Fraction(1, 2))
        self.assertEqual(Fraction(-2, 3) * Fraction(3, 4), Fraction(-1, 2))

        # Division
        self.assertEqual(Fraction(1, 2) / Fraction(1, 4), Fraction(2, 1))
        self.assertEqual(Fraction(-1, 2) / Fraction(1, 4), Fraction(-2, 1))

        with self.assertRaises(ZeroDivisionError):
            Fraction(1, 2) / Fraction(0, 1)

    def test_comparison(self):
        """Test des comparaisons."""
        self.assertTrue(Fraction(1, 2) == Fraction(2, 4))
        self.assertFalse(Fraction(1, 2) == Fraction(2, 3))
        self.assertFalse(Fraction(1, 3) == Fraction(1, 2))

    def test_power(self):
        """Test des puissances."""
        self.assertEqual(Fraction(2, 3) ** 2, Fraction(4, 9))
        self.assertEqual(Fraction(2, 3) ** -1, Fraction(3, 2))
        self.assertEqual(Fraction(3, 2) ** 0, Fraction(1, 1))

    def test_is_zero(self):
        """Test de la méthode is_zero."""
        self.assertTrue(Fraction(0, 1).is_zero())
        self.assertFalse(Fraction(1, 2).is_zero())

    def test_is_integer(self):
        """Test de la méthode is_integer."""
        self.assertTrue(Fraction(4, 2).is_integer())
        self.assertFalse(Fraction(3, 2).is_integer())
        self.assertTrue(Fraction(0, 5).is_integer())

    def test_is_unit(self):
        """Test de la méthode is_unit."""
        self.assertTrue(Fraction(1, 3).is_unit())
        self.assertFalse(Fraction(2, 3).is_unit())

    def test_is_adjacent_to(self):
        """Test de la méthode is_adjacent_to."""
        f1 = Fraction(1, 3)
        f2 = Fraction(2, 3)
        f3 = Fraction(1, 2)
        f4 = Fraction(3, 4)

        # Cas attendus comme vrais
        self.assertTrue(f1.is_adjacent_to(f2))  # Différence = -1/3
        self.assertTrue(Fraction(1, 5).is_adjacent_to(Fraction(2, 5)))  # Différence = -1/5

        # Cas attendus comme faux
        self.assertFalse(f1.is_adjacent_to(f3), "1/3 et 1/2 ne sont pas adjacentes, différence = -1/6")  # Faux
        self.assertFalse(f1.is_adjacent_to(f4), "1/3 et 3/4 ne sont pas adjacentes")


if __name__ == "__main__":
    unittest.main()
