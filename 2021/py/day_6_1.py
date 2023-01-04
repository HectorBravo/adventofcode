# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2021/day/6

import adv_common as common
import collections as cl

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
        # print('day:', day, 'fish_list:', fish_list)
    return len(fish_list)

def calc_len_after_days_optimal(fish_list, days):
    collection = cl.Counter(
        fish for fish in fish_list
    )
    for day in range(days):
        _new_collection = cl.Counter()
        for age, fishes in collection.items():
            if age == 0:
                _new_collection[6] += fishes
                _new_collection[8] += fishes
            else:
                _new_collection[age - 1] += fishes
        collection = _new_collection
        # print('day:', day, 'fish_list:', collection)
    return collection.total()

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return calc_len_after_days(list(contents), DAYS_TO_SIMULATE)

@common.elapsed_time_factory()
def process_solution2(contents):
    # print('Contents:', contents)
    return calc_len_after_days_optimal(contents, DAYS_TO_SIMULATE)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int_list', separator = ',')
    result = process_solution(contents)
    common.print_result(result, 362639)
    result = process_solution2(contents)
    common.print_result(result, 362639)