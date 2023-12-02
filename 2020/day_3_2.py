# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 2 https://adventofcode.com/2020/day/3

import adv_common as common
import math

def get_trees(_coord):
    return len(list(filter(lambda x: x == '#', [contents[i*_coord[1]][(_coord[0]*i) % len(contents[0])] for i in range(1, int((len(contents)-1)/_coord[1]) + 1)])))

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    paths = ((1, 1), (3, 1), (5, 1), (7, 1), (1, 2))
    return math.prod(list(map(get_trees, paths)))

if __name__ == "__main__":
    contents = common.read_input('char_list')
    result = process_contents(contents)
    common.print_result(result, 3952146825)
