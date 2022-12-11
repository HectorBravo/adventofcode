# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 1 https://adventofcode.com/2022/day/5

import sys
import adv_common as common

def split_input(input):
    directions = []
    blank_line_found = False
    crates = [[] for _ in range(len(input[0]) // 4 + 1)]

    for line in input:
        if blank_line_found:
            directions += [tuple([int(x) for x in line.split(' ') if x.lstrip("-").isnumeric()])]
        elif line == '':
            blank_line_found = True
        else:
            for i in range(len(line) // 4 + 1):
                if line[4*i+1: 4*i+2] != ' ':
                    crates[i].append(line[4*i+1: 4*i+2])
    return crates, directions

def move_elems(elems, src_crate, dst_crate):
    for _ in range(elems):
        dst_crate.insert(0, src_crate.pop(0))

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    crates, directions = split_input(contents)
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
    common.print_result(result, 'RTGWZTHLD')
