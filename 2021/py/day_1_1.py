# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2021/day/1

import adv_common as common

@common.elapsed_time_factory()
def process_contents(contents):
    # print(contents)
    result = 0
    previous = contents[0]
    for current in contents:
        if current > previous:
            result += 1
        previous = current
    return result

@common.elapsed_time_factory()
def process_contents2(contents):
    # print(contents)
    return len([contents[i:i+2] for i in range(0, len(contents) - 1) if contents[i+1] > contents[i]])

if __name__ == "__main__":
    contents = common.read_input('int')
    result = process_contents(contents)
    common.print_result(result, 1342)
    result = process_contents2(contents)
    common.print_result(result, 1342)