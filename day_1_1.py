# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2021/day/1

import adv2021_common as common

def process_contents(contents):
    # print(contents)
    result = 0
    previous = contents[0]
    for current in contents:
        if int(current) > int(previous):
            result += 1
        previous = current
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 1342)