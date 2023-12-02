# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 7 excercise 2 https://adventofcode.com/2021/day/7

import adv_common as common

def calc_fuel(_list):
    min_item = min(_list)
    max_item = max(_list)
    min_count = ((max_item - min_item)//2*(max_item - min_item + 1)) * len(_list)
    for horizontal_position in range(max_item, min_item, -1):
        count = 0
        for item in _list:
            if count > min_count:
                break
            distance = abs(horizontal_position - item)
            if (distance + 1) % 2 == 0:
                count += (((distance + 1) // 2) * (distance))
            else:
                count += ((distance // 2) * (distance + 1))
        if count < min_count:
            min_count = count
    return min_count

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    crab_list = common.str_list_to_int_lst(_contents[0].split(','))
    return calc_fuel(crab_list)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 86397080)
