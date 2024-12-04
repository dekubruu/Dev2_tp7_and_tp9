from fraction import Fraction

def main():
    try:
        # Basic operations
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 4)
        print(f"Addition: {f1} + {f2} = {f1 + f2}")
        print(f"Subtraction: {f1} - {f2} = {f1 - f2}")
        print(f"Multiplication: {f1} * {f2} = {f1 * f2}")
        print(f"Division: {f1} / {f2} = {f1 / f2}")

        # Integer operations
        print(f"Addition with int: {f1} + 1 = {f1 + 1}")
        print(f"Subtraction with int: {f1} - 1 = {f1 - 1}")

        # Simplification test
        f3 = Fraction(6, 8)
        print(f"Simplified fraction: {f3}")

        # Float conversion
        print(f"Decimal value: {float(f1)}")

        f4 = Fraction(1, 1)
        f5 = Fraction(1, 3)
        f6 = Fraction(1, 3)

        print(f4.is_zero())  # False
        print(f6.is_integer())  # True (2/4 = 1/2)
        print(f4.is_proper())  # True
        print(f6.is_unit())  # False (numérateur != 1 après simplification)
        print(f4.is_adjacent_to(f5))  # True (1/2 - 1/3 = 1/6)

        # Exception handling
        try:
            Fraction(1, 0)
        except ValueError as e:
            print(f"Error: {e}")

        try:
            f1 / Fraction(0)
        except ZeroDivisionError as e:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Unexpected error: {e}")




if __name__ == "__main__":
    main()
