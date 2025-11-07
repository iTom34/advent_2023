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


def car_has_adjacent_symbol(text: list[str], coordinates: DigitCoordinates) -> bool:
    """
    For a coordinates, check surrouding for a symbol
    :param coordinates: Coordinates to check
    :return: True if surrounded by a symbol
    """
    max_index_column = len(text[0]) - 1
    max_index_line = len(text) - 1
    line = coordinates.line
    column = coordinates.column

    top_condition = line - 1 >= 0
    bottom_condition = line + 1 <= max_index_line
    left_condition = column - 1 >= 0
    right_condition = column + 1 <= max_index_column

    result = False

    # Top left
    if top_condition and left_condition:
        car = text[line - 1][column - 1]
        result |= (not car.isnumeric()) and car != '.'

    # Top
    if top_condition:
        car = text[line - 1][column]
        result |= (not car.isnumeric()) and car != '.'

    # Top right
    if top_condition and right_condition:
        car = text[line - 1][column + 1]
        result |= (not car.isnumeric()) and car != '.'

    # Right
    if right_condition:
        car = text[line][column + 1]
        result |= (not  car.isnumeric()) and car != '.'

    # Bottom Right
    if bottom_condition and right_condition:
        car = text[line + 1][column + 1]
        result |= (not car.isnumeric()) and car != '.'

    # Bottom
    if bottom_condition:
        car = text[line + 1][column]
        result |= (not car.isnumeric()) and car != '.'

    # Bottom left
    if bottom_condition and left_condition:
        car = text[line + 1][column - 1]
        result |= (not car.isnumeric()) and car != '.'

    # Left
    if left_condition:
        car = text[line][column - 1]
        result |= (not car.isnumeric()) and car != '.'

    return result


def number_has_adjacent_symbol(text: list[str], number: Number) -> bool:
    """
    Return True if the number has an adjacent symbol
    """

    for coordinates in number.digit_coordinates:
        if car_has_adjacent_symbol(text, coordinates):
            return True

    return False


def puzzle_1(input_puzzle: Path) -> int:
    """
    Solves puzzle_1
    """
    sum = 0

    text = import_puzzle(input_puzzle)
    numbers = find_numbers(text)

    for number in numbers:
        if number_has_adjacent_symbol(text, number):
            sum += number.value

    return sum


# --- Puzzle 2 ---

class Star:
    """
    Holds a star position
    """
    def __init__(self, line: int, column: int):
        self.line: int = line
        self.column: int = column

    def __eq__(self, other):
        return self.line == other.line and self.column == other.column

    def __repr__(self):
        return f"({self.line}, {self.column})"

    def _find_adjacent_numbers(self, numbers: list[Number]) -> list[tuple]:
        """
        Finds the adjacent numbers and return them in list of tuple.
        """
        adjacent_numbers = []
        for number in numbers:
            for coordinate in number.digit_coordinates:

                if (coordinate.line == (self.line - 1)) and (coordinate.column == (self.column - 1)):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == (self.line - 1)) and (coordinate.column == self.column):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == (self.line - 1)) and (coordinate.column == (self.column + 1)):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == self.line) and (coordinate.column == (self.column + 1)):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == (self.line + 1)) and (coordinate.column == (self.column + 1)):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == (self.line + 1)) and (coordinate.column == self.column):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == (self.line + 1)) and (coordinate.column == (self.column - 1)):
                    adjacent_numbers.append(number)
                    break

                elif (coordinate.line == self.line) and (coordinate.column == (self.column - 1)):
                    adjacent_numbers.append(number)
                    break

        return adjacent_numbers

    def compute_gear_ratio(self, numbers: list[Number]) -> int:
        """
        Compute the gear ratio of a star
        """
        adjacent_numbers = self._find_adjacent_numbers(numbers)

        if len(adjacent_numbers) == 2:
            return adjacent_numbers[0].value * adjacent_numbers[1].value

        return 0


def find_starts(puzzle_input: list[str]) -> list[Star]:
    """
    Find the start in a puzzle
    return a list with all the starts found
    """
    stars = []
    for line_index, line in enumerate(puzzle_input):
        for column_index, car in enumerate(line):
            if car == '*':
                stars.append(Star(line_index, column_index))

    return stars


def puzzle_2(input_puzzle: Path) -> int:
    text = import_puzzle(input_puzzle)
    numbers = find_numbers(text)
    stars = find_starts(text)

    sum = 0

    for star in stars:
        sum += star.compute_gear_ratio(numbers)

    return sum