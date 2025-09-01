#!/usr/bin/python3
import sys

def factorial(n):
    result = 1
    while n > 1:
        result *= n
        n -= 1
    return result

# Vérification du nombre d'arguments
if len(sys.argv) != 2:
    print("Usage: python3 script.py <entier_positif>")
    sys.exit(1)

try:
    value = int(sys.argv[1])
    if value < 0:
        raise ValueError("Le nombre doit être un entier positif.")
except ValueError as e:
    print("Erreur:", e)
    sys.exit(1)

# Calcul et affichage de la factorielle
f = factorial(value)
print(f)