import pytest

from advent.day_6 import ACCELERATION_RATE, Race, puzzle_1, puzzle_2


@pytest.fixture
def r1_example() -> Race:
    return Race(7, 9)


@pytest.fixture
def r2_example() -> Race:
    return Race(15, 40)


@pytest.fixture
def r3_example() -> Race:
    return Race(30, 200)


@pytest.fixture
def r1() -> Race:
    return Race(55, 401)


@pytest.fixture
def r2() -> Race:
    return Race(99, 1485)


@pytest.fixture
def r3() -> Race:
    return Race(97, 2274)


@pytest.fixture
def r4() -> Race:
    return Race(93, 1405)


@pytest.fixture
def races_example(r1_example, r2_example, r3_example) -> list[Race]:
    return [r1_example, r2_example, r3_example]


@pytest.fixture
def races(r1, r2, r3, r4) -> list[Race]:
    return [r1, r2, r3, r4]


@pytest.fixture
def f_puzzle_2_example() -> Race:
    return Race(71530, 940200)


@pytest.fixture
def f_puzzle_2() -> Race:
    return Race(55999793, 401148522741405)


@pytest.mark.parametrize("button_pressed_duration, expected", [(0, 0),
                                                               (1, 6),
                                                               (2, 10),
                                                               (3, 12),
                                                               (4, 12),
                                                               (5, 10),
                                                               (6, 6),
                                                               (7, 0),
                                                               (8, 0)])
def test_get_distance_made(r1_example: Race, button_pressed_duration: int, expected: int):
    assert r1_example.get_distance_made(button_pressed_duration) == expected


def test_get_all_distance(r1_example):
    assert r1_example.get_all_distance() == {0: 0,
                                             1: 6,
                                             2: 10,
                                             3: 12,
                                             4: 12,
                                             5: 10,
                                             6: 6,
                                             7: 0}


def test_get_all_beating_records(r1_example):
    assert r1_example.get_all_beating_records() == {2: 10,
                                                    3: 12,
                                                    4: 12,
                                                    5: 10}


@pytest.mark.parametrize("fixture_name, expected", [("r1_example", 4),
                                                    ("r2_example", 8),
                                                    ("r3_example", 9)])
def test_get_number_of_ways_to_beat_record(fixture_name: str, expected: int, request):
    race = request.getfixturevalue(fixture_name)
    assert race.get_number_of_ways_to_beat_record() == expected


@pytest.mark.parametrize("fixture_name, expected", [("races_example", 288),
                                                    ("races", 2374848)])
def test_puzzle_1(fixture_name: str, expected: int, request):
    races = request.getfixturevalue(fixture_name)
    assert puzzle_1(races) == expected


@pytest.mark.parametrize("fixture_name, expected", [("f_puzzle_2_example", 71503),
                                                    ("f_puzzle_2", 39132886)])
def test_puzzle_2(fixture_name: str, expected: int, request):
    races = request.getfixturevalue(fixture_name)
    assert puzzle_2(races) == expected
