# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2021/day/6

import sys
sys.path.append('../../common/py')
import adv_common as common

DAYS_TO_SIMULATE = 256

def calc_len_after_days(number, days):
    # print(number, days)
    count = 1
    if days > 0:
        for days_remaining in range(days, 0, -1):
            if (number == 0):
                count += calc_len_after_days(8, days_remaining - 1)
                number = 6
            else:
                number -= 1
    return count

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return sum([calc_len_after_days(number, DAYS_TO_SIMULATE) for number in contents])

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int_list', separator = ',')
    result = process_solution(contents)
    common.print_result(result, 1639854996917)
