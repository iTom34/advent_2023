import pytest
from mock import Mock
from pathlib import Path
from importlib_resources import files

import advent.tests.resources.day_4
from advent.day_4 import import_puzzle, Card, puzzle_1, CardNewRules, import_puzzle_2, process_copies, puzzle_2


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


# --- Puzzle 2 ---

CARD_1_P2 = CardNewRules(1, [88, 11, 20, 66, 55, 92, 43, 23, 98, 70], [99, 81, 56, 30, 88, 55, 57, 11, 90, 45, 53, 28, 33, 20, 84, 54, 24, 64, 74, 98, 36, 77, 61, 82, 69])
CARD_2_P2 = CardNewRules(2, [12, 13, 53, 14, 70, 16, 81, 1, 2, 3], [62, 24, 60, 72, 67, 76, 25, 46, 40, 26, 28, 57, 69, 70, 78, 79, 81, 1, 11, 15, 30, 63, 68, 37, 53])
CARD_3_P2 = CardNewRules(3, [87, 81, 7, 92, 88, 66, 58, 22, 13, 59], [42, 18, 31, 11, 17, 62, 46, 52, 22, 48, 83, 99, 93, 2, 26, 28, 88, 4, 56, 20, 25, 43, 82, 89, 59])
CARD_4_P2 = CardNewRules(4, [13, 92, 1, 2, 3, 4, 5, 6, 7, 8], [69, 16, 12, 58, 27, 49, 67, 31, 47, 53, 35, 89, 75, 20, 96, 44, 50, 92, 14, 98, 15, 81, 84, 13, 10])
CARD_5_P2 = CardNewRules(5, [49, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18, 62, 86, 49, 93, 52, 43, 22, 23, 35, 76, 25, 79, 31, 15, 10, 32, 47, 72, 98, 19, 71, 81, 13, 39])
CARD_6_P2 = CardNewRules(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 15, 93, 66, 49, 11, 83, 55, 22, 17, 40, 43, 80, 84, 29, 74, 34, 16, 39, 31, 92, 56, 96, 68, 65])

CARDS_P2 = [CARD_1_P2,
            CARD_2_P2,
            CARD_3_P2,
            CARD_4_P2,
            CARD_5_P2,
            CARD_6_P2]


@pytest.fixture
def f_example_puzzle2() -> Path:
    example = files(advent.tests.resources.day_4).joinpath("example_puzzle_2.txt")
    return Path(str(example))


@pytest.fixture
def card_1_p2() -> Card:
    return CardNewRules(1, [88, 11, 20, 66, 55, 92, 43, 23, 98, 70], [99, 81, 56, 30, 88, 55, 57, 11, 90, 45, 53, 28, 33, 20, 84, 54, 24, 64, 74, 98, 36, 77, 61, 82, 69])


@pytest.fixture
def card_2_p2() -> Card:
    return CardNewRules(2, [12, 13, 53, 14, 70, 16, 81, 1, 2, 3], [62, 24, 60, 72, 67, 76, 25, 46, 40, 26, 28, 57, 69, 70, 78, 79, 81, 1, 11, 15, 30, 63, 68, 37, 53])


@pytest.fixture
def card_3_p2() -> Card:
    return CardNewRules(3, [87, 81, 7, 92, 88, 66, 58, 22, 13, 59], [42, 18, 31, 11, 17, 62, 46, 52, 22, 48, 83, 99, 93, 2, 26, 28, 88, 4, 56, 20, 25, 43, 82, 89, 59])


@pytest.fixture
def card_4_p2() -> Card:
    return CardNewRules(4, [13, 92, 1, 2, 3, 4, 5, 6, 7, 8], [69, 16, 12, 58, 27, 49, 67, 31, 47, 53, 35, 89, 75, 20, 96, 44, 50, 92, 14, 98, 15, 81, 84, 13, 10])


@pytest.fixture
def card_5_p2() -> Card:
    return CardNewRules(5, [49, 1, 2, 3, 4, 5, 6, 7, 8, 9], [18, 62, 86, 49, 93, 52, 43, 22, 23, 35, 76, 25, 79, 31, 15, 10, 32, 47, 72, 98, 19, 71, 81, 13, 39])


@pytest.fixture
def card_6_p2() -> Card:
    return CardNewRules(6, [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], [30, 15, 93, 66, 49, 11, 83, 55, 22, 17, 40, 43, 80, 84, 29, 74, 34, 16, 39, 31, 92, 56, 96, 68, 65])


@pytest.fixture
def cards_p2(card_1_p2, card_2_p2, card_3_p2, card_4_p2, card_5_p2, card_6_p2) -> list[Card]:
    return [card_1_p2, card_2_p2, card_3_p2, card_4_p2, card_5_p2, card_6_p2]


def test_import_puzzle_2(f_example_puzzle2, cards_p2):
    assert import_puzzle_2(f_example_puzzle2) == cards_p2


@pytest.mark.parametrize("fixture_name, matches", [("card_1_p2", 5),
                                                   ("card_2_p2", 4),
                                                   ("card_3_p2", 3),
                                                   ("card_4_p2", 2),
                                                   ("card_5_p2", 1),
                                                   ("card_6_p2", 0)])
def test_p2_cards_matches(fixture_name: str, matches: int, request):
    card = request.getfixturevalue(fixture_name)
    assert card.number_of_match() == matches


def test_process_copies(cards_p2: list[CardNewRules]):
    process_copies(cards_p2)

    assert cards_p2[0].number_of_cards == 1
    assert cards_p2[1].number_of_cards == 2
    assert cards_p2[2].number_of_cards == 4
    assert cards_p2[3].number_of_cards == 8
    assert cards_p2[4].number_of_cards == 16
    assert cards_p2[5].number_of_cards == 32

@pytest.mark.parametrize("fixture_name, expected", [("f_example_puzzle2", 63),
                                                    ("f_puzzle", 11787590)])
def test_puzzle_2(fixture_name: str, expected: int, request):
    input_puzzle = request.getfixturevalue(fixture_name)
    assert puzzle_2(input_puzzle) == expected