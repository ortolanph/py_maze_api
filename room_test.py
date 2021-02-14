from room import Room, Kind, Directions, opposite_exit, remaining_exits, symbol_from


def test_symbol():
    room = Room(2, 2, Kind.NORMAL)

    actual = room.symbol()
    expected = 2002

    assert actual == expected


def test_normal_room():
    room = Room(2, 2, Kind.NORMAL)

    actual = room.kind
    expected = Kind.NORMAL

    assert actual == expected


def test_start_room():
    room = Room(2, 2, Kind.START)

    actual = room.kind
    expected = Kind.START

    assert actual == expected


def test_end_room():
    room = Room(2, 2, Kind.END)

    actual = room.kind
    expected = Kind.END

    assert actual == expected


def test_opposite_exit():
    my_exit = Directions.EAST

    actual = opposite_exit(my_exit)
    expected = Directions.WEST

    assert actual == expected


def test_remaining_exits():
    my_exits = [Directions.EAST, Directions.SOUTH]

    actual = remaining_exits(my_exits)
    expected = [Directions.NORTH, Directions.WEST]

    assert actual == expected


def test_symbol_from():
    x = 5
    y = 5

    actual = symbol_from(x, y)
    expected = 5005

    assert actual == expected
