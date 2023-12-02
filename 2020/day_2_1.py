# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 1 https://adventofcode.com/2020/day/2

import adv_common as common
import re

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)

    number = 0
    for content in _contents:
        minimum, maximum, letter, password = re.fullmatch(r'(\d+)-(\d+) (.): (\w+)', content).groups()
        minimum, maximum = int(minimum), int(maximum)
        # print(minimum, maximum, letter, password, password.count(letter))

        if password.count(letter) in list(range(minimum, maximum + 1)):
            number += 1
    return number

if __name__ == "__main__":
    contents = common.read_input('str')
    result = process_contents(contents)
    common.print_result(result, 454)