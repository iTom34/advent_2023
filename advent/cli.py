import argparse
from pathlib import Path

import advent.day_1
import advent.day_2
import advent.day_3


def entry_point():
    parser = argparse.ArgumentParser(prog="Advent of code 2023",
                                     description="Solutions of the calendar 2023")

    parser.add_argument("day",
                        choices=['1', '2', '3'],
                        help="Day of the puzzle")

    parser.add_argument("puzzle_number",
                        choices=['1', '2'],
                        help="Puzzle number of the day")

    parser.add_argument("data_input",
                        help="Data input to the puzzle")

    args = parser.parse_args()
    data_input = Path(args.data_input)

    if args.day == '1':
        if args.puzzle_number == '1':
            result = advent.day_1.puzzle_1(data_input)
            print(f"D01P1 - Solution {result}")

        elif args.puzzle_number == '2':
            result = advent.day_1.puzzle_2(data_input)
            print(f"D01P2 - Solution {result}")

    elif args.day == '2':
        if args.puzzle_number == '1':
            result = advent.day_2.puzzle_1(data_input)
            print(f"D02P1 - Solution {result}")

        elif args.puzzle_number == '2':
            result = advent.day_2.puzzle_2(data_input)
            print(f"D02P2 - Solution {result}")

    elif args.day == '3':
        if args.puzzle_number == '1':
            result = advent.day_3.puzzle_1(data_input)
            print(f"D03P1 - Solution {result}")

        elif args.puzzle_number == '2':
            result = advent.day_3.puzzle_2(data_input)
            print(f"D03P2 - Solution {result}")
