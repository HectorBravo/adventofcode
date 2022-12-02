# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 1 https://adventofcode.com/2022/day/1

import adv2022_common as common
import time

shape_score = {'X': 1, 'Y': 2, 'Z': 3}
outcome_score = {   ('B X'): 0, ('C Y'): 0, ('A Z'): 0,
                                    ('A X'): 3, ('B Y'): 3, ('C Z'): 3,
                                    ('C X'): 6, ('A Y'): 6, ('B Z'): 6 }


def process_solution(contents):
    # print('Contents:', contents)
    count = sum(shape_score[pair.split()[1]] + outcome_score[pair] for pair in contents)
    return count

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 13526)
    print("--- %s seconds ---" % (time.time() - start_time))
