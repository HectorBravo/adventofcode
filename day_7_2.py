# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 7 excercise 2 https://adventofcode.com/2021/day/7

import adv2021_common as common
import time

def calc_fuel(list):
    min_item = min(list)
    max_item = max(list)
    min_count = ((max_item - min_item)//2*(max_item - min_item + 1)) * len(list)
    for horizontal_position in range(max_item, min_item, -1):
        count = 0
        for item in list:
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

def process_solution(contents):
    # print('Contents:', contents)
    crab_list = common.str_list_to_int_lst(contents[0].split(','))
    return calc_fuel(crab_list)

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 86397080)
    print("--- %s seconds ---" % (time.time() - start_time))
