import pytest
from importlib_resources import files
from pathlib import Path

from advent.day_1 import find_last_and_first_digit, puzzle_1, find_start_spelled_number, find_first_and_last_digit_puzzle_2, puzzle_2

import advent.tests.resources.day_1.puzzle_1
import advent.tests.resources.day_1.puzzle_2


@pytest.fixture
def example_puzzle_1() -> Path:
    example = files(advent.tests.resources.day_1.puzzle_1).joinpath("example.txt")
    return Path(str(example))


@pytest.fixture
def example_puzzle_2() -> Path:
    example = files(advent.tests.resources.day_1.puzzle_2).joinpath("example.txt")
    return Path(str(example))


def test_puzzle_1(example_puzzle_1):
    assert puzzle_1(example_puzzle_1) == 142


@pytest.mark.parametrize("input, expected",
                         [("1abc2", 12),
                          ("pqr3stu8vwx", 38),
                          ("a1b2c3d4e5f", 15),
                          ("treb7uchet", 77)])
def test_find_last_and_first_digit(input: str, expected: int):
    assert find_last_and_first_digit(input) == expected


@pytest.mark.parametrize("input, expected",
                         [("two1nine", 2),
                          ("qmsdlfkjqsdmlngbqlsk", None),
                          ("wo1nineqdsflkj2", None),
                          ("2eightwothree", None),
                          ("qsdmflkjaeightwothree", None),
                          ("oneqsdmflkjaonetwothree", 1),
                          ("twoqsdmflkjatwotwothree", 2),
                          ("threeqsdmflkjathreetwothree", 3),
                          ("fourqsdmflkjafourtwothree", 4),
                          ("fiveqsdmflkjafivetwothree", 5),
                          ("sixqsdmflkjasixtwothree", 6),
                          ("sevenqsdmflkjaseventwothree", 7),
                          ("eightqsdmflkjaeightwothree", 8),
                          ("nineqsdmflkjaninetwothree", 9)])
def test_find_start_spelled_number(input, expected):
    assert find_start_spelled_number(input) == expected


@pytest.mark.parametrize("input, expected",
                         [("two1nine", 29),
                          ("eightwothree", 83),
                          ("abcone2threexyz", 13),
                          ("xtwone3four", 24),
                          ("4nineeightseven2", 42),
                          ("zoneight234", 14),
                          ("7pqrstsixteen", 76),
                          ("4d", 44),
                          ("k3", 33),
                          ("37three5btqxsqkszchfivebvbbddssvc", 35),
                          ("onetwothree", 13),
                          ("jjhxddmg5mqxqbgfivextlcpnvtwothreetwonerzk", 51),
                          ("nfsssvfzfive9seveneightfour5sevenpstctrnkmj", 57),
                          ("8cttggeightsix54czlc2nine", 89),
                          ("cgvvsl44five5ztlfdrc", 45),
                          ("6lqjrhbnxxcqlpnmjsthreesixxsxcgqsxmdx7", 67)])
def test_find_first_and_last_digits_puzzle_2(input, expected):
    assert find_first_and_last_digit_puzzle_2(input) == expected


def test_puzzle_2(example_puzzle_2):
    assert puzzle_2(example_puzzle_2) == 281
