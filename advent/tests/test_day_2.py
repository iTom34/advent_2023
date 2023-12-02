import pytest

from advent.day_2 import parser, split_games, parser_set_key_values, possible_game, puzzle_1, minimum_cubes, \
    computer_power, puzzle_2
from importlib_resources import files
from pathlib import Path

import advent.tests.resources.day_2

EXAMPLE = ["Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
           "Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
           "Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
           "Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
           "Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
           "Game 10: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"]

EXAMPLE_PARSED = {1: [{('blue', 3), ('red', 4)},
                      {('blue', 6), ('red', 1), ('green', 2)},
                      {('green', 2)}],
                  2: [{('blue', 1), ('green', 2)},
                      {('red', 1), ('blue', 4), ('green', 3)},
                      {('blue', 1), ('green', 1)}],
                  3: [{('blue', 6), ('red', 20), ('green', 8)},
                      {('blue', 5), ('green', 13), ('red', 4)},
                      {('green', 5), ('red', 1)}],
                  4: [{('blue', 6), ('green', 1), ('red', 3)},
                      {('red', 6), ('green', 3)},
                      {('red', 14), ('blue', 15), ('green', 3)}],
                  5: [{('blue', 1), ('red', 6), ('green', 3)},
                      {('red', 1), ('blue', 2), ('green', 2)}],
                  10: [{('blue', 1), ('red', 6), ('green', 3)},
                       {('red', 1), ('blue', 2), ('green', 2)}]}


@pytest.fixture
def f_example_puzzle_1() -> Path:
    example = files(advent.tests.resources.day_2).joinpath("example_puzzle_1.txt")
    return Path(str(example))


@pytest.fixture
def f_puzzle_1() -> Path:
    example = files(advent.tests.resources.day_2).joinpath("puzzle_1_input.txt")
    return Path(str(example))


def test_parser(f_example_puzzle_1):
    assert parser(f_example_puzzle_1) == EXAMPLE_PARSED


def test_parser_build_games():
    assert split_games(EXAMPLE) == {
        1: "3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green",
        2: "1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue",
        3: "8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red",
        4: "1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red",
        5: "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green",
        10: "6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green"}


@pytest.mark.parametrize("text, expected", [('3 blue,', ('blue', 3)),
                                            (' 4 red;', ('red', 4)),
                                            (' 2 green,', ('green', 2)),
                                            (' 2 green', ('green', 2))])
def test_parser_set_key_values(text: str, expected: int):
    assert parser_set_key_values(text) == expected


@pytest.mark.parametrize("game, expected", [(EXAMPLE_PARSED[1], True),
                                            (EXAMPLE_PARSED[2], True),
                                            (EXAMPLE_PARSED[3], False),
                                            (EXAMPLE_PARSED[4], False),
                                            (EXAMPLE_PARSED[5], True),
                                            (EXAMPLE_PARSED[10], True)])
def test_possible_game(game: list, expected: bool):
    assert possible_game(game) == expected


@pytest.mark.parametrize("fixture_name, expected", [("f_example_puzzle_1", 18),
                                                    ("f_puzzle_1", 2348)])
def test_puzzle_1(fixture_name: str, expected: int, request):
    input_file = request.getfixturevalue(fixture_name)
    assert puzzle_1(input_file) == expected


# ---- Puzzle 2 ----
@pytest.mark.parametrize("sets, expected", [(EXAMPLE_PARSED[1], {'red': 4, 'green': 2, 'blue': 6}),
                                            (EXAMPLE_PARSED[2], {'red': 1, 'green': 3, 'blue': 4}),
                                            (EXAMPLE_PARSED[3], {'red': 20, 'green': 13, 'blue': 6}),
                                            (EXAMPLE_PARSED[4], {'red': 14, 'green': 3, 'blue': 15}),
                                            (EXAMPLE_PARSED[5], {'red': 6, 'green': 3, 'blue': 2})])
def test_minimum_cubes(sets: list, expected: dict):
    assert minimum_cubes(sets) == expected


@pytest.mark.parametrize("minimums, expected", [({'red': 4, 'green': 2, 'blue': 6}, 48),
                                                ({'red': 1, 'green': 3, 'blue': 4}, 12),
                                                ({'red': 20, 'green': 13, 'blue': 6}, 1560),
                                                ({'red': 14, 'green': 3, 'blue': 15}, 630),
                                                ({'red': 6, 'green': 3, 'blue': 2}, 36)])
def test_compute_power(minimums: dict, expected: int):
    assert computer_power(minimums) == expected