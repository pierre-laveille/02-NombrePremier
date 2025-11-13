"""Module principal : affichage des nombres premiers inférieurs à 100."""

from math import sqrt


def isprime(p):
    """
    Retourne la valeur de vérité de la question : p est un nombre premier.

    Args:
        p (int): Valeur entière à tester.

    Returns:
        bool: True si p est premier, False sinon.
    """
    if p in (0, 1):
        return False
    for i in range(2, int(sqrt(p)) + 1):
        if p % i == 0:
            return False
    return True


def main():
    """
    Fonction principale : affiche les nombres premiers de 0 à 99.
    """
    for n in range(100):
        if isprime(n):
            print(n, end=", ")
    print()


if __name__ == "__main__":
    main()
