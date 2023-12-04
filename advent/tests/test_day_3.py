import pytest
from pathlib import Path
from importlib_resources import files
from mock import Mock

from advent.day_3 import (import_puzzle,
                          find_numbers,
                          car_has_adjacent_symbol,
                          Number,
                          DigitCoordinates,
                          number_has_adjacent_symbol,
                          puzzle_1,
                          Star,
                          find_starts,
                          puzzle_2)

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


@pytest.fixture
def f_puzzle() -> Path:
    example = files(advent.tests.resources.day_3).joinpath("puzzle.txt")
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


@pytest.mark.skip
def test_find_numbers():
    assert find_numbers(EXAMPLE_PUZZLE_PARSED) == NUMBERS_IN_PUZZLE


@pytest.mark.parametrize("coordinates, expected", [(DigitCoordinates(0, 0), False),
                                                   (DigitCoordinates(0, 9), False),
                                                   (DigitCoordinates(9, 0), False),
                                                   (DigitCoordinates(9, 9), False),
                                                   (DigitCoordinates(3, 1), False),
                                                   (DigitCoordinates(4, 2), True),
                                                   (DigitCoordinates(3, 2), True),
                                                   (DigitCoordinates(3, 3), True),
                                                   (DigitCoordinates(3, 4), True),
                                                   (DigitCoordinates(4, 4), True),
                                                   (DigitCoordinates(5, 4), True),
                                                   (DigitCoordinates(5, 3), True),
                                                   (DigitCoordinates(5, 2), True),])
def test_car_has_adjacent_symbol(coordinates: DigitCoordinates, expected):
    assert car_has_adjacent_symbol(EXAMPLE_PUZZLE_PARSED, coordinates) == expected


@pytest.mark.parametrize("number, expected", [(number_467, True),
                                              (number_114, False),
                                              (number_35, True),
                                              (number_633, True),
                                              (number_617, True),
                                              (number_58, False),
                                              (number_592, True),
                                              (number_755, True),
                                              (number_644, True),
                                              (number_598, True)])
def test_number_has_adjacent_symbol(number: Number, expected: bool):
    assert number_has_adjacent_symbol(EXAMPLE_PUZZLE_PARSED, number) == expected


@pytest.mark.parametrize("fixture_name, expected", [("f_example_puzzle", 4361),
                                                    ("f_puzzle", 530495)])
def test_puzzle_1(fixture_name, expected, request):
    input_puzzle = request.getfixturevalue(fixture_name)
    assert puzzle_1(input_puzzle) == expected


# --- Puzzle 2 ---
def test_find_starts():
    assert find_starts(EXAMPLE_PUZZLE_PARSED) == [Star(1, 3),
                                                  Star(4, 3),
                                                  Star(8, 5)]


def test_stars_equality():
    assert Star(1, 2) == Star(1, 2)
    assert Star(1, 2) != Star(2, 1)


LIST_OF_NUMBERS = [Number(1, frozenset([DigitCoordinates(0, 0)])),
                   Number(2, frozenset([DigitCoordinates(0, 1)])),
                   Number(3, frozenset([DigitCoordinates(0, 2)])),
                   Number(4, frozenset([DigitCoordinates(1, 2)])),
                   Number(5, frozenset([DigitCoordinates(2, 2)])),
                   Number(6, frozenset([DigitCoordinates(2, 1)])),
                   Number(7, frozenset([DigitCoordinates(2, 0)])),
                   Number(8, frozenset([DigitCoordinates(1, 0)]))]


@pytest.mark.parametrize("star, expected", [(Star(1, 1), LIST_OF_NUMBERS),
                                            (Star(1, 4), [])])
def test_find_adjacent_numbers(star: Star, expected: list[Number]):
    assert star._find_adjacent_numbers(LIST_OF_NUMBERS) == expected


@pytest.mark.parametrize("numbers, expected", [([], 0),
                                                ([Number(2, None)], 0),
                                                ([Number(2, None),
                                                  Number(3, None)], 6),
                                                ([Number(2, None),
                                                  Number(3, None),
                                                  Number(4, None)], 0)])
def test_compute_gear_ratio(numbers, expected):
    star = Star(1, 1)
    star._find_adjacent_numbers = Mock(return_value=numbers)
    assert star.compute_gear_ratio(numbers) == expected
    star._find_adjacent_numbers.assert_called_once_with(numbers)


@pytest.mark.parametrize("fixture_name, expected", [("f_example_puzzle", 467835),
                                                    ("f_puzzle", 80253814)])
def test_puzzle_2(fixture_name, expected, request):
    input_puzzle = request.getfixturevalue(fixture_name)
    assert puzzle_2(input_puzzle) == expected
