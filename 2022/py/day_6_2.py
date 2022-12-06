# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 2 https://adventofcode.com/2022/day/6

import sys
sys.path.append('../../common/py')
import adv_common as common
import day_6_1

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    characters = 14
    return day_6_1.get_first_diff_sequence(contents[0], characters)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2803)
