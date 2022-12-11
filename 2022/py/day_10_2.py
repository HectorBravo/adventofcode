# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 10 excercise 2 https://adventofcode.com/2022/day/10

import sys
sys.path.append('../../common/py')
import adv_common as common
import numpy as np

CRT_COLS = 40
CRT_ROWS = 6

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    cycles = 0
    register_x = 1
    crt_string = ''
    for instruction in contents:
        if (cycles % CRT_COLS) in range(register_x - 1, register_x + 2):
            crt_string += '#'
        else:
            crt_string += ' '
        # print(crt_string)
        cycles += 1
        if instruction != 'noop':
            if (cycles % CRT_COLS) in range(register_x - 1, register_x + 2):
                crt_string += '#'
            else:
                crt_string += ' '
            instruction, value = [int(x) if x.lstrip("-").isnumeric() else x for x in instruction.split()]
            # print(instruction, value)
            cycles += 1
            register_x += value
        # print('cycles, register', cycles, register_x)
    message_array = np.array([crt_string[CRT_COLS*i:CRT_COLS*i+CRT_COLS] for i in range(CRT_ROWS)])
    print(message_array)
    return 0

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    # common.print_result(result, 0)
