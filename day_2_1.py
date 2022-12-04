# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 1 https://adventofcode.com/2021/day/2

import adv2021_common as common

@common.elapsed_time_factory()
def process_contents(contents):
    # print(contents)
    result = 0
    x = 0
    y = 0
    for pair in contents:
        direction, value = pair.split()
        value = int(value)
        if direction == 'forward':
            x += value
        elif direction == 'down':
            y += value
        elif direction == 'up':
            y -= value
    result = x * y
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 2036120)
