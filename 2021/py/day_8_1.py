# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 8 excercise 1 https://adventofcode.com/2021/day/8

import adv_common as common

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    number_list =[]
    for line in contents:
        _, right = line.split('|')
        number_list += list(filter(lambda x : len(x) == 2 or len(x) == 3 or len(x) == 4 or len(x) == 7, right.split()))
    return len(number_list)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 495)
