def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(row))

def move_player(maze, player_pos, move):
    x, y = player_pos
    if move == 'up':
        x -= 1
    elif move == 'down':
        x += 1
    elif move == 'left':
        y -= 1
    elif move == 'right':
        y += 1
    
    if 0 <= x < len(maze) and 0 <= y < len(maze[0]):
        if maze[x][y] != '#':
            player_pos = (x, y)
            if maze[x][y] == 'E': 
                print("Félicitations, vous avez atteint la sortie !")
    return player_pos

def main():
    maze = load_maze('maze.txt')
    player_pos = (1, 1) 
    
    while True:
        display_maze(maze)
        print("Déplacer le joueur avec 'up', 'down', 'left', 'right'")
        move = input("Entrez le déplacement: ")
        player_pos = move_player(maze, player_pos, move)
        

        if maze[player_pos[0]][player_pos[1]] == 'E':
            break 

if __name__ == "__main__":
    main()