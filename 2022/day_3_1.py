# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2022/day/3

import adv2022_common as common
import time

def get_prio(item):
    prio = 0
    if item >= 'a':
        prio = ord(item) - ord('a') + 1
    else:
        prio = ord(item) - ord('A') + 27
    return prio

def process_solution(contents):
    # print('Contents:', contents)
    prio_sum = sum([get_prio(''.join(set(rucksack[:len(rucksack) // 2]).intersection(rucksack[(len(rucksack) // 2):]))) for rucksack in contents])
    # prio_sum = 0
    # for rucksack in contents:
    #     print(rucksack[:len(rucksack) // 2], rucksack[(len(rucksack) // 2):])
    #     common = set(rucksack[:len(rucksack) // 2]).intersection(rucksack[(len(rucksack) // 2):])
    #     S = ''.join(common)
    #     print(S)
    #     print(ord(S), get_prio(S))
    #     prio_sum += get_prio(S)
    return prio_sum

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 8515)
    print("--- %s seconds ---" % (time.time() - start_time))
