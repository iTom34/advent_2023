import pytest
from pathlib import Path
from importlib_resources import files

from advent.day_3 import import_puzzle, find_numbers, has_adjacent_symbol, Number, DigitCoordinates

import advent.tests.resources.day_3

EXAMPLE_PUZZLE_PARSED = ["467..114..",
                         "...*......",
                         "..35..633.",
                         "......#...",
                         "617*......",
                         ".....+.58.",
                         "..592.....",
                         "......755.",
                         "...$.*....",
                         ".664.598.."]

number_467 = Number(value=467,
                    digit_coordinates=frozenset([DigitCoordinates(0, 0),
                                                 DigitCoordinates(0, 1),
                                                 DigitCoordinates(0, 2)]))

number_114 = Number(value=114,
                    digit_coordinates=frozenset([DigitCoordinates(0, 5),
                                                 DigitCoordinates(0, 6),
                                                 DigitCoordinates(0, 7)]))

number_35 = Number(value=35,
                   digit_coordinates=frozenset([DigitCoordinates(2, 2),
                                                DigitCoordinates(2, 3)]))

number_633 = Number(value=633,
                    digit_coordinates=frozenset([DigitCoordinates(2, 6),
                                                 DigitCoordinates(2, 7),
                                                 DigitCoordinates(2, 8)]))

number_617 = Number(value=617,
                    digit_coordinates=frozenset([DigitCoordinates(4, 0),
                                                 DigitCoordinates(4, 1),
                                                 DigitCoordinates(4, 2)]))

number_58 = Number(value=58,
                   digit_coordinates=frozenset([DigitCoordinates(5, 7),
                                                DigitCoordinates(5, 8)]))

number_592 = Number(value=592,
                    digit_coordinates=frozenset([DigitCoordinates(6, 2),
                                                 DigitCoordinates(6, 3),
                                                 DigitCoordinates(6, 4)]))

number_755 = Number(value=755,
                    digit_coordinates=frozenset([DigitCoordinates(7, 6),
                                                 DigitCoordinates(7, 7),
                                                 DigitCoordinates(7, 8)]))

number_644 = Number(value=644,
                    digit_coordinates=frozenset([DigitCoordinates(9, 1),
                                                 DigitCoordinates(9, 2),
                                                 DigitCoordinates(9, 3)]))

number_598 = Number(value=598,
                    digit_coordinates=frozenset([DigitCoordinates(9, 5),
                                                 DigitCoordinates(9, 6),
                                                 DigitCoordinates(9, 7)]))

NUMBERS_IN_PUZZLE = [number_467,
                     number_114,
                     number_35,
                     number_633,
                     number_617,
                     number_58,
                     number_592,
                     number_755,
                     number_644,
                     number_598]


@pytest.fixture
def f_example_puzzle() -> Path:
    example = files(advent.tests.resources.day_3).joinpath("example_puzzle.txt")
    return Path(str(example))


class TestDigitCoordinate:
    def test_equal(self):
        assert DigitCoordinates(1, 2) == DigitCoordinates(1, 2)

    def test_not_equal(self):
        assert DigitCoordinates(1, 2) != DigitCoordinates(2, 1)


class TestNumber:
    def test_equal(self):
        number_1 = Number(1, frozenset([DigitCoordinates(1, 2)]))
        number_2 = Number(1, frozenset([DigitCoordinates(1, 2)]))

        assert number_1 == number_2

    def test_not_equal(self):
        number_1 = Number(1, frozenset([DigitCoordinates(1, 2)]))
        number_2 = Number(1, frozenset([DigitCoordinates(1, 1)]))

        assert number_1 != number_2


def test_import_file(f_example_puzzle):
    assert import_puzzle(f_example_puzzle) == EXAMPLE_PUZZLE_PARSED


def test_find_numbers():
    assert find_numbers(EXAMPLE_PUZZLE_PARSED) == NUMBERS_IN_PUZZLE
