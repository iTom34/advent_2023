from pathlib import Path
from collections import namedtuple

DigitCoordinates = namedtuple("Coordinates", "line column")


class Number:
    def __init__(self, value: int, digit_coordinates: list[DigitCoordinates]):
        """
        Constructor of a number
        :param value: Values of a number
        :param digit_coordinates: List individual digit coordinates
        """
        self.value = value
        digit_coordinates: list[DigitCoordinates] = digit_coordinates


def import_puzzle(input_file: Path) -> list[str]:
    """
    Imports the file and converts it into a list of strings
    :param input_file: input puzzle file
    :return: List of string
    """
    with open(input_file, 'r') as file:
        lines = file.readlines()

    # Removes '/n'
    for index, line in enumerate(lines):
        lines[index] = line.rstrip()

    return lines


def find_numbers(text: list[str]) -> list[Number]:
    """
    Finds numbers in text file
    :param text:
    :return:
    """
    pass


def has_adjacent_symbol(coordinates: DigitCoordinates) -> bool:
    """
    For a coordinates, check surrouding for a symbol
    :param coordinates: Coordinates to check
    :return: True if surrounded by a symbol
    """
    pass

