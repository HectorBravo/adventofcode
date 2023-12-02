# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 10 excercise 1 https://adventofcode.com/2022/day/10

import adv_common as common

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    signal_strenght = 0
    cycles = 0
    register_x = 1
    for instruction in _contents:
        cycles += 1
        if cycles == 20 or ((cycles - 20) % 40 == 0):
            signal_strenght += (cycles*register_x)
            print(instruction)
            print('cycles, register, signal_strenght', cycles, register_x, signal_strenght)
        if instruction != 'noop':
            instruction, value = [int(x) if x.lstrip("-").isnumeric() else x for x in instruction.split()]
            print(instruction, value)
            cycles += 1
            if cycles == 20 or ((cycles - 20) % 40 == 0):
                signal_strenght += (cycles*register_x)
                print('cycles, register, signal_strenght', cycles, register_x, signal_strenght)
            register_x += value
        # print('cycles, register', cycles, register_x)
    return signal_strenght

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 12560)
