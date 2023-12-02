# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2022/day/6

import adv_common as common

def get_first_diff_sequence(_input, _characters):
    for i in range(len(_input)):
        if len(set(_input[i:i+_characters])) == _characters:
            break
    return i + _characters

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    characters = 4
    return get_first_diff_sequence(_contents[0], characters)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 1142)
