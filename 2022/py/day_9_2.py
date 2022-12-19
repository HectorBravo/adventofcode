# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 2 https://adventofcode.com/2022/day/9

import adv_common as common
import day_9_1

NUM_SEGMENTS = 10

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    positions = day_9_1.gen_positions(contents, NUM_SEGMENTS)
    # day_9_1.draw_positions(positions)
    return len(positions)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2619)
