# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 1 https://adventofcode.com/2022/day/5

import adv_common as common

def split_input(_input):
    crate_list, direction_list = _input
    directions = []
    crates = [[] for _ in range(len(crate_list[0]) // 4 + 1)]

    for direction in direction_list:
        directions += [tuple(int(x) for x in direction.split(' ') if x.lstrip("-").isnumeric())]
    for crate in crate_list:
        for i in range(len(crate) // 4 + 1):
            if crate[4*i+1: 4*i+2] != ' ':
                crates[i].append(crate[4*i+1: 4*i+2])
    return crates, directions

def move_elems(elems, src_crate, dst_crate):
    for _ in range(elems):
        dst_crate.insert(0, src_crate.pop(0))

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    crates, directions = split_input(_contents)
    # print('crates:\n', crates)
    # print('directions:\n', directions)
    for elems, src_crate, dst_crate in directions:
        # print(elems, src_crate, dst_crate)
        move_elems(elems, crates[src_crate - 1], crates[dst_crate - 1])
    # print('crates', crates)
    return "".join([i[0] for i in crates])

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 'RTGWZTHLD')
