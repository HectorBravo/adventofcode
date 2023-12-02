# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2021/day/1#part2

import adv_common as common

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    _result = 0
    previous_sum = sum(_contents[0:3])
    for i in range(1, len(_contents)-2):
        current_sum = sum(_contents[i:i+3])
        if current_sum > previous_sum:
            _result += 1
        previous_sum = current_sum
    return _result

@common.elapsed_time_factory()
def process_contents2(_contents):
    # print(_contents)
    return len([_contents[i:i+4] for i in range(0, len(_contents) - 1) if sum(_contents[i+1:i+4]) > sum(_contents[i:i+3])])

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int')
    result = process_contents(contents)
    common.print_result(result, 1378)
    result = process_contents2(contents)
    common.print_result(result, 1378)
