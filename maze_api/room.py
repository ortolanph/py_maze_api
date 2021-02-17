KIND = {
    "NORMAL": 1,
    "START": 2,
    "END": 3
}


DIRECTIONS = {
    "NORTH": 1,
    "EAST": 2,
    "SOUTH": 3,
    "WEST": 4
}


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
    DIRECTIONS["NORTH"]: Exit(DIRECTIONS["SOUTH"], 0, -1, "N"),
    DIRECTIONS["EAST"]:  Exit(DIRECTIONS["WEST"], 1, 0, "E"),
    DIRECTIONS["SOUTH"]: Exit(DIRECTIONS["NORTH"], 0, 1, "S"),
    DIRECTIONS["WEST"]:  Exit(DIRECTIONS["EAST"], -1, 0, "W")
}


def opposite_exit(room_exit):
    return ALL_EXITS[room_exit].opposite


def symbol_from(x, y):
    return (x * 1000) + y


class Room:
    x = 0
    y = 0
    kind = KIND["NORMAL"]
    exits = []

    def __init__(self, x, y, kind):
        self.x = x
        self.y = y
        self.kind = kind
        self.exits = []

    def symbol(self):
        return symbol_from(self.x, self.y)

    def __contains_exit(self, room_exit):
        return self.exits.__contains__(room_exit)

    def __print_exits(self):
        n = "N" if self.__contains_exit(DIRECTIONS["NORTH"]) else " "
        e = "E" if self.__contains_exit(DIRECTIONS["EAST"]) else " "
        s = "S" if self.__contains_exit(DIRECTIONS["SOUTH"]) else " "
        w = "W" if self.__contains_exit(DIRECTIONS["WEST"]) else " "

        return f"{n}{e}{s}{w}"

    def __print_kind_name(self):
        kind_name = ""

        if self.kind == KIND["NORMAL"]:
            kind_name = "NORMAL"

        if self.kind == KIND["START"]:
            kind_name = "START"

        if self.kind == KIND["END"]:
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
