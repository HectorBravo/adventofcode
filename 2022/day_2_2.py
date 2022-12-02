# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 1 https://adventofcode.com/2022/day/1

import adv2022_common as common
import time

outcome_score = {   ('B X'): (0, 1), ('C Y'): (3, 3), ('A Z'): (6, 2),
                                    ('A X'): (0, 3), ('B Y'): (3, 2), ('C Z'): (6, 1),
                                    ('C X'): (0, 2), ('A Y'): (3, 1), ('B Z'): (6, 3) }

def process_solution(contents):
    # print('Contents:', contents)
    count = sum(sum(outcome_score[pair]) for pair in contents)
    return count

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 14204)
    print("--- %s seconds ---" % (time.time() - start_time))
