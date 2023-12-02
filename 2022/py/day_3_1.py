# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2022/day/3

import adv_common as common

def get_prio(_item):
    prio = 0
    if _item >= 'a':
        prio = ord(_item) - ord('a') + 1
    else:
        prio = ord(_item) - ord('A') + 27
    return prio

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    prio_sum = sum(get_prio(''.join(set(rucksack[:len(rucksack) // 2]).intersection(rucksack[(len(rucksack) // 2):]))) for rucksack in _contents)
    # prio_sum = 0
    # for rucksack in _contents:
    #     print(rucksack[:len(rucksack) // 2], rucksack[(len(rucksack) // 2):])
    #     common = set(rucksack[:len(rucksack) // 2]).intersection(rucksack[(len(rucksack) // 2):])
    #     S = ''.join(common)
    #     print(S)
    #     print(ord(S), get_prio(S))
    #     prio_sum += get_prio(S)
    return prio_sum

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 8515)
