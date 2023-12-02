# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 2 https://adventofcode.com/2020/day/2

import adv_common as common
import re

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)

    number = 0
    for content in _contents:
        lower, higher, letter, password = re.fullmatch(r'(\d+)-(\d+) (.): (\w+)', content).groups()
        lower, higher = int(lower), int(higher)
        # print(lower, higher, letter, password, password[lower-1] == letter, password[higher-1] == letter)

        if (password[lower-1] == letter) ^ (password[higher-1] == letter):
            number += 1
    return number

if __name__ == "__main__":
    contents = common.read_input('str')
    result = process_contents(contents)
    common.print_result(result, 649)