from typing import Union

class Fraction:
    """Class representing a fraction and operations on it.

    Supports exact arithmetic operations and ensures fractions are always simplified.
    """

    def __init__(self, num: int = 0, den: int = 1):
        """Initialize a fraction with numerator and denominator.

        PRE : den != 0
        POST : The fraction is reduced to its simplest form.
        RAISES : ValueError if the denominator is zero.
        """
        if den == 0:
            raise ValueError("Denominator cannot be zero.")
        self._numerator = num
        self._denominator = den
        self._simplify()

    @property
    def numerator(self) -> int:
        """Returns the numerator of the fraction."""
        return self._numerator

    @property
    def denominator(self) -> int:
        """Returns the denominator of the fraction."""
        return self._denominator

    def _simplify(self):
        """Simplify the fraction using the greatest common divisor (GCD)."""
        gcd = self._pgcd(abs(self._numerator), abs(self._denominator))
        self._numerator //= gcd
        self._denominator //= gcd
        if self._denominator < 0:  # Ensure denominator is always positive
            self._numerator *= -1
            self._denominator *= -1

    @staticmethod
    def _pgcd(a: int, b: int) -> int:
        """Compute the greatest common divisor (GCD) using Euclid's algorithm."""
        while b:
            a, b = b, a % b
        return a

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
        """Check if a fraction's value is 0

        PRE: The fraction is valid (denominator != 0).
        POST: Returns True if the fraction equals 0, False otherwise.
        """
        return self.numerator == 0

    def is_integer(self) -> bool:
        """Check if a fraction is an integer (e.g., 8/4, 3, 2/2).

        PRE: The fraction is valid (denominator != 0).
        POST: Returns True if the fraction is an integer, False otherwise.
        """
        return self.numerator % self.denominator == 0

    def is_proper(self) -> bool:
        """Check if the absolute value of the fraction is < 1.

        PRE: The fraction is valid (denominator != 0).
        POST: Returns True if the absolute value of the fraction is < 1, False otherwise.
        """
        return abs(self.numerator) < abs(self.denominator)

    def is_unit(self) -> bool:
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE: The fraction is valid (denominator != 0) and reduced.
        POST: Returns True if the numerator is 1, False otherwise.
        """
        return self.numerator == 1

    def is_adjacent_to(self, other: 'Fraction') -> bool:
        """Check if two fractions differ by a unit fraction.

        PRE: Both fractions are valid (denominator != 0).
        POST: Returns True if the absolute value of the difference is a unit fraction, False otherwise.
        """
        difference = self - other
        difference._simplify()
        return abs(difference.numerator) == 1 and difference.denominator != 0
