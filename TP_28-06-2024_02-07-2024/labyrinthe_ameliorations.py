""" Labyrinthe """
# pas terminé ni documenté dans le rapport
class MazeLoadError(Exception):
    """Exception levée lorsque le chargement du labyrinth échoue."""

def load_maze(file_path):
    """
    Initialisation du larbyrinth

    Paramètres :
    file_path (str): Chemin du template du labyrinth.

    Retourne :
    list: Labyrinth
    """
    try:
        with open(file_path, 'r', encoding="utf-8") as file:
            maze = [list(line.strip()) for line in file.readlines()]
        return maze
    except Exception as load_exception:
        raise MazeLoadError(f"Erreur lors de l\'import du labyrinthe : {str(load_exception)}") from load_exception

def display_maze(maze):
    """
    Affichage du larbyrinth

    Paramètres :
    maze (list): Labyrinth

    Retourne :
    list: Labyrinth
    """
    for row in maze:
        print(''.join(row))

def move_player(maze, player_pos, move):
    """
    Déplace le joueur

    Paramètres :
    maze (list): Labyrinth
    player_pos (int, int) : position actuel du joueur
    move (enum: up, down, left, right) : direction 

    Retourne :
    player_pos: (int, int) nouvelle position du joueur
    """
    x, y = player_pos
    if move == 'up':
        x -= 1
    elif move == 'down':
        x += 1
    elif move == 'left':
        y -= 1
    elif move == 'right':
        y += 1

    # Vérifier les limites du labyrinthe
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        if maze[x][y] != '#':  # Vérifier si c'est un mur
            player_pos = (x, y)
            if maze[x][y] == 'E':  # Vérifier si le joueur atteint la sortie
                print("Félicitations, vous avez atteint la sortie !")
    return player_pos

def main():
    """
    Fonction principale du jeu
    """
    maze = load_maze('maze.txt')
    player_pos = (1, 1)  # Position initiale du joueur

    while True:
        display_maze(maze)
        print("Déplacer le joueur avec 'up', 'down', 'left', 'right'")
        move = input("Entrez le déplacement: ")
        player_pos = move_player(maze, player_pos, move)

        # Ajouter un solveur de chemin pour trouver le chemin de 'S' à 'E'

        if maze[player_pos[0]][player_pos[1]] == 'E':
            break  # Sortir de la boucle si le joueur atteint la sortie

if __name__ == "__main__":
    main()
