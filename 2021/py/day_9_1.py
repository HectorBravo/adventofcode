# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 1 https://adventofcode.com/2021/day/9

import adv_common as common
import numpy as np

def sum_risk_level(array):
    risk_level = 0
    cols_num = len(array[0])
    rows_num = len(array)
    for y in range(rows_num):
        for x in range(cols_num):
            number = int(array[y][x])
            has_top = True
            has_bottom = True
            has_left = True
            has_right = True
            if x == 0:
                has_left = False
            elif x == (cols_num - 1):
                has_right = False
            if y == 0:
                has_top = False
            elif y == (rows_num - 1):
                has_bottom = False
            # print(x, y)
            if ((not has_left or number < int(array[y][x-1])) and
                (not has_right or number < int(array[y][x+1])) and
                (not has_top or number < int(array[y-1][x])) and
                (not has_bottom or number < int(array[y+1][x]))):
                risk_level += (number + 1)
                # print('found:', x, y)
    return risk_level

def gen_lava_dict(input):
    lava_dict = {}
    for y, line in enumerate(input):
        for x, value in enumerate(line):
            lava_dict[x+y*1j] = int(value)
    min_x_y = min(item.real for item in lava_dict.keys()) + min(item.imag for item in lava_dict.keys())*1j
    max_x_y = max(item.real for item in lava_dict.keys()) + max(item.imag for item in lava_dict.keys())*1j
    return min_x_y, max_x_y, lava_dict

def sum_risk_level2(lava_dict, min_x_y, max_x_y):
    risk_level = []
    for key, value in lava_dict.items():
        neighbour_positions = common.get_neighbour_positions(key, min_x_y, max_x_y)
        # print('Pos', key, 'value', value, 'neighbour_positions', neighbour_positions)
        if value < min([lava_dict[neighbour] for neighbour in neighbour_positions]):
            risk_level.append(value + 1)
    # print(risk_level)
    return sum(risk_level)

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    lava_matrix = np.array(contents)
    return sum_risk_level(lava_matrix)

@common.elapsed_time_factory()
def process_solution2(contents):
    # print('Contents:', contents)
    min_x_y, max_x_y, lava_dict = gen_lava_dict(contents)
    # print('lava_dict', lava_dict, 'min_x_y', min_x_y, 'max_x_y', max_x_y)
    return sum_risk_level2(lava_dict, min_x_y, max_x_y)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 506)
    result = process_solution2(contents)
    common.print_result(result, 506)
