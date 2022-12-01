# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2021/day/6

import adv2021_common as common
import numpy as np
import time

DAYS_TO_SIMULATE = 80

def calc_len_after_days(fish_list, days):
    for day in range(days):
        new_ones = []
        for i in range(len(fish_list)):
            fish_list[i] -= 1
            if fish_list[i] < 0:
                fish_list[i] = 6
                new_ones.append(8)
        if new_ones:
            fish_list += new_ones
        print('day:', day, 'fish_list:', fish_list)
    return len(fish_list)

def process_solution(contents):
    # print('Contents:', contents)
    fish_list = common.str_list_to_int_lst(contents[0].split(','))
    # print(fish_list)
    return calc_len_after_days(fish_list, DAYS_TO_SIMULATE)

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 362639)
    print("--- %s seconds ---" % (time.time() - start_time))
