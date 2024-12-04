from fraction import Fraction

def main():
    try:
        # Création de fractions
        f1 = Fraction(2, 5)  # 2/5
        f2 = Fraction(7, 3)  # 7/3
        f3 = Fraction(-4, 6)  # -4/6 (réduit à -2/3)

        print("Fraction 1:", f1)
        print("Fraction 2:", f2)
        print("Fraction 3:", f3)

        # Test des propriétés
        print("f1 is zero:", f1.is_zero())  # False
        print("f3 is zero:", f3.is_zero())  # False
        print("f2 is integer:", f2.is_integer())  # False
        print("Fraction 3 is proper:", f3.is_proper())  # True

        # Test des opérateurs arithmétiques
        f4 = f1 + f3
        f5 = f2 - f1
        f6 = f1 * f3
        f7 = f2 / f1

        print("f1 + f3 =", f4)  # 2/5 + (-2/3) = -4/15
        print("f2 - f1 =", f5)  # 7/3 - 2/5 = 29/15
        print("f1 * f3 =", f6)  # 2/5 * (-2/3) = -4/15
        print("f2 / f1 =", f7)  # 7/3 ÷ 2/5 = 35/6

        # Test d'autres opérations
        f8 = f2 ** 2
        print("f2 ** 2 =", f8)  # 7/3 ** 2 = 49/9

        # Test de la méthode as_mixed_number
        f9 = Fraction(-10, 4)
        print("Fraction 9 as mixed number:", f9.as_mixed_number())  # -3 1/2

        # Test d'exceptions
        try:
            f10 = Fraction(3, 0)  # Denominator cannot be zero
        except ValueError as e:
            print("Caught exception:", e)

        # Test de fractions adjacentes
        f11 = Fraction(3, 5)
        f12 = Fraction(4, 5)
        print("f11 is adjacent to f12:", f11.is_adjacent_to(f12))  # True (difference = 1/5)

    except Exception as e:
        print("An error occurred:", e)

if __name__ == "__main__":
    main()
