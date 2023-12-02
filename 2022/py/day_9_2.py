# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 2 https://adventofcode.com/2022/day/9

import adv_common as common
import day_9_1

NUM_SEGMENTS = 10

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    positions = day_9_1.gen_positions(_contents, NUM_SEGMENTS)
    # common.draw_positions(positions)
    return len(positions)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2619)
