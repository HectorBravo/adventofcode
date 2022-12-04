# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 4 excercise 1 https://adventofcode.com/2022/day/4

import adv2022_common as common

def process_solution(contents):
    # print('Contents:', contents)
    pairs = [pair.split(',') for pair in contents]
    count = 0
    for pair in pairs:
        pair1 = list(map(int, pair[0].split('-')))
        pair2 = list(map(int, pair[1].split('-')))
        set1 = set(range(pair1[0], pair1[1] + 1))
        set2 = set(range(pair2[0], pair2[1] + 1))
        if set1.issubset(set2) or set2.issubset(set1):
            count += 1
    return count

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 571)
