class Fraction:
    """Class representing a fraction and operations on it

    Author : V. Van den Schrieck
    Date : October 2021
    This class allows fraction manipulations through several operations.
    """

    def __init__(self, num=0, den=1):
        """This builds a fraction based on some numerator and denominator.

        PRE : den must not be 0.
        POST : Initializes a fraction with a numerator (num) and denominator (den) in reduced form.
        """
        pass

    @property
    def numerator(self):
        """Return the numerator in reduced form."""
        pass

    @property
    def denominator(self):
        """Return the denominator of the fraction."""
        pass

    # ------------------ Textual representations ------------------

    def __str__(self):
        """Return a textual representation of the reduced form of the fraction.

        PRE : None.
        POST : Returns a string representing the fraction in reduced form
               ("num/den" if den != 1, or just "num" if den == 1).
        """
        pass

    def as_mixed_number(self):
        """Return a textual representation of the reduced form of the fraction as a mixed number.

        A mixed number is the sum of an integer and a proper fraction.

        PRE : None.
        POST : Returns a string representing the fraction as a mixed number
               ("integer part proper_fraction" if applicable, otherwise just "integer").
        """
        pass

    # ------------------ Operators overloading ------------------

    def __add__(self, other):
        """Overloading of the + operator for fractions.

        PRE : other must be a Fraction.
        POST : Returns a new Fraction representing the sum of the two fractions.
        """
        pass

    def __sub__(self, other):
        """Overloading of the - operator for fractions.

        PRE : other must be a Fraction.
        POST : Returns a new Fraction representing the difference of the two fractions.
        """
        pass

    def __mul__(self, other):
        """Overloading of the * operator for fractions.

        PRE : other must be a Fraction.
        POST : Returns a new Fraction representing the product of the two fractions.
        """
        pass

    def __truediv__(self, other):
        """Overloading of the / operator for fractions.

        PRE : other must be a Fraction and its numerator must not be 0.
        POST : Returns a new Fraction representing the division of the two fractions.
        """
        pass

    def __pow__(self, other):
        """Overloading of the ** operator for fractions.

        PRE : other must be an integer.
        POST : Returns a new Fraction representing the fraction raised to the power other.
        """
        pass

    def __eq__(self, other):
        """Overloading of the == operator for fractions.

        PRE : other must be a Fraction.
        POST : Returns True if the two fractions are equivalent, otherwise False.
        """
        pass

    def __float__(self):
        """Returns the decimal value of the fraction.

        PRE : None.
        POST : Returns the decimal (floating-point) value of the fraction.
        """
        pass

    # ------------------ Properties checking ------------------

    def is_zero(self):
        """Check if a fraction's value is 0.

        PRE : None.
        POST : Returns True if the fraction is equal to 0, otherwise False.
        """
        pass

    def is_integer(self):
        """Check if a fraction is integer (e.g., 8/4, 3, 2/2).

        PRE : None.
        POST : Returns True if the fraction is an integer, otherwise False.
        """
        pass

    def is_proper(self):
        """Check if the absolute value of the fraction is < 1.

        PRE : None.
        POST : Returns True if the absolute value of the fraction is less than 1, otherwise False.
        """
        pass

    def is_unit(self):
        """Check if a fraction's numerator is 1 in its reduced form.

        PRE : None.
        POST : Returns True if the numerator is 1 and the fraction is in reduced form, otherwise False.
        """
        pass

    def is_adjacent_to(self, other):
        """Check if two fractions differ by a unit fraction.

        Two fractions are adjacent if the absolute value of the difference is a unit fraction.

        PRE : other must be a instance of Fraction.
        POST : Returns True if the two fractions are adjacent, otherwise False.
        """
        pass
