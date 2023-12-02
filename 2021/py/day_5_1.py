# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 1 https://adventofcode.com/2021/day/5

import adv_common as common
import numpy as np

def calc_rows_and_cols(_contents):
    max_cols = _contents.max(axis = 0)[0:3:2].max() + 1
    max_rows = _contents.max(axis = 0)[1:4:2].max() + 1
    return max_rows, max_cols

def get_coordinates(_contents):
    coordinates_list = []
    for line in _contents:
        line_tuple = line.split()
        elems = common.str_list_to_int_lst(line_tuple[0].split(',') + line_tuple[2].split(','))
        # print('matching:', elems)
        coordinates_list.append(elems)
    return np.array(coordinates_list)

def mark_coordinates(_coordinates_list, _vents_matrix):
    # print('_vents_matrix\n', _vents_matrix)
    for vector in _coordinates_list:
        point_list = common.gen_point_list(vector)
        # print(point_list)
        for point in point_list:
            _vents_matrix[point[1]][point[0]] += 1
    return _vents_matrix

def count_dangerous_areas(_array, _rating):
    filter_array = _array >= _rating
    return len(_array[filter_array])

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    coordinates_list = get_coordinates(_contents)
    filtered_coordinates = np.array([x for x in coordinates_list if x[0] == x[2] or x[1] == x[3]])
    rows_num, cols_num = calc_rows_and_cols(filtered_coordinates)
    vents_matrix = np.zeros((rows_num, cols_num), dtype = int)
    vents_matrix = mark_coordinates(filtered_coordinates, vents_matrix)
    # print(vents_matrix)
    danger_rating = 2
    _result = count_dangerous_areas(vents_matrix, danger_rating)
    return _result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 5698)
