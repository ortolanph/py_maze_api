from random import randint, shuffle
from room import KIND, Room, ALL_EXITS, opposite_exit, symbol_from


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
            return KIND["START"]

        if self.__rooms == self.__width * self.__height:
            return KIND["END"]

        return KIND["NORMAL"]

    def __possible_links(self, x, y):
        possible_links = []

        for possible_link in ALL_EXITS:
            nx = x + ALL_EXITS[possible_link].dx
            ny = y + ALL_EXITS[possible_link].dy

            if nx == 0 or nx > self.__width:
                continue

            if ny == 0 or ny > self.__height:
                continue

            dir_symbol = symbol_from(nx, ny)

            if dir_symbol in self.__maze:
                possible_links.append(possible_link)

        return possible_links

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
        opposite = -1
        while not self.__dead_end(x, y):
            exits = self.__available_exits(x, y)
            shuffle(exits)
            my_exit = exits[0]

            room = Room(x, y, self.__room_count())
            room.exits.append(my_exit)

            if opposite > 0:
                room.exits.append(opposite)

            self.__maze[room.symbol()] = room
            self.__rooms += 1

            opposite = opposite_exit(my_exit)
            x += ALL_EXITS[my_exit].dx
            y += ALL_EXITS[my_exit].dy
        else:
            room = Room(x, y, self.__room_count())
            room.exits.append(opposite)
            self.__maze[room.symbol()] = room
            self.__rooms += 1

    def __hunt(self):
        for y in range(1, self.__height + 1):
            for x in range(1, self.__width + 1):
                symbol = symbol_from(x, y)
                links = self.__possible_links(x, y)
                if symbol not in self.__maze and len(links) > 0:
                    room = Room(x, y, self.__room_count())
                    shuffle(links)
                    link = links[0]
                    room.exits.append(link)
                    self.__maze[room.symbol()] = room
                    self.__rooms += 1

                    opposite = opposite_exit(link)
                    another_symbol = symbol_from(x + ALL_EXITS[link].dx, y + ALL_EXITS[link].dy)
                    another_room = self.__maze[another_symbol]
                    another_room.exits.append(opposite)
                    self.__maze[another_symbol] = another_room

    def create_maze(self):
        initial_x = randint(1, self.__width)
        initial_y = randint(1, self.__height)

        self.__walk(initial_x, initial_y)
        while self.__rooms < (self.__width * self.__height):
            self.__hunt()

    def start_room(self):
        return [room for room in self.__maze.values() if room.kind == KIND["START"]][0]

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
