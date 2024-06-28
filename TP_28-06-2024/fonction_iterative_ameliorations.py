"""Module : Fibonacci """

def fibonacci_iteratif(nombre: int) -> int:
    
    """
    Calcule le n-ième nombre de Fibonacci de manière itérative.

    Paramètre:
    nombre (int): L'indice du nombre de Fibonacci à calculer. Doit être un entier positif.

    Retourne:
    int: Le n-ième nombre de Fibonacci si l'entrée est valide.
    str: Un message d'erreur si l'entrée est invalide.
    """
    try:      
         # Vérification si nombre est un entier positif
        if not isinstance(nombre, int) or nombre <= 0:
            raise TypeError("Entrée invalide, nombre doit être un entier positif.")
        
        # Cas particuliers pour les premières valeurs de Fibonacci
        if nombre == 1:
            return 0
        elif nombre == 2:
            return 1

        # Initialisation des deux premiers nombres de Fibonacci
        a, b = 0, 1

        # Boucle pour calculer les nombres de Fibonacci jusqu'à la valeur désirée
        for _ in range(2, nombre):
            a, b = b, a + b  # Mettre à jour a et b pour obtenir le prochain nombre de Fibonacci

        return b

    except TypeError:
        return "Erreur : Le paramètre 'nombre' doit être un entier positif."


# Exemple d'utilisation pour tester la fonction
print(fibonacci_iteratif(10))  # Devrait afficher 34, le 10ème nombre de Fibonacci

