import pytest
from mock import Mock
from pathlib import Path
from importlib_resources import files

import advent.tests.resources.day_4
from advent.day_4 import import_puzzle, Card, puzzle_1

CARD_1 = Card(1, [59, 65, 20, 66, 55, 92, 43, 23, 98, 70], [99, 81, 56, 30, 88, 55, 57, 11, 90, 45, 53, 28, 33, 20, 84, 54, 24, 64, 74, 98, 36, 77, 61, 82, 69])
CARD_20 = Card(20, [62, 76, 53, 69, 70, 72, 81, 1, 67, 78], [62, 24, 60, 72, 67, 76, 25, 46, 40, 26, 28, 57, 69, 70, 78, 79, 81, 1, 11, 15, 30, 63, 68, 37, 53])
CARD_300 = Card(300, [87, 81, 7, 92, 88, 66, 58, 22, 13, 59], [42, 18, 31, 11, 17, 62, 46, 52, 22, 48, 83, 99, 93, 2, 26, 28, 88, 4, 56, 20, 25, 43, 82, 89, 44])


@pytest.fixture
def f_example_puzzle() -> Path:
    example = files(advent.tests.resources.day_4).joinpath("example.txt")
    return Path(str(example))


@pytest.fixture
def f_puzzle() -> Path:
    example = files(advent.tests.resources.day_4).joinpath("puzzle.txt")
    return Path(str(example))


@pytest.fixture
def card_1() -> Card:
    return Card(1, [59, 65, 20, 66, 55, 92, 43, 23, 98, 70], [99, 81, 56, 30, 88, 55, 57, 11, 90, 45, 53, 28, 33, 20, 84, 54, 24, 64, 74, 98, 36, 77, 61, 82, 69])


@pytest.fixture
def card_20() -> Card:
    return Card(20, [62, 76, 53, 69, 70, 72, 81, 1, 67, 78], [62, 24, 60, 72, 67, 76, 25, 46, 40, 26, 28, 57, 69, 70, 78, 79, 81, 1, 11, 15, 30, 63, 68, 37, 53])


@pytest.fixture
def card_300() -> Card:
    return Card(300, [87, 81, 7, 92, 88, 66, 58, 22, 13, 59], [42, 18, 31, 11, 17, 62, 46, 52, 22, 48, 83, 99, 93, 2, 26, 28, 88, 4, 56, 20, 25, 43, 82, 89, 44])


class TestCard:
    def test_equality(self):
        assert Card(1, [1], [3]) == Card(1, [1], [3])
        assert Card(1, [1], [3]) != Card(1, [1], [2])

    @pytest.mark.parametrize("card_name, expected", [('card_1', 3),
                                                     ('card_20', 10),
                                                     ('card_300', 2)])
    def test_number_of_match(self, card_name, expected, request):
        card: Card = request.getfixturevalue(card_name)
        assert card.number_of_match() == expected

    @pytest.mark.parametrize("number_of_match, expected", [(0, 0),
                                                           (1, 1),
                                                           (2, 2),
                                                           (3, 4),
                                                           (4, 8)])
    def test_compute_score(self, card_1, number_of_match: int, expected: int):
        card_1.number_of_match = Mock(return_value=number_of_match)
        assert card_1.computer_score() == expected


def test_import_puzzle(f_example_puzzle):
    result = import_puzzle(f_example_puzzle)
    expected = [CARD_1, CARD_20, CARD_300]
    assert result == expected


@pytest.mark.parametrize("fixture_name, expected", [("f_example_puzzle", 518),
                                                    ("f_puzzle", 18519)])
def test_puzzle_1(fixture_name, expected, request):
    puzzle_file = request.getfixturevalue(fixture_name)
    assert puzzle_1(puzzle_file) == expected
