# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2020/day/1#part2

import adv_common as common

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    for i, num in enumerate(_contents):
        numbers = list(filter(lambda x: 2020-x-num in _contents[:i]+_contents[i+1:], _contents[:i]+_contents[i+1:]))
        if len(numbers) == 2:
            return numbers[0]*numbers[1]*num

if __name__ == "__main__":
    contents = common.read_input('int')
    result = process_contents(contents)
    common.print_result(result, 272423970)
