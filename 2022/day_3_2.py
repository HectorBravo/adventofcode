# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 2 https://adventofcode.com/2022/day/2

from importlib.metadata import packages_distributions
import adv2022_common as common
import time
import day_3_1

def process_solution(contents):
    # print('Contents:', contents)
    groups = [contents[i:i+3] for i in range(0, len(contents), 3)]
    prio_sum = sum([day_3_1.get_prio(''.join(set(group[0]).intersection(group[1]).intersection(group[2]))) for group in groups])
    # prio_sum = 0
    # for group in groups:
    #     print(group)
    #     common = set(group[0]).intersection(group[1]).intersection(group[2])
    #     print(common)
    #     S = ''.join(common)
    #     print(S)
    #     print(ord(S), day_3_1.get_prio(S))
    #     prio_sum += day_3_1.get_prio(S)
    return prio_sum

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 2434)
    print("--- %s seconds ---" % (time.time() - start_time))
