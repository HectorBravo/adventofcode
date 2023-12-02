# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 2 https://adventofcode.com/2021/day/9


import adv_common as common
import numpy as np
import day_9_1

def get_basin_elems(_lava_dict, _position, _min_x_y, _max_x_y, _processed_matrix):
    # print('_position', _position, 'neighbours', common.get_neighbour_positions(_position, _min_x_y, _max_x_y))
    filtered_neighbour_positions = [_position]
    _processed_matrix[int(_position.imag)][int(_position.real)] = 1
    for neighbour in common.get_neighbour_positions(_position, _min_x_y, _max_x_y):
        if _processed_matrix[int(neighbour.imag)][int(neighbour.real)] != 1 and _lava_dict[neighbour] != 9:
            filtered_neighbour_positions += get_basin_elems(_lava_dict, neighbour, _min_x_y, _max_x_y, _processed_matrix)
    return filtered_neighbour_positions

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    min_x_y, max_x_y, lava_dict = day_9_1.gen_lava_dict(_contents)
    processed_matrix = np.full((int(max_x_y.imag + 1), int(max_x_y.real + 1)), int(0))
    basin_sizes = []
    for key, value in lava_dict.items():
        if processed_matrix[int(key.imag)][int(key.real)] != 1 and value != 9:
            basin_sizes.append(len(get_basin_elems(lava_dict, key,  min_x_y, max_x_y, processed_matrix)))
    # print(processed_matrix)
    basin_sizes.sort(reverse = True)
    return basin_sizes[0]*basin_sizes[1]*basin_sizes[2]

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 931200)
