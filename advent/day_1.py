import re
from pathlib import Path


def puzzle_1(input: Path) -> int:
    """
    :param input: input of the puzzle
    :return: solution of the puzzle
    """

    sum = 0

    with open(input, 'r') as file:
        for line in file.readlines():
            sum += find_last_and_first_digit(line)

    return sum


def find_last_and_first_digit(input: str) -> int:
    """
    Combine first and last digit of the string
    :param input: input string
    :return: Combined value of the first and last digit
    """

    first_digit = ""
    last_digit = ""

    for char in input:
        if char.isdigit() is True:
            if first_digit == "":
                first_digit = char
            last_digit = char

    result = int(first_digit) * 10 + int(last_digit)

    return result


def find_start_spelled_number(text: str) -> int | None:
    """
    Finds spelled number at start of text, otherwise return None
    :param text: String containing the text to analyse
    :return: the first integer or None
    """

    result = re.match(r"(one|two|three|four|five|six|seven|eight|nine)", text)

    if result is None:
        return None

    elif result.group(1) == "one":
        return 1

    elif result.group(1) == "two":
        return 2

    elif result.group(1) == "three":
        return 3

    elif result.group(1) == "four":
        return 4

    elif result.group(1) == "five":
        return 5

    elif result.group(1) == "six":
        return 6

    elif result.group(1) == "seven":
        return 7

    elif result.group(1) == "eight":
        return 8

    elif result.group(1) == "nine":
        return 9

    return None


def find_first_and_last_digit_puzzle_2(text: str) -> int:
    """
    Finds the first and last digit (spelled or not)
    :param text: text to analyse
    :return: combined integers
    """

    first_digit = None
    last_digit = None

    for start_index in range(len(text)):
        sub_text = text[start_index:]
        found_digit = None

        if sub_text[0].isdigit() is True:
            found_digit = int(sub_text[0])

        elif find_start_spelled_number(sub_text) is not None:
            found_digit = find_start_spelled_number(sub_text)

        if found_digit is not None:
            if (first_digit is None) and (found_digit is not None):
                first_digit = found_digit

            last_digit = found_digit

    return first_digit * 10 + last_digit


def puzzle_2(source: Path) -> int:
    """
    Solves puzzle 2 of day 1
    :param source: File containing the input of the puzzle
    :return: Solution of the puzzle
    """

    sum = 0

    with open(source, 'r') as file:
        for line in file.readlines():
            sum += find_first_and_last_digit_puzzle_2(line)

    return sum
































