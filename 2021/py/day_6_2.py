# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2021/day/6

import adv_common as common
import day_6_1

DAYS_TO_SIMULATE = 256

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return day_6_1.calc_len_after_days_optimal(contents, DAYS_TO_SIMULATE)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int_list', separator = ',')
    result = process_solution(contents)
    common.print_result(result, 1639854996917)
