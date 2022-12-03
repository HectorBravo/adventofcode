# Copyright Hector Bravo <hbravo@cuic.net>
# Common functions for https://adventofcode.com/2021/

import sys
import os

script_name = os.path.basename(sys.argv[0])
input_file = script_name.split('.')[0][:-2] + '_input.txt'

def read_input():
    print('Input file:', input_file)
    with open(input_file) as f:
        contents = f.read().splitlines()
    return tuple(contents)

def print_result(result, expected_result = None):
    print('Result is:', result)
    if expected_result:
        assert(result == expected_result)

def str_list_to_int_lst(str_list):
    return list(map(int, str_list))

def gen_point_list(vector):
    # print('vector:', vector)
    x0 = vector[0]
    y0 = vector[1]
    x1 = vector[2]
    y1 = vector[3]

    direction_x = 0
    direction_y = 0

    if x0 > x1:
        direction_x = -1
    elif x0 < x1:
        direction_x = 1
    if y0 > y1:
        direction_y = -1
    elif y0 < y1:
        direction_y = 1

    max_steps_x = abs(x0 - x1) + 1
    max_steps_y = abs(y0 - y1) + 1
    num_steps = max(max_steps_x, max_steps_y)

    point_list = [(x0 + step * direction_x, y0 + step *direction_y) for step in range(num_steps)]
    return tuple(point_list)
