class Kind:
    NORMAL = 0
    START = 1
    END = 2


class Directions:
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3


class Exit:
    opposite = 0
    dx = 0
    dy = 0
    symbol = ""

    def __init__(self, opposite, dx, dy, symbol):
        self.opposite = opposite
        self.dx = dx
        self.dy = dy
        self.symbol = symbol


ALL_EXITS = {
    Directions.NORTH: Exit(Directions.SOUTH, 0, -1, "N"),
    Directions.EAST:  Exit(Directions.WEST, 1, 0, "E"),
    Directions.SOUTH: Exit(Directions.NORTH, 0, 1, "S"),
    Directions.WEST:  Exit(Directions.EAST, -1, 0, "W")
}


def remaining_exits(room_exits):
    return list(set(ALL_EXITS) - set(room_exits))


def opposite_exit(room_exit):
    return ALL_EXITS[room_exit].opposite


def symbol_from(x, y):
    return (x * 1000) + y


class Room:
    x = 0
    y = 0
    kind = Kind.NORMAL
    exits = []

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind

    def symbol(self):
        return symbol_from(self.x, self.y)

    def __contains_exit(self, room_exit):
        return self.exits.__contains__(room_exit)

    def __print_exits(self):
        n = "N" if self.__contains_exit(Directions.NORTH) else " "
        e = "E" if self.__contains_exit(Directions.EAST) else " "
        s = "S" if self.__contains_exit(Directions.SOUTH) else " "
        w = "W" if self.__contains_exit(Directions.WEST) else " "

        return f"{n}{e}{s}{w}"

    def __print_kind_name(self):
        kind_name = ""

        if self.kind == Kind.NORMAL:
            kind_name = "NORMAL"

        if self.kind == Kind.START:
            kind_name = "START"

        if self.kind == Kind.END:
            kind_name = "END"

        return kind_name

    def __get_info(self):
        str_exits = self.__print_exits()
        str_kind = self.__print_kind_name()
        return str_exits, str_kind

    def __str__(self):
        str_exits, str_kind = self.__get_info()
        return f"[{self.symbol():6}][{str_exits}][{str_kind:6}]"

    def __repr__(self):
        str_exits, str_kind = self.__get_info()
        return f"[{self.symbol():6}][{str_exits}][{str_kind:6}]"
