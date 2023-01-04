# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 14 excercise 1 https://adventofcode.com/2021/day/14


import adv_common as common
import day_14_1

ITERATIONS = 40

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return day_14_1.calc_most_common_minus_less_common(contents[0][0], contents[1], ITERATIONS)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 4704817645083)
