# Copyright Hector Bravo <hbravo@cuic.net>
# Common functions for https://adventofcode.com

import sys
import os
import time
import shutil
from colorama import Fore, Back, Style

script_name = os.path.basename(sys.argv[0])
dir_name = os.path.dirname(sys.argv[0])
input_file = script_name.split('.')[0][:-2] + '_input.txt'

def read_input(data_type = 'str', separator = '\n', struct_list_separator = '\n\n'):
    print(Fore.GREEN + 'Input file:' + Style.BRIGHT, input_file, Style.RESET_ALL)
    with open(dir_name + '\\' + input_file, "r") as f:
        if data_type == 'int':
            contents = list(map(int, f))
        elif data_type == 'int_list':
            contents = list(map(int, f.read().split(separator)))
        elif data_type == 'char_list':
            lines = f.read().splitlines()
            contents = [[c for c in lines[i]] for i in range(len(lines))]
        elif data_type == 'struct_list':
            structs = f.read().split(struct_list_separator)
            contents = [struct.split(separator) for struct in structs]
        else:
            contents = f.read().split(separator)
    return tuple(contents)

def gen_next_files():
    script_name = os.path.basename(sys.argv[0])
    current_file = script_name.split('.')[0].split('_')
    new_day_file = [*current_file]
    new_input_file = []
    if current_file[2] == '2':
        new_day_file[1] = str(int(new_day_file[1]) + 1)
        new_day_file[2] = '1.py'
        new_input_file = [*new_day_file][0:2] + ['input.txt']
    else:
        new_day_file[2] = '2.py'
    new_day_file = '_'.join(new_day_file)
    new_input_file = '_'.join(new_input_file)
    if not os.path.exists(dir_name + '\\' + new_day_file):
        print(Fore.RED + 'Created new day file' + Style.BRIGHT, dir_name + '\\' + new_day_file, Style.RESET_ALL)
        shutil.copy(dir_name + '\\' + script_name, dir_name + '\\' + new_day_file)
    if new_input_file and (not os.path.exists(dir_name + '\\' + new_input_file)):
        print(Fore.RED + 'Created new input file' + Style.BRIGHT, dir_name + '\\' + new_input_file, Style.RESET_ALL)
        with open(dir_name + '\\' + new_input_file, 'w') as f:
            pass

def print_result(result, expected_result = None):
    print(Fore.GREEN + 'Result is:' + Style.BRIGHT, result, Style.RESET_ALL)
    if expected_result:
        assert(result == expected_result)
        gen_next_files()

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

def elapsed_time_factory(print_args = False):
    def elapsed_time_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if print_args:
                print('Time consumed by function ' + Fore.CYAN + func.__name__ + ' (' + Fore.WHITE + str(args) + Fore.CYAN + ')' + Style.RESET_ALL + ' was ' + Style.BRIGHT + str(end_time - start_time) + Style.RESET_ALL + ' seconds')
            else:
                print('Time consumed by function ' + Fore.CYAN + func.__name__ + Style.RESET_ALL + ' was ' + Style.BRIGHT + str(end_time - start_time) + Style.RESET_ALL + ' seconds')
            return result
        return wrapper
    return elapsed_time_decorator

def get_neighbour_positions(position:complex, min_x_y:complex, max_x_y:complex, include_diagonals = False):
    neighbours = {position + 1, position -1, position +1j, position -1j}
    if include_diagonals:
        neighbours |= {position + (1+1j), position + (-1+1j), position + (1-1j), position + (-1-1j)}
    filtered_neigbours = set(filter(lambda number: number.real >= min_x_y.real and number.real <= max_x_y.real and
                                                            number.imag >= min_x_y.imag and number.imag <= max_x_y.imag,
                                                            neighbours))
    return filtered_neigbours