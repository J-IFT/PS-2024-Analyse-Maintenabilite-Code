import random

def system_state(a, b):
    """
    Détermine l'état du système en fonction des valeurs de a et b.

    Args:
    - a (int): Valeur de la première variable.
    - b (int): Valeur de la deuxième variable.

    Returns:
    - str: "ouvert" si le système est ouvert, "fermé" sinon.

    Raises:
    - ValueError: Si les valeurs de a ou b ne sont pas des entiers.
    """
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError("Les valeurs de a et b doivent être des entiers.")

    if random.random() > 0.5:
        if a > 10 and b < 5:
            return "ouvert"
        else:
            return "fermé"
    else:
        return "ouvert"

if __name__ == "__main__":
    try:
        a = int(input("Entrez la valeur de a : "))
        b = int(input("Entrez la valeur de b : "))

        result = system_state(a, b)
        print(f"Le système est {result}")

    except ValueError as ve:
        print(f"Erreur : {ve}")
