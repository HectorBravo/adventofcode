# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2022/day/1

import adv_common as common

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    calories_array = [sum(int(content) for content in _contents[i]) for i in range(len(_contents))]
    calories_array.sort()
    return sum(calories_array[-3:])

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 208191)
