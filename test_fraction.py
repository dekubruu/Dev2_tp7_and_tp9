from fraction import Fraction

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

