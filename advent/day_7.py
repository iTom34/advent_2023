import re
from enum import Enum
from pathlib import Path
from collections import Counter


class Card(Enum):
    a = 13
    k = 12
    q = 11
    j = 10
    t = 9
    nine = 8
    height = 7
    seven = 6
    six = 5
    five = 4
    four = 3
    three = 2
    two = 1


class Type(Enum):
    five_of_a_kind = 7
    four_of_a_kind = 6
    full_house = 5
    three_of_a_kind = 4
    two_pair = 3
    one_pair = 2
    high_card = 1


class Hand:
    def __init__(self, cards: list[Card], beat: int):
        self.cards: list[Card] = cards
        self.beat: int = beat

    def __repr__(self):
        return f"{self.cards}: {self.beat}"

    def __eq__(self, other):
        return self.cards == other.cards and self.beat == other.beat

    def __lt__(self, other):
        if self.get_type() != other.get_type():
            return self.get_type().value < other.get_type().value

        for index in range(5):
            if self.cards[index] != other.cards[index]:
                return self.cards[index].value < other.cards[index].value

        return None

    def get_type(self) -> Type:
        if self._detect_five_of_a_kind():
            return Type.five_of_a_kind

        elif self._detect_four_of_a_kind():
            return Type.four_of_a_kind

        elif self._detect_full_house():
            return Type.full_house

        elif self._detect_three_of_kind():
            return Type.three_of_a_kind

        elif self._detect_two_pair():
            return Type.two_pair

        elif self._detect_one_pair():
            return Type.one_pair

        elif self._detect_high_card():
            return Type.high_card

        else:
            return None

    def _detect_five_of_a_kind(self) -> bool:
        counter = Counter(self.cards)

        for card, count in counter.items():
            if count == 5:
                return True

        return False

    def _detect_four_of_a_kind(self) -> bool:
        counter = Counter(self.cards)

        for card, count in counter.items():
            if count == 4:
                return True

        return False

    def _detect_full_house(self) -> bool:
        counter = Counter(self.cards)

        found_three_identical_cards = False
        found_two_identical_cards = False

        for card, count in counter.items():
            if count == 3:
                found_three_identical_cards = True

            elif count == 2:
                found_two_identical_cards = True

        return found_two_identical_cards and found_three_identical_cards

    def _detect_three_of_kind(self) -> bool:
        counter = Counter(self.cards)

        found_three_identical_cards = False
        found_two_identical_cards = False

        for card, count in counter.items():
            if count == 3:
                found_three_identical_cards = True

            elif count == 2:
                found_two_identical_cards = True

        return not found_two_identical_cards and found_three_identical_cards

    def _detect_two_pair(self) -> bool:
        counter = Counter(self.cards)

        number_of_pair = 0

        for card, count in counter.items():
            if count == 2:
                number_of_pair += 1

        return number_of_pair == 2

    def _detect_one_pair(self) -> bool:
        counter = Counter(self.cards)

        number_of_pair = 0

        for card, count in counter.items():
            if count == 2:
                number_of_pair += 1

        return number_of_pair == 1 and not self._detect_full_house()

    def _detect_high_card(self) -> bool:
        result = False
        result |= self._detect_five_of_a_kind()
        result |= self._detect_four_of_a_kind()
        result |= self._detect_full_house()
        result |= self._detect_three_of_kind()
        result |= self._detect_two_pair()
        result |= self._detect_one_pair()

        return not result


MAP_CAR_CARD = {'A', Card.a,
                'K', Card.k,
                'Q', Card.q,
                'J', Card.j,
                '9', Card.nine,
                '8', Card.height,
                '7', Card.seven,
                '6', Card.six,
                '5', Card.five,
                '4', Card.four,
                '3', Card.three,
                '2', Card.two}


def car_to_card(car: str) -> Card:
    if car == 'A':
        return Card.a

    elif car == 'K':
        return Card.k

    elif car == 'Q':
        return Card.q

    elif car == 'J':
        return Card.j

    elif car == 'T':
        return Card.t

    elif car == '9':
        return Card.nine

    elif car == '8':
        return Card.height

    elif car == '7':
        return Card.seven

    elif car == '6':
        return Card.six

    elif car == '5':
        return Card.five

    elif car == '4':
        return Card.four

    elif car == '3':
        return Card.three

    elif car == '2':
        return Card.two


def import_puzzle(input_file: Path) -> list[Hand]:
    with open(input_file) as file:
        lines = file.readlines()

    hands: list[Hand] = []
    for line in lines:
        match = re.match(r"(.)(.)(.)(.)(.) (\d\d?\d?)", line)

        cards: list[Card] = []
        for index in range(1, 6):
            cards.append(car_to_card(match[index]))

        hands.append(Hand(cards, int(match[6])))

    return hands


def puzzle_1(input_file: Path) -> int:
    hands = import_puzzle(input_file)

    hands.sort()

    result = 0
    for index, hand in enumerate(hands):
        result += (index + 1) * hand.beat

    return result