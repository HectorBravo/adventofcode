# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 6 excercise 1 https://adventofcode.com/2022/day/6

import adv2022_common as common

def get_first_diff_sequence(input, characters):
    for i in range(len(input)):
        if len(set(input[i:i+characters])) == characters:
            break
    return i + characters

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    characters = 4
    return get_first_diff_sequence(contents[0], characters)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 1142)
