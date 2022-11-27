# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 2 https://adventofcode.com/2021/day/5

import adv2021_common as common
import day_5_1
import numpy as np

def process_solution(contents):
    coordinates_list = day_5_1.get_coordinates(contents)
    rows_num, cols_num = day_5_1.calc_rows_and_cols(coordinates_list)
    vents_matrix = np.zeros((rows_num, cols_num), dtype = int)
    vents_matrix = day_5_1.mark_coordinates(coordinates_list, vents_matrix)
    # print(vents_matrix)
    danger_rating = 2
    result = day_5_1.count_dangerous_areas(vents_matrix, danger_rating)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 15463)
