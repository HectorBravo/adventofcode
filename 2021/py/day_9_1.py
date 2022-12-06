# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 1 https://adventofcode.com/2021/day/9

import sys
sys.path.append('../../common/py')
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

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    lava_matrix = np.array(contents)
    return sum_risk_level(lava_matrix)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 506)
