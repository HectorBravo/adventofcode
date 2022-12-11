# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 2 https://adventofcode.com/2021/day/5

import adv_common as common
import day_5_1
import numpy as np

def gen_coord_dict(coordinate_list):
    coords_dict = {}
    for vector in coordinate_list:
        points = common.gen_point_list(vector)
        # print(points)
        for point in points:
            if point in coords_dict:
                coords_dict[point] += 1
            else:
                coords_dict[point] = 1
    return coords_dict

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    coordinates_list = day_5_1.get_coordinates(contents)
    rows_num, cols_num = day_5_1.calc_rows_and_cols(coordinates_list)
    vents_matrix = np.zeros((rows_num, cols_num), dtype = int)
    vents_matrix = day_5_1.mark_coordinates(coordinates_list, vents_matrix)
    # print(vents_matrix)
    danger_rating = 2
    result = day_5_1.count_dangerous_areas(vents_matrix, danger_rating)
    return result

@common.elapsed_time_factory()
def process_solution2(contents):
    # print('Contents:', contents)
    coordinates_list = day_5_1.get_coordinates(contents)
    vents_dict = gen_coord_dict(coordinates_list)
    # print(vents_dict)
    danger_rating = 2
    values = len(dict(filter(lambda x : x[1] >= danger_rating, vents_dict.items())))
    return values

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 15463)
    result = process_solution2(contents)
    common.print_result(result, 15463)
