# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2022/day/1

import adv_common as common
import numpy as np

def get_max_calories(calories_array):
    max_calories = 0
    current_calories = 0
    for line, calories in enumerate(calories_array):
        if calories == '':
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        elif line == (len(calories_array) - 1):
            current_calories += int(calories)
            if current_calories > max_calories:
                max_calories = current_calories
        else:
            current_calories += int(calories)
    return max_calories

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    calories_array = np.array(contents)
    return get_max_calories(calories_array)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 71502)
