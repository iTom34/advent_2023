from pathlib import Path
import re


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
            build_set = []
            for quantity in a_set:
                build_set.append(parser_set_key_values(quantity))

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


def parser_set_key_values(text: str) -> dict:

    quantity, colour = re.findall(r"(\d+) (\w+)", text)[0]

    return {colour: int(quantity)}
