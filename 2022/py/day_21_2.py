# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 21 excercise 2 https://adventofcode.com/2022/day/21


import adv_common as common
import day_21_1
from sympy import solve

def get_monkey_expr(_monkey, _monkey_dict):
    if _monkey_dict[_monkey].isnumeric():
        return _monkey if _monkey == 'humn' else _monkey_dict[_monkey]
    monkey1, operation, monkey2 = _monkey_dict[_monkey].split()
    _monkey_dict[monkey1] = get_monkey_expr(monkey1, _monkey_dict)
    _monkey_dict[monkey2] = get_monkey_expr(monkey2, _monkey_dict)
    if _monkey == 'root':
        # Assume root operation will always be sum
        operation = '-'
    return '(' + _monkey_dict[monkey1] + operation + _monkey_dict[monkey2] + ')'

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    monkey_dict = day_21_1.generate_monkey_dict(_contents)
    return solve(get_monkey_expr('root', monkey_dict))[0]

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 3330805295850)
