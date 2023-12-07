from enum import Enum
from pathlib import Path

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
    pass

