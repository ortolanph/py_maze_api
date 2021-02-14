from random import randint, shuffle
from room import Kind, Room, ALL_EXITS, remaining_exits, opposite_exit, symbol_from


class Maze:
    __maze = dict()
    __width = 0
    __height = 0
    __rooms = 1

    def __init__(self, width, height):
        self.__width = width
        self.__height = height

    def __room_count(self):
        if self.__rooms == 1:
            return Kind.START

        if self.__rooms == self.__width * self.__height:
            return Kind.END

        return Kind.NORMAL

    def __available_exits(self, x, y):
        possible_exits = []

        for possible_exit in ALL_EXITS:
            nx = x + ALL_EXITS[possible_exit].dx
            ny = y + ALL_EXITS[possible_exit].dy

            if nx == 0 or nx > self.__width:
                continue

            if ny == 0 or ny > self.__height:
                continue

            dir_symbol = symbol_from(nx, ny)

            if dir_symbol not in self.__maze:
                possible_exits.append(possible_exit)

        return possible_exits

    def __dead_end(self, x, y):
        return True if len(self.__available_exits(x, y)) == 0 else False

    def __walk(self, x, y):
        my_exit = -1
        opposite = -1
        while not self.__dead_end(x, y):
            kind = self.__room_count()
            room = Room(x, y, kind)
            room.exits = []

            if opposite > -1:
                room.exits.append(opposite)

            possible_exits = self.__available_exits(x, y)

            if my_exit > -1:
                possible_exits = list(set(possible_exits) - {opposite_exit(my_exit)})

            shuffle(possible_exits)
            my_exit = possible_exits[0]
            room.exits.append(my_exit)
            self.__maze[room.symbol()] = room
            self.__rooms += 1

            opposite = opposite_exit(my_exit)
            x = x + ALL_EXITS[my_exit].dx
            y = y + ALL_EXITS[my_exit].dy
        else:
            kind = self.__room_count()
            room = Room(x, y, kind)
            # TODO: what if it's a dead end room?
            room.exits.append(opposite)
            self.__maze[room.symbol()] = room
            self.__rooms += 1

    def __hunt(self):
        for y in range(1, self.__height + 1):
            for x in range(1, self.__width + 1):
                index = symbol_from(x, y)
                available = self.__available_exits(x, y)
                if index not in self.__maze and len(available) > 0:
                    self.__walk(x, y)

    def create_maze(self):
        initial_x = randint(1, self.__width)
        initial_y = randint(1, self.__height)

        self.__walk(initial_x, initial_y)
        # TODO: delete the line below after problems solved
        self.print_maze()
        self.__hunt()

    def start_room(self):
        return next(filter(lambda room: room.kind == Kind.START, self.__maze.values()))

    def room_at(self, x, y):
        symbol = symbol_from(x, y)
        return self.__maze[symbol]

    def print_maze(self):
        for y in range(1, self.__height + 1):
            line = ""
            for x in range(1, self.__width + 1):
                index = symbol_from(x, y)
                if index in self.__maze:
                    room = self.__maze[index]
                    line += room.__repr__()
                else:
                    line += f"[{index:6}]              "
            print(line)
