import pytest
from pathlib import Path
from importlib_resources import files
from mock import Mock

import advent.tests.resources.day_7
from advent.day_7 import Hand, Card, Type, car_to_card, import_puzzle, puzzle_1

IMPORTED_EXAMPLE = [Hand([Card.three, Card.two, Card.t, Card.three, Card.k], 765),
                    Hand([Card.t, Card.five, Card.five, Card.j, Card.five], 684),
                    Hand([Card.k, Card.k, Card.six, Card.seven, Card.seven], 28),
                    Hand([Card.k, Card.t, Card.j, Card.j, Card.t], 220),
                    Hand([Card.q, Card.q, Card.q, Card.j, Card.a], 483)]


@pytest.fixture
def f_example() -> Path:
    example = files(advent.tests.resources.day_7).joinpath("example.txt")
    return Path(str(example))


@pytest.fixture
def f_puzzle() -> Path:
    example = files(advent.tests.resources.day_7).joinpath("puzzle.txt")
    return Path(str(example))


@pytest.fixture
def f_five_of_a_kind() -> Hand:
    return Hand([Card.a, Card.a, Card.a, Card.a, Card.a], 1)


@pytest.fixture
def f_four_of_a_kind() -> Hand:
    return Hand([Card.a, Card.j, Card.a, Card.a, Card.a], 2)


@pytest.fixture
def f_full_house() -> Hand:
    return Hand([Card.a, Card.j, Card.a, Card.j, Card.a], 3)


@pytest.fixture
def f_three_of_a_kind() -> Hand:
    return Hand([Card.a, Card.j, Card.a, Card.k, Card.a], 4)


@pytest.fixture
def f_two_pair() -> Hand:
    return Hand([Card.a, Card.j, Card.a, Card.k, Card.j], 5)


@pytest.fixture
def f_one_pair() -> Hand:
    return Hand([Card.a, Card.j, Card.k, Card.q, Card.k], 6)


@pytest.fixture
def f_high_card() -> Hand:
    return Hand([Card.a, Card.j, Card.k, Card.q, Card.t], 7)


@pytest.mark.parametrize("car, expected", [('A', Card.a),
                                           ('K', Card.k),
                                           ('Q', Card.q),
                                           ('J', Card.j),
                                           ('T', Card.t),
                                           ('9', Card.nine),
                                           ('8', Card.height),
                                           ('7', Card.seven),
                                           ('6', Card.six),
                                           ('5', Card.five),
                                           ('4', Card.four),
                                           ('3', Card.three),
                                           ('2', Card.two)])
def test_car_to_card(car: str, expected: Card):
    assert car_to_card(car) == expected


def test_import_puzzle(f_example: Path):
    assert import_puzzle(f_example) == IMPORTED_EXAMPLE


