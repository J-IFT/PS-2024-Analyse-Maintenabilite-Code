"""Module : Fibonacci """

def fibonacci(nombre: int, memo=None) -> int:
    """
    Calcule le n-ième nombre de Fibonacci de manière récursive.

    Paramètre:
    n (int): L'indice du nombre de Fibonacci à calculer. Doit être un entier positif.

    Retourne:
    int: Le n-ième nombre de Fibonacci si l'entrée est valide.
    str: Un message d'erreur si l'entrée est invalide.
    """
    try:
         # Vérification si nombre est un entier positif
        if not isinstance(nombre, int) or nombre <= 0:
            raise TypeError("Entrée invalide, nombre doit être un entier positif.")
        
        # Initialisation du dictionnaire de mémorisation si ce n'est pas déjà fait
        if memo is None:
            memo = {}

        # Vérification si le résultat pour nombre est déjà calculé et stocké dans le dictionnaire
        if nombre in memo:
            return memo[nombre]

        # Cas de base : Fibonacci(0) = 0 et Fibonacci(1) = 1
        if nombre == 1:
            return 0
        elif nombre == 2:
            return 1

        # Calcul de Fibonacci(nombre) en utilisant les résultats de Fibonacci(nombre-1) et Fibonacci(nombre-2)
        # et stockage du résultat dans le dictionnaire de mémorisation
        memo[nombre] = fibonacci(nombre-1, memo) + fibonacci(nombre-2, memo)
        return memo[nombre]

    except TypeError:
        return "Erreur : Le paramètre 'nombre' doit être un entier positif."

# Exemple d'utilisation
print(fibonacci(-10))