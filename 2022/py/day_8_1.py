# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 8 excercise 1 https://adventofcode.com/2022/day/8

import adv_common as common
import numpy as np

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    tree_matrix = np.array(contents)
    # print(tree_matrix)
    count = (len(tree_matrix) * 2) + (len(tree_matrix[0]) - 2) * 2
    for x in range(1, len(tree_matrix[0]) - 1):
        for y in range(1, len(tree_matrix) - 1):
            elem = tree_matrix[y][x]
            left = tree_matrix[y][:x]
            right = tree_matrix[y][x + 1:]
            top = tree_matrix[:y,x:x+1]
            bottom = tree_matrix[y+1:,x:x+1]
            if elem > max(left) or elem > max(right) or elem > max(top) or elem > max(bottom):
                # print('lower element elem', elem, 'at x y', x, y)
                count +=1
    return count

if __name__ == "__main__":
    contents = common.read_input(data_type = 'char_list')
    result = process_solution(contents)
    common.print_result(result, 1676)
