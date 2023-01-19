# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2020/day/1#part2

import adv_common as common

@common.elapsed_time_factory()
def process_contents(contents):
    # print(contents)
    for i, num in enumerate(contents):
        numbers = list(filter(lambda x: 2020-x-num in contents[:i]+contents[i+1:], contents[:i]+contents[i+1:]))
        if len(numbers) == 2:
            return numbers[0]*numbers[1]*num

if __name__ == "__main__":
    contents = common.read_input('int')
    result = process_contents(contents)
    common.print_result(result, 272423970)