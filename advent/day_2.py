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
        result = re.match(r"Game (\d): (.+)", line)

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






























