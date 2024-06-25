import random
from typing import List, Tuple

COULEURS_VALIDES = ['R', 'J', 'V', 'B', 'N', 'D']

def generer_code_couleurs() -> List[str]:
    """
    Génère un code secret de 4 couleurs parmi les couleurs valides.
    
    Returns:
    List[str]: Une liste de 4 couleurs aléatoires.
    """
    return [random.choice(COULEURS_VALIDES) for _ in range(4)]

def verifier_proposition(code_secret: List[str], proposition: List[str]) -> Tuple[int, int]:
    """
    Vérifie la proposition du joueur par rapport au code secret.
    
    Args:
    code_secret (List[str]): Le code secret généré.
    proposition (List[str]): La proposition du joueur.
    
    Returns:
    Tuple[int, int]: (nombre de pions bien placés, nombre de pions de bonne couleur mais mal placés)
    """
    bien_places = sum(1 for i in range(len(proposition)) if proposition[i] == code_secret[i])
    
    # Compter les occurrences de chaque couleur dans le code secret et la proposition
    code_count = {couleur: code_secret.count(couleur) for couleur in COULEURS_VALIDES}
    proposition_count = {couleur: proposition.count(couleur) for couleur in COULEURS_VALIDES}
    
    mal_places = sum(min(code_count[couleur], proposition_count[couleur]) for couleur in COULEURS_VALIDES)
    
    # Enlever les bien placés des mal placés
    mal_places -= bien_places

    return bien_places, mal_places

def demander_proposition() -> List[str]:
    """
    Demande une proposition au joueur.
    
    Returns:
    List[str]: La proposition du joueur sous forme de liste de couleurs.
    """
    while True:
        proposition = input("Entrez une combinaison de couleurs (R J V B N D) avec un espace entre chaque : ").strip().upper().split()
        if len(proposition) == 4 and all(c in COULEURS_VALIDES for c in proposition):
            return proposition
        else:
            print("Entrée invalide. Assurez-vous d'entrer exactement 4 couleurs parmi R, J, V, B, N, D.")

def jouer() -> None:
    """
    Lance le jeu de Mastermind.
    """
    code_secret = generer_code_couleurs()
    essais = 12
    print("Bienvenue au Mastermind ! Vous avez 12 essais pour deviner le code secret.")

    for essai in range(1, essais + 1):
        print(f"Essai {essai} sur {essais}")
        proposition = demander_proposition()
        bien_places, mal_places = verifier_proposition(code_secret, proposition)
        
        if bien_places == 4:
            print("Félicitations ! Vous avez deviné le code secret :", " ".join(code_secret))
            return

        print(f"{bien_places} pions de bonne couleur à la bonne place")
        print(f"{mal_places} pions de bonne couleur")
        
    print("Dommage, vous avez épuisé tous vos essais. Le code secret était :", " ".join(code_secret))

def jouer_nouveau() -> None:
    """
    Fonction pour lancer une nouvelle partie ou quitter le jeu.
    """
    while True:
        jouer()
        rejouer = input("Voulez-vous jouer une nouvelle partie ? (O/N) : ").strip().upper()
        if rejouer != 'O':
            print("Merci d'avoir joué !")
            break

if __name__ == "__main__":
    jouer_nouveau()
