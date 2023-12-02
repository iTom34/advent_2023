from pathlib import Path
import re

RED_QUANTITY = 12
GREEN_QUANTITY = 13
BLUE_QUANTITY = 14


def parser(file: Path) -> dict:
    """
    Parses the input puzzle
    """

    lines = []

    with open(file, 'r') as file:
        lines = file.readlines()

    tmp_1 = split_games(lines)

    for key, value in tmp_1.items():
        
        sets = []

        regex_results = re.findall(r"[ ]?\d+ \w+[,;]?", value)

        current_set = set()

        for group in regex_results:
            if group[-1] == ",":
                current_set.add(group)

            else:
                current_set.add(group)
                sets.append(current_set)
                current_set = set()

        tmp_1[key] = sets

    built_games = {}

    # Parsing the Key values of each
    for game_id, sets in tmp_1.items():
        build_sets = []
        for a_set in sets:
            build_set = set()
            for quantity in a_set:
                build_set.add(parser_set_key_values(quantity))

            build_sets.append(build_set)

        built_games[game_id] = build_sets

    return built_games


def split_games(lines: list[str]) -> dict:

    games: dict = {}
    for line in lines:
        result = re.match(r"Game (\d+): (.+)", line)

        if result is not None:
            games[int(result[1])] = result[2]

    return games


def parser_set_key_values(text: str) -> tuple:

    quantity, colour = re.findall(r"(\d+) (\w+)", text)[0]

    return colour, int(quantity)


def possible_game(sets: list) -> bool:
    """
    Return true if a game is possible
    :param sets: a game
    :return: True if the game is possible
    """
    possible = True
    for a_set in sets:
        for colour, quantity in a_set:
            if colour == 'red' and quantity > RED_QUANTITY:
                return False

            elif colour == 'green' and quantity > GREEN_QUANTITY:
                return False

            elif colour == 'blue' and quantity > BLUE_QUANTITY:
                return False

    return True


def puzzle_1(input_puzzle: Path) -> int:
    """
    Solves the puzzle 1
    :param input_puzzle: Input of the puzzle
    :return: The solution
    """
    my_sum = 0

    games = parser(input_puzzle)

    for game_id, sets in games.items():
        if possible_game(sets) is True:
            my_sum += game_id

    return my_sum

# ---- Puzzle 2 ----


def minimum_cubes(sets: list) -> dict:
    """
    Find the minimum number of cubes necessary to a game to be possible
    :param sets: All the sets of a game
    :return: Dictionary with the minimum of cubes
    """
    minimums = {}
    for a_set in sets:
        for colour, quantity in a_set:
            if colour not in minimums:
                minimums[colour] = quantity

            else:
                if minimums[colour] < quantity:
                    minimums[colour] = quantity

    return minimums


def computer_power(minimums: dict) -> int:
    """
    Computes the power of the cubes
    :param minimums:
    :return:
    """
    my_sum = 1

    for quantity in minimums.values():
        my_sum *= quantity

    return my_sum


def puzzle_2(input_puzzle: Path) -> int:
    """
    Solves the puzzle 2
    :param input_puzzle:
    :return: Solution
    """
    my_sum = 0

    games = parser(input_puzzle)
    minimums: list[dict] = []

    for sets in games.values():
        minimums.append(minimum_cubes(sets))

    my_sum = 0
    for my_minimum in minimums:
        my_sum += computer_power(my_minimum)

    return my_sum
