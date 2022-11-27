# Copyright Hector Bravo <hbravo@cuic.net>
# Common functions for https://adventofcode.com/2021/

import sys
import os

script_name = os.path.basename(sys.argv[0])
input_file = script_name.split('.')[0] + '_input.txt'

def read_input():
    print('Input file:', input_file)
    with open(input_file) as f:
        contents = f.read().splitlines()
    return contents

def print_result(result, expected_result = None):
    print('Result is:', result)
    if expected_result:
        assert(result == expected_result)

def str_list_to_int_lst(str_list):
    return list(map(int, str_list))