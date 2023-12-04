import re
from pathlib import Path

REGULAR_EXPRESSION = r"Card. ? ?(\d+):  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d) \|  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)  ?(\d?\d)"


class Card:
    def __init__(self, card_number: int, winning_numbers: list[int], your_numbers: list[int]):
        self.card_number: int = card_number
        self.winning_numbers: list[int] = winning_numbers
        self.your_numbers: list[int] = your_numbers

    def __repr__(self):
        return f"{self.card_number}: {self.winning_numbers} | {self.your_numbers}"

    def __eq__(self, other):
        return (self.card_number == other.card_number
                and self.winning_numbers == other.winning_numbers
                and self.your_numbers == other.your_numbers)

    def __hash__(self):
        return hash((self.card_number, self.winning_numbers, self.your_numbers))


def import_puzzle(input_file: Path) -> list[Card]:
    """
    Imports the file and converts it into a list of strings
    :param input_file: input puzzle file
    :return: List of string
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    cards = set()
    for line in lines:
        match = re.match(REGULAR_EXPRESSION, line)
        groups = match.groups()

        card_id = groups[0]
        winning_numbers = []
        for index in range(1, 11):
            winning_numbers.append(int(groups[index]))

        your_numbers = []
        for index in range(11, 36):
            your_numbers.append(int(groups[index]))

        cards.add(Card(card_number=card_id,
                          winning_numbers=winning_numbers,
                          your_numbers=your_numbers))

    return cards