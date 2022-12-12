# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 7 excercise 2 https://adventofcode.com/2022/day/7

import adv_common as common
import day_7_1

FILESYSTEM_SPACE = 70000000
UPDATE_SPACE_NEEDED = 30000000

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    directory_tree = day_7_1.gen_directory_tree(contents)
    # print(directory_tree)
    available_space = FILESYSTEM_SPACE - directory_tree['.']
    needed_space = UPDATE_SPACE_NEEDED - available_space
    print(available_space, needed_space)
    return min([v for _, v in directory_tree.items() if v > needed_space])

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2481982)
