# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 2 excercise 1 https://adventofcode.com/2022/day/1

import adv_common as common

outcome_score = {   ('B X'): (0, 1), ('C Y'): (3, 3), ('A Z'): (6, 2),
                                    ('A X'): (0, 3), ('B Y'): (3, 2), ('C Z'): (6, 1),
                                    ('C X'): (0, 2), ('A Y'): (3, 1), ('B Z'): (6, 3) }

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    count = sum(sum(outcome_score[pair]) for pair in _contents)
    return count

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 14204)
