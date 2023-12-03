from pathlib import Path


class DigitCoordinates:
    def __init__(self, line: int, column: int):
        self.line: int = line
        self.column: int = column

    def __hash__(self):
        return hash((self.line, self.column))

    def __eq__(self, other):
        result_1 = self.line == other.line
        result_2 = self.column == other.column
        return result_1 and result_2

    def __repr__(self):
        return f"({self.line}, {self.column})"


class Number:
    def __init__(self, value: int, digit_coordinates: frozenset[DigitCoordinates]):
        """
        Constructor of a number
        :param value: Values of a number
        :param digit_coordinates: List individual digit coordinates
        """
        self.value = value
        self.digit_coordinates: frozenset = digit_coordinates

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        result = f"{self.value}: "

        for a_digit_coordinates in self.digit_coordinates:
            result += f"{a_digit_coordinates} "

        return result

    def __eq__(self, other):
        result_1 = self.value == other.value
        result_2 = self.digit_coordinates == other.digit_coordinates
        return result_1 and result_2

    def __hash__(self):
        return hash((self.value, self.digit_coordinates))


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


def find_numbers(text: list[str]) -> set[Number]:
    """
    Finds numbers in text file
    :param text:
    :return:
    """
    result: list[Number] = []

    for line_index, line in enumerate(text):
        number_value = 0
        digit_coordinates = []

        for column_index, car in enumerate(line):
            # A Number
            if car.isnumeric():
                number_value *= 10
                number_value += int(car)
                digit_coordinates.append(DigitCoordinates(line_index, column_index))

            # Not a number and not empty
            elif len(digit_coordinates) != 0:
                result.append(Number(number_value, frozenset(digit_coordinates)))
                number_value = 0
                digit_coordinates = []

            # End of line and not empty
            if column_index == (len(line) - 1) and len(digit_coordinates) != 0:
                result.append(Number(number_value, frozenset(digit_coordinates)))
                number_value = 0
                digit_coordinates = []

    return result


def has_adjacent_symbol(coordinates: DigitCoordinates) -> bool:
    """
    For a coordinates, check surrouding for a symbol
    :param coordinates: Coordinates to check
    :return: True if surrounded by a symbol
    """
    pass

