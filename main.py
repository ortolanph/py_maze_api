from maze import Maze

if __name__ == '__main__':
    my_maze = Maze(5, 5)
    my_maze.create_maze()
    my_maze.print_maze()
    print(my_maze.start_room())
