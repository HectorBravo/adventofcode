# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 2 https://adventofcode.com/2022/day/5

import sys
import adv_common as common
import day_5_1

def move_elems(elems, src_crate, dst_crate):
    for i in range(elems):
        dst_crate.insert(0, src_crate.pop(elems - 1 - i))

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    crates, directions = day_5_1.split_input(contents)
    # print('crates:\n', crates)
    # print('directions:\n', directions)
    for elems, src_crate, dst_crate in directions:
        # print(elems, src_crate, dst_crate)
        move_elems(elems, crates[src_crate - 1], crates[dst_crate - 1])
    # print('crates', crates)
    return "".join([i[0] for i in crates])

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 'STHGRZZFR')
