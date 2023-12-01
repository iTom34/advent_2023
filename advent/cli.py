import argparse
from pathlib import Path

from advent.day_1 import puzzle_1, puzzle_2

def entry_point():
    parser = argparse.ArgumentParser(prog="Advent of code 2023",
                                     description="Solutions of the calendar 2023")

    parser.add_argument("day",
                        help="Day of the puzzle")

    parser.add_argument("puzzle_number",
                        choices=['1', '2'],
                        help="Puzzle number of the day")

    parser.add_argument("data_input",
                        help="Data input to the puzzle")

    args = parser.parse_args()

    if args.day == '1':
        if args.puzzle_number == '1':
            data_input = Path(args.data_input)

            result = puzzle_1(data_input)

            print(f"D01P1 - Solution {result}")

        elif args.puzzle_number == '2':
            
            data_input = Path(args.data_input)

            result = puzzle_2(data_input)

            print(f"D01P2 - Solution {result}")
