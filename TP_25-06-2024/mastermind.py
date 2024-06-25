import random

def generer_code_couleurs():
    """
    Génère un code secret de 4 couleurs parmi R, J, V, B, N, D (Rouge, Jaune, Vert, Bleu, Noir, Doré).
    
    Returns:
    list: Une liste de 4 couleurs aléatoires.
    """
    couleurs = ['R', 'J', 'V', 'B', 'N', 'D']
    return [random.choice(couleurs) for _ in range(4)]

def verifier_proposition(code_secret, proposition):
    """
    Vérifie la proposition du joueur par rapport au code secret.
    
    Args:
    code_secret (list): Le code secret généré.
    proposition (list): La proposition du joueur.
    
    Returns:
    tuple: (nombre de pions bien placés, nombre de pions de bonne couleur mais mal placés)
    """
    bien_places = 0
    mal_places = 0
    code_temp = code_secret.copy()
    proposition_temp = proposition.copy()

    # Vérification des bien placés
    for i in range(len(proposition)):
        if proposition[i] == code_temp[i]:
            bien_places += 1
            code_temp[i] = proposition_temp[i] = None

    # Vérification des mal placés
    for i in range(len(proposition_temp)):
        if proposition_temp[i] and proposition_temp[i] in code_temp:
            mal_places += 1
            code_temp[code_temp.index(proposition_temp[i])] = None

    return bien_places, mal_places

def demander_proposition():
    """
    Demande une proposition au joueur.
    
    Returns:
    list: La proposition du joueur sous forme de liste de couleurs.
    """
    while True:
        proposition = input("Entrez une combinaison de couleurs (R J V B N D) avec un espace entre chaque : ").strip().upper().split()
        if len(proposition) == 4 and all(c in ['R', 'J', 'V', 'B', 'N', 'D'] for c in proposition):
            return proposition
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement 4 couleurs parmi R, J, V, B, N, D.")

def jouer():
    """
    Lance le jeu de Mastermind.
    """
    code_secret = generer_code_couleurs()
    essais = 12
    print("Bienvenue au Mastermind ! Vous avez 12 essais pour deviner le code secret.")

    while essais > 0:
        print(f"Essai {13 - essais} sur 12")
        proposition = demander_proposition()
        bien_places, mal_places = verifier_proposition(code_secret, proposition)
        
        if bien_places == 4:
            print("Félicitations ! Vous avez deviné le code secret :", " ".join(code_secret))
            return

        print(f"{bien_places} pions de bonne couleur à la bonne place")
        print(f"{mal_places} pions de bonne couleur")
        essais -= 1

    print("Dommage, vous avez épuisé tous vos essais. Le code secret était :", " ".join(code_secret))

if __name__ == "__main__":
    jouer()
