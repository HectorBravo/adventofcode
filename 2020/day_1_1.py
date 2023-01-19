# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2020/day/1

import adv_common as common

@common.elapsed_time_factory()
def process_contents(contents):
    # print(contents)
    numbers = list(filter(lambda x: 2020-x in contents, contents))
    return numbers[0]*numbers[1]

if __name__ == "__main__":
    contents = common.read_input('int')
    result = process_contents(contents)
    common.print_result(result, 703131)
