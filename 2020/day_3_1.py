# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2020/day/3

import adv_common as common

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    return len(list(filter(lambda x: x == '#', [_contents[i][(3*i) % len(_contents[0])] for i in range(1, len(_contents))])))

if __name__ == "__main__":
    contents = common.read_input('char_list')
    result = process_contents(contents)
    common.print_result(result, 205)
