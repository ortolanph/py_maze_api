from maze_api.room import Room, KIND, DIRECTIONS, opposite_exit, symbol_from


def test_symbol():
    room = Room(2, 2, KIND["NORMAL"])

    actual = room.symbol()
    expected = 2002

    assert actual == expected


def test_normal_room():
    room = Room(2, 2, KIND["NORMAL"])

    actual = room.kind
    expected = KIND["NORMAL"]

    assert actual == expected


def test_start_room():
    room = Room(2, 2, KIND["START"])

    actual = room.kind
    expected = KIND["START"]

    assert actual == expected


def test_end_room():
    room = Room(2, 2, KIND["END"])

    actual = room.kind
    expected = KIND["END"]

    assert actual == expected


def test_opposite_exit():
    my_exit = DIRECTIONS["EAST"]

    actual = opposite_exit(my_exit)
    expected = DIRECTIONS["WEST"]

    assert actual == expected


def test_symbol_from():
    x = 5
    y = 5

    actual = symbol_from(x, y)
    expected = 5005

    assert actual == expected