class TestHand:
    @pytest.mark.parametrize("hand_1, hand_2, expected",
                             [(Hand([Card.k, Card.t], 123), Hand([Card.k, Card.t], 123), True),
                              (Hand([Card.k, Card.t], 123), Hand([Card.k, Card.t], 256), False),
                              (Hand([Card.k, Card.k], 123), Hand([Card.k, Card.t], 123), False)])
    def test_equality(self, hand_1: Hand, hand_2: Hand, expected: bool):
        assert (hand_1 == hand_2) == expected

    @pytest.mark.parametrize("hand, expected",
                             [(Hand([Card.a, Card.a, Card.a, Card.a, Card.a], 0), Type.five_of_a_kind),
                              (Hand([Card.a, Card.k, Card.a, Card.a, Card.a], 0), Type.four_of_a_kind),
                              (Hand([Card.a, Card.k, Card.a, Card.k, Card.a], 0), Type.full_house),
                              (Hand([Card.a, Card.k, Card.j, Card.k, Card.k], 0), Type.three_of_a_kind),
                              (Hand([Card.k, Card.a, Card.j, Card.j, Card.a], 0), Type.two_pair),
                              (Hand([Card.j, Card.a, Card.k, Card.t, Card.a], 0), Type.one_pair),
                              (Hand([Card.a, Card.j, Card.k, Card.t, Card.q], 0), Type.high_card)])
    def test_get_type(self, hand: Hand, expected: Type):
        assert hand.get_type() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', True),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', False)])
    def test_detect_five_of_a_kind(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_five_of_a_kind() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', True),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', False)])
    def test_detect_four_of_a_kind(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_four_of_a_kind() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', True),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', False)])
    def test_detect_full_house(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_full_house() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', True),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', False)])
    def test_detect_three_of_a_kind(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_three_of_kind() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', True),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', False)])
    def test_detect_two_pair(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_two_pair() == expected

    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', True),
                                                        ('f_high_card', False)])
    def test_detect_one_pair(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_one_pair() == expected


    @pytest.mark.parametrize("fixture_name, expected", [('f_five_of_a_kind', False),
                                                        ('f_four_of_a_kind', False),
                                                        ('f_full_house', False),
                                                        ('f_three_of_a_kind', False),
                                                        ('f_two_pair', False),
                                                        ('f_one_pair', False),
                                                        ('f_high_card', True)])
    def test_detect_one_pair(self, fixture_name: str, expected: bool, request):
        hand = request.getfixturevalue(fixture_name)
        assert hand._detect_high_card() == expected

    @pytest.mark.parametrize("fixture_hand, expected", [('f_five_of_a_kind', Type.five_of_a_kind),
                                                        ('f_four_of_a_kind', Type.four_of_a_kind),
                                                        ('f_full_house', Type.full_house),
                                                        ('f_three_of_a_kind', Type.three_of_a_kind),
                                                        ('f_two_pair', Type.two_pair),
                                                        ('f_one_pair', Type.one_pair),
                                                        ('f_high_card', Type.high_card)])
    def test_get_type(self, fixture_hand: Hand, expected: Type, request):
        hand = request.getfixturevalue(fixture_hand)
        assert hand.get_type() == expected

    @pytest.mark.parametrize("hand_1", ['f_five_of_a_kind',
                                          'f_four_of_a_kind',
                                          'f_full_house',
                                          'f_three_of_a_kind',
                                          'f_two_pair',
                                          'f_one_pair',
                                          'f_high_card'])
    @pytest.mark.parametrize("hand_2", ['f_five_of_a_kind',
                                          'f_four_of_a_kind',
                                          'f_full_house',
                                          'f_three_of_a_kind',
                                          'f_two_pair',
                                          'f_one_pair',
                                          'f_high_card'])
    def test_compare_different_type(self, hand_1: Hand, hand_2: Hand, request):
        hand_1 = request.getfixturevalue(hand_1)
        hand_2 = request.getfixturevalue(hand_2)
        if hand_1.get_type() != hand_2.get_type():
            assert (hand_1 < hand_2) == (hand_1.get_type().value < hand_2.get_type().value)


    @pytest.mark.parametrize("cards_1, cards_2, expected", [([Card.k], [Card.a], True),
                                                            ([Card.k, Card.k], [Card.k, Card.a], True),
                                                            ([Card.k, Card.k, Card.k], [Card.k, Card.k, Card.a], True),
                                                            ([Card.k, Card.k, Card.k, Card.k], [Card.k, Card.k, Card.k, Card.a], True),
                                                            ([Card.k, Card.k, Card.k, Card.k, Card.k], [Card.k, Card.k, Card.k, Card.k, Card.a], True)])
    def test_compare_same_type(self, cards_1: list[Card], cards_2: list[Card], expected: bool):
        hand_1 = Hand(cards_1, 123)
        hand_1.get_type = Mock(return_value=Type.five_of_a_kind)

        hand_2 = Hand(cards_2, 123)
        hand_2.get_type = Mock(return_value=Type.five_of_a_kind)

        assert (hand_1 < hand_2) == expected
        hand_1.get_type.assert_called_once()
        hand_2.get_type.assert_called_once()

    def test_sort(self, f_five_of_a_kind, f_four_of_a_kind, f_full_house, f_three_of_a_kind, f_two_pair, f_one_pair, f_high_card):
        hands = [f_five_of_a_kind, f_four_of_a_kind, f_full_house, f_three_of_a_kind, f_two_pair, f_one_pair, f_high_card]
        hands.sort()
        assert hands == [f_high_card, f_one_pair, f_two_pair, f_three_of_a_kind, f_full_house, f_four_of_a_kind, f_five_of_a_kind]


@pytest.mark.parametrize("puzzle_input, expected", [("f_example", 6440),
                                                    ("f_puzzle", 246644206)])
def test_puzzle(puzzle_input: str, expected: int, request):
    puzzle_file = request.getfixturevalue(puzzle_input)
    assert puzzle_1(puzzle_file) == expected