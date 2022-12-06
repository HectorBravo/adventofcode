# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2022/day/1

import adv2022_common as common
import numpy as np

def get_max_calories_list(current_list, calories):
    new_max_list = [*current_list]
    new_max_list.append(calories)
    new_max_list.sort(reverse = True)
    return new_max_list[:3]

def get_max_calories(calories_array):
    max_calories_list = []
    current_calories = 0
    for line, calories in enumerate(calories_array):
        if calories == '':
            max_calories_list = get_max_calories_list(max_calories_list, current_calories)
            current_calories = 0
        elif line == (len(calories_array) - 1):
            current_calories += int(calories)
            max_calories_list = get_max_calories_list(max_calories_list, current_calories)
        else:
            current_calories += int(calories)
    return sum(max_calories_list)

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    calories_array = np.array(contents)
    return get_max_calories(calories_array)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 208191)
