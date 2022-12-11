# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2021/day/1#part2

import sys
import adv_common as common

@common.elapsed_time_factory()
def process_contents(contents):
    # print(contents)
    result = 0
    previous_sum = sum(contents[0:3])
    for i in range(1, len(contents)-2):
        current_sum = sum(contents[i:i+3])
        if current_sum > previous_sum:
            result += 1
        previous_sum = current_sum
    return result

@common.elapsed_time_factory()
def process_contents2(contents):
    # print(contents)
    return len([contents[i:i+4] for i in range(0, len(contents) - 1) if sum(contents[i+1:i+4]) > sum(contents[i:i+3])])

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int')
    result = process_contents(contents)
    common.print_result(result, 1378)
    result = process_contents2(contents)
    common.print_result(result, 1378)