# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 21 excercise 2 https://adventofcode.com/2022/day/21


import adv_common as common
import day_21_1
from sympy import solve

def get_monkey_expr(monkey, monkey_dict):
    if monkey_dict[monkey].isnumeric():
        return monkey if monkey == 'humn' else monkey_dict[monkey]
    else:
        monkey1, operation, monkey2 = monkey_dict[monkey].split()
        monkey_dict[monkey1] = get_monkey_expr(monkey1, monkey_dict)
        monkey_dict[monkey2] = get_monkey_expr(monkey2, monkey_dict)
        if monkey == 'root':
            # Assume root operation will always be sum
            operation = '-'
        return '(' + monkey_dict[monkey1] + operation + monkey_dict[monkey2] + ')'

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    monkey_dict = day_21_1.generate_monkey_dict(contents)
    return solve(get_monkey_expr('root', monkey_dict))[0]

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 3330805295850)
