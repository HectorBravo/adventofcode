# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2022/day/1

import adv2022_common as common
import time
import numpy as np

def get_max_calories(calories_array):
    max_calories = 0
    current_calories = 0
    for line in range(len(calories_array)):
        if calories_array[line] == '':
            if current_calories > max_calories:
                max_calories = current_calories
            current_calories = 0
        elif line == (len(calories_array) - 1):
            current_calories += int(calories_array[line])
            if current_calories > max_calories:
                max_calories = current_calories
        else:
            current_calories += int(calories_array[line])
    return max_calories

def process_solution(contents):
    # print('Contents:', contents)
    calories_array = np.array(contents)
    return get_max_calories(calories_array)

if __name__ == "__main__":
    contents = common.read_input()
    start_time = time.time()
    result = process_solution(contents)
    common.print_result(result, 71502)
    print("--- %s seconds ---" % (time.time() - start_time))
