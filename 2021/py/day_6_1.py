# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2021/day/6

import adv_common as common
import collections as cl

DAYS_TO_SIMULATE = 80

def calc_len_after_days(_fish_list, _days):
    for day in range(_days):
        new_ones = []
        for i, _ in enumerate(_fish_list):
            _fish_list[i] -= 1
            if _fish_list[i] < 0:
                _fish_list[i] = 6
                new_ones.append(8)
        if new_ones:
            _fish_list += new_ones
        # print('day:', day, '_fish_list:', _fish_list)
    return len(_fish_list)

def calc_len_after_days_optimal(_fish_list, _days):
    collection = cl.Counter(
        fish for fish in _fish_list
    )
    for day in range(_days):
        _new_collection = cl.Counter()
        for age, fishes in collection.items():
            if age == 0:
                _new_collection[6] += fishes
                _new_collection[8] += fishes
            else:
                _new_collection[age - 1] += fishes
        collection = _new_collection
        # print('day:', day, 'collection:', collection)
    return collection.total()

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    return calc_len_after_days(list(_contents), DAYS_TO_SIMULATE)

@common.elapsed_time_factory()
def process_solution2(_contents):
    # print('Contents:', _contents)
    return calc_len_after_days_optimal(_contents, DAYS_TO_SIMULATE)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'int_list', separator = ',')
    result = process_solution(contents)
    common.print_result(result, 362639)
    result = process_solution2(contents)
    common.print_result(result, 362639)