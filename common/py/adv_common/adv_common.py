# Copyright Hector Bravo <hbravo@cuic.net>
# Common functions for https://adventofcode.com

import sys
import os
import time
import shutil
import collections
from colorama import Fore, Back, Style
import numpy as np

script_name = os.path.basename(sys.argv[0])
dir_name = os.path.dirname(sys.argv[0])
input_file = script_name.split('.')[0][:-2] + '_input.txt'

def read_input(data_type = 'str', separator = '\n', struct_list_separator = '\n\n'):
    print(Fore.GREEN + 'Input file:' + Style.BRIGHT, input_file, Style.RESET_ALL)
    with open(dir_name + '\\' + input_file, "r", encoding="utf-8") as f:
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
    current_script_name = os.path.basename(sys.argv[0])
    current_file = current_script_name.split('.')[0].split('_')
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
        shutil.copy(dir_name + '\\' + current_script_name, dir_name + '\\' + new_day_file)
    if new_input_file and (not os.path.exists(dir_name + '\\' + new_input_file)):
        print(Fore.RED + 'Created new input file' + Style.BRIGHT, dir_name + '\\' + new_input_file, Style.RESET_ALL)
        with open(dir_name + '\\' + new_input_file, 'w', encoding="utf-8") as f:
            pass

def print_result(_result, _expected_result = None):
    print(Fore.GREEN + 'Result is:' + Style.BRIGHT, _result, Style.RESET_ALL)
    if _expected_result:
        assert _result == _expected_result
        gen_next_files()

def str_list_to_int_lst(_str_list):
    return list(map(int, _str_list))

def gen_point_list(_vector):
    # print('_vector:', _vector)
    x0 = _vector[0]
    y0 = _vector[1]
    x1 = _vector[2]
    y1 = _vector[3]

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

def elapsed_time_factory(_print_args = False):
    def elapsed_time_decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.time()
            result = func(*args, **kwargs)
            end_time = time.time()
            if _print_args:
                print('Time consumed by function ' + Fore.CYAN + func.__name__ + ' (' + Fore.WHITE + str(args) + Fore.CYAN + ')' + Style.RESET_ALL + ' was ' + Style.BRIGHT + str(end_time - start_time) + Style.RESET_ALL + ' seconds')
            else:
                print('Time consumed by function ' + Fore.CYAN + func.__name__ + Style.RESET_ALL + ' was ' + Style.BRIGHT + str(end_time - start_time) + Style.RESET_ALL + ' seconds')
            return result
        return wrapper
    return elapsed_time_decorator

def get_neighbour_positions(_position:complex, _min_x_y:complex, _max_x_y:complex, _include_diagonals = False):
    neighbours = {_position + 1, _position -1, _position +1j, _position -1j}
    if _include_diagonals:
        neighbours |= {_position + (1+1j), _position + (-1+1j), _position + (1-1j), _position + (-1-1j)}
    filtered_neigbours = set(filter(lambda number: number.real >= _min_x_y.real and number.real <= _max_x_y.real and
                                                            number.imag >= _min_x_y.imag and number.imag <= _max_x_y.imag,
                                                            neighbours))
    return filtered_neigbours

def draw_path(_array, _path, _fill_sequence):
    i = 0
    for position in _path:
        _array[int(position.imag)][int(position.real)] = _fill_sequence[i]
        i  = (i + 1) % len(_fill_sequence)
    for line in _array:
        print("".join(line))

def find_all_paths(_graph, _start, _end, _current_path):
    _current_path += [_start]
    if _start == _end:
        return [_current_path]
    if _start not in _graph:
        return []
    path_list = []
    for node in _graph[_start]:
        if node not in _current_path:
            newpaths = find_all_paths(_graph, node, _end, _current_path)
            for newpath in newpaths:
                path_list.append(newpath)
    return path_list

# Breadth first implementation
def find_shortest_path_bfs(_graph, _start, _end):
    dist = {_start: [_start]}
    q = collections.deque([_start])
    while len(q):
        at = q.popleft()
        for next_graph in _graph[at]:
            if next_graph not in dist:
                dist[next_graph] = dist[at]+[next_graph]
                q.append(next_graph)
    return dist.get(_end)

def draw_positions(_positions, _fill_char = '#', _empty_char = '.'):
    max_x = max(set(int(position.real) for position in _positions))
    min_x = min(set(int(position.real) for position in _positions))
    max_y = max(set(int(position.imag) for position in _positions))
    min_y = min(set(int(position.imag) for position in _positions))
    # print(max_x, min_x, max_y, min_y)
    # print(_positions)
    array = np.full((max_y - min_y + 1, max_x - min_x + 1), _empty_char)
    for position in _positions:
        array[abs(min_y) + int(position.imag)][abs(min_x) + int(position.real)] = _fill_char
    # print(array)
    for i in range(max_y - min_y + 1):
        print("".join(array[i]))
