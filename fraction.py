from typing import Union
import math

class Fraction:
    """Class representing a fraction and operations on it.

    Supports exact arithmetic operations and ensures fractions are always simplified.
    """

    def __init__(self, numerator: int, denominator: int):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero.")

        gcd = math.gcd(numerator, denominator)
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    @property
    def numerator(self) -> int:
        return self._numerator

    @property
    def denominator(self) -> int:
        return self._denominator



    @staticmethod
    def _pgcd(a: int, b: int) -> int:
        """Compute the greatest common divisor (GCD) using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number."""
        if self.numerator % self.denominator == 0:
            # La fraction est un entier
            return str(self.numerator // self.denominator)

        whole = self.numerator // self.denominator
        fraction_part = abs(self.numerator) % abs(self.denominator)

        if self.numerator < 0 and fraction_part != 0:
            whole = whole + 1  # Ajuste correctement pour les fractions négatives

        if whole == 0:
            # La fraction n'a pas de partie entière
            return f"{self.numerator}/{self.denominator}"

        return f"{whole} {fraction_part}/{abs(self.denominator)}"

    def __str__(self) -> str:
        """Returns a string representation of the fraction."""
        return f"{self.numerator}/{self.denominator}" if self.denominator != 1 else str(self.numerator)

    def __add__(self, other: Union["Fraction", int]) -> "Fraction":
        """Addition of fractions or integers."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator + other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        raise TypeError("Addition is only supported between Fractions or integers.")

    def __sub__(self, other: Union["Fraction", int]) -> "Fraction":
        """Subtraction of fractions or integers."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        raise TypeError("Subtraction is only supported between Fractions or integers.")

    def __mul__(self, other: Union["Fraction", int]) -> "Fraction":
        """Multiplication of fractions or integers."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.numerator * other.numerator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        raise TypeError("Multiplication is only supported between Fractions or integers.")

    def __pow__(self, exp):
        """Élève une fraction à une puissance entière."""
        if exp < 0:
            return Fraction(self.denominator ** abs(exp), self.numerator ** abs(exp))
        return Fraction(self.numerator ** exp, self.denominator ** exp)

    def __truediv__(self, other: Union["Fraction", int]) -> "Fraction":
        """Division of fractions or integers."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            if other.numerator == 0:
                raise ZeroDivisionError("Cannot divide by zero.")
            num = self.numerator * other.denominator
            den = self.denominator * other.numerator
            return Fraction(num, den)
        raise TypeError("Division is only supported between Fractions or integers.")

    def __eq__(self, other: object) -> bool:
        """Equality check between fractions."""
        if isinstance(other, Fraction):
            return self.numerator * other.denominator == self.denominator * other.numerator
        return False

    def __float__(self) -> float:
        """Return the decimal value of the fraction."""
        return self.numerator / self.denominator

    def is_zero(self) -> bool:
        """Check if a fraction's value is 0"""
        return self.numerator == 0

    def is_integer(self) -> bool:
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2)."""
        return self.numerator % self.denominator == 0

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1."""
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form."""
        return self.numerator == 1

    def __sub__(self, other: Union["Fraction", int]) -> "Fraction":
        """Soustraction des fractions ou des entiers."""
        if isinstance(other, int):
            other = Fraction(other, 1)
        if isinstance(other, Fraction):
            num = self.numerator * other.denominator - other.numerator * self.denominator
            den = self.denominator * other.denominator
            return Fraction(num, den)
        raise TypeError("La soustraction est uniquement supportée entre des fractions ou des entiers.")

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Vérifie si deux fractions sont adjacentes, c'est-à-dire si leur différence est égale à 1 ou -1."""
        difference = self - other
        # Debug: affiche la différence pour vérifier qu'elle est correcte
        print(f"Debug: Différence entre {self} et {other} est {difference}")
        # Vérifier si la différence est une fraction d'unité
        return abs(difference.numerator) == 1 and difference.denominator == 1



