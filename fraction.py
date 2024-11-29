"""
Module Fraction
----------------
Ce module définit la classe Fraction, qui permet de manipuler des nombres rationnels
et d'effectuer des opérations arithmétiques (addition, soustraction, multiplication, division).
"""


class Fraction:
    def __init__(self, numerateur, denominateur):
        if denominateur == 0:
            raise ValueError("Le dénominateur ne peut pas être nul.")
        self.numerateur = numerateur
        self.denominateur = denominateur

    def __str__(self):
        return f"{self.numerateur}/{self.denominateur}"

    def simplifie(self):
        def pgcd(a, b):
            while b:
                a, b = b, a % b
            return a

        facteur = pgcd(self.numerateur, self.denominateur)
        self.numerateur //= facteur
        self.denominateur //= facteur

    def __add__(self, autre):
        numerateur = self.numerateur * autre.denominateur + autre.numerateur * self.denominateur
        denominateur = self.denominateur * autre.denominateur
        return Fraction(numerateur, denominateur)

    def __eq__(self, autre):
        return (self.numerateur * autre.denominateur) == (self.denominateur * autre.numerateur)

    def __sub__(self, autre):
        numerateur = self.numerateur * autre.denominateur - autre.numerateur * self.denominateur
        denominateur = self.denominateur * autre.denominateur
        return Fraction(numerateur, denominateur)

    def __mul__(self, autre):
        numerateur = self.numerateur * autre.numerateur
        denominateur = self.denominateur * autre.denominateur
        return Fraction(numerateur, denominateur)

    def __truediv__(self, autre):
        if autre.numerateur == 0:
            raise ZeroDivisionError("Division par zéro interdite.")
        numerateur = self.numerateur * autre.denominateur
        denominateur = self.denominateur * autre.numerateur
        return Fraction(numerateur, denominateur)


# Création et affichage de fractions
f1 = Fraction(1, 2)
f2 = Fraction(2, 3)
print("Fraction 1:", f1)
print("Fraction 2:", f2)

# Addition de fractions
f3 = f1 + f2
print("Addition:", f3)

# Simplification
f3.simplifie()
print("Simplifiée:", f3)

# Comparaison
print("f1 et f2 sont égales :", f1 == f2)

# Test des nouvelles opérations
f4 = f1 - f2
print("Soustraction:", f4)

f5 = f1 * f2
print("Multiplication:", f5)

f6 = f1 / f2
print("Division:", f6)
