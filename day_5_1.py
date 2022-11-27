# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 5 excercise 1 https://adventofcode.com/2021/day/5

import adv2021_common as common
import numpy as np

def filter_elems(contents):
    filtered_elems = []
    output_cols = 0
    output_rows = 0
    for line in contents:
        line_tuple = line.split()
        elems = common.str_list_to_int_lst(line_tuple[0].split(',') + line_tuple[2].split(','))
        if (elems[0] == elems[2]) or (elems[1] == elems[3]):
            # print('matching:', elems)
            max_cols = max(elems[0], elems[2])
            max_rows = max(elems[1], elems[3])
            if max_cols > output_cols:
                output_cols = max_cols
            if max_rows > output_rows:
                output_rows = max_rows
            filtered_elems.append(elems)
    return np.array(filtered_elems), output_rows + 1, output_cols + 1

def gen_vents_matrix(filtered_elems, rows_num, cols_num):
    vents_matrix = np.zeros((rows_num, cols_num), dtype = int)
    for elem in filtered_elems:
        # print('processing:', elem)
        if elem[0] == elem[2]:
            col = elem[0]
            start = min(elem[1], elem[3])
            end = max(elem[1], elem[3]) + 1
            for i in range(start, end):
                vents_matrix[i][col] += 1
        else:
            row = elem[1]
            start = min(elem[0], elem[2])
            end = max(elem[0], elem[2]) + 1
            for i in range(start, end):
                vents_matrix[row][i] += 1
    return vents_matrix

def count_dangerous_areas(array, rating):
    filter_array = (array >= rating)
    return len(array[filter_array])

def process_contents(contents):
    # print('Contents:', contents)
    filtered_elems, rows_num, cols_num = filter_elems(contents)
    vents_matrix = gen_vents_matrix(filtered_elems, rows_num, cols_num)
    # print(vents_matrix)
    danger_rating = 2
    result = count_dangerous_areas(vents_matrix, danger_rating)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 5698)
