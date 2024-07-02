def load_maze(file_path):
    with open(file_path, 'r') as file:
        maze = [list(line.strip()) for line in file.readlines()]
    return maze

def display_maze(maze):
    for row in maze:
        print(''.join(row))

maze = load_maze('maze.txt')
display_maze(maze)
