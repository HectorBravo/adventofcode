# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 8 excercise 2 https://adventofcode.com/2022/day/8

import sys
sys.path.append('../../common/py')
import adv_common as common
import numpy as np

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    tree_matrix = np.array(contents)
    # print(tree_matrix)
    max_scenic_score = 0
    for x in range(0, len(tree_matrix[0]) - 1):
        for y in range(0, len(tree_matrix) - 1):
            trees = []
            elem = tree_matrix[y][x]
            # print('x y elem', x, y, elem)
            left = tree_matrix[y][:x][::-1]
            right = tree_matrix[y][x + 1:]
            top = tree_matrix[:y,x:x+1][::-1]
            bottom = tree_matrix[y+1:,x:x+1]
            trees.append(list(left))
            trees.append(list(right))
            trees.append(list(top.reshape((1, len(top)))[0]))
            trees.append(list(bottom.reshape((1, len(bottom)))[0]))
            # print(trees)
            count_list = [0 for _ in range(len(trees))]
            for i, sight_line in enumerate(trees):
                for tree_height in sight_line:
                    count_list[i] += 1
                    if tree_height >= elem:
                        break
            current_count = np.prod(count_list)
            # print(count_list, current_count)
            if current_count > max_scenic_score:
                max_scenic_score = current_count
    return max_scenic_score

if __name__ == "__main__":
    contents = common.read_input(data_type = 'char_list')
    result = process_solution(contents)
    common.print_result(result, 313200)
