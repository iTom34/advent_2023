import pytest
from pathlib import Path
from importlib_resources import files

from advent.day_3 import import_puzzle, find_numbers, has_adjacent_symbol

import advent.tests.resources.day_3

EXAMPLE_PUZZLE_PARSED = ["467..114..",
                         "...*......",
                         "..35..633.",
                         "......#...",
                         "617*......",
                         ".....+.58.",
                         "..592.....",
                         "......755.",
                         "...$.*....",
                         ".664.598.."]


@pytest.fixture
def f_example_puzzle() -> Path:
    example = files(advent.tests.resources.day_3).joinpath("example_puzzle.txt")
    return Path(str(example))


def test_import_file(f_example_puzzle):
    assert import_puzzle(f_example_puzzle) == EXAMPLE_PUZZLE_PARSED
