import argparse
from pathlib import Path

import advent.year_2023.day_1
import advent.day_1
import advent.day_2
import advent.day_3
import advent.day_4
import advent.year_2025.day_1

def entry_point():
    parser = argparse.ArgumentParser(prog="Advent of code 2023",
                                     description="Solutions of the calendar 2023")

    parser.add_argument("year",
                        choices=['2023', '2025'],
                        help="Year of the puzzle")

    parser.add_argument("day",
                        choices=['1', '2', '3', '4'],
                        help="Day of the puzzle")

    parser.add_argument("puzzle_number",
                        choices=['1', '2'],
                        help="Puzzle number of the day")

    parser.add_argument("data_input",
                        help="Data input to the puzzle")

    args = parser.parse_args()
    data_input = Path(args.data_input)

    advent_2023 = {'1': advent.year_2023.day_1.day1}
    advent_2025 = {'1': advent.year_2025.day_1.day1}
    years = {'2025': advent_2025,
             '2023': advent_2023}

    if args.year in years:
        year = years[args.year]
        if args.day in year:
            day = year[args.day]
            if args.puzzle_number == '1':
                day.puzzle_1(args.data_input)
            elif args.puzzle_number == '2':
                day.puzzle_2(args.data_input)
            else:
                print(f"Puzzle {args.puzzle_number} is not implemented")
        else:
            print(f"Day {args.day} is not implemented")
    else:
        print(f"Year {args.year} is not implemented")

