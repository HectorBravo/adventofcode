# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 21 excercise 1 https://adventofcode.com/2022/day/21


import adv_common as common

def generate_monkey_dict(_contents):
    monkey_dict = {}
    for line in _contents:
        monkey_dict[line.split(':')[0]] = line.split(':')[1].lstrip()
    return monkey_dict

def get_monkey_expr(_monkey, _monkey_dict):
    if _monkey_dict[_monkey].isnumeric():
        return _monkey_dict[_monkey]
    else:
        monkey1, operation, monkey2 = _monkey_dict[_monkey].split()
        _monkey_dict[monkey1] = get_monkey_expr(monkey1, _monkey_dict)
        _monkey_dict[monkey2] = get_monkey_expr(monkey2, _monkey_dict)
        return '(' + _monkey_dict[monkey1] + operation + _monkey_dict[monkey2] + ')'

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    monkey_dict = generate_monkey_dict(_contents)
    return int(eval(get_monkey_expr('root', monkey_dict)))

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 145167969204648)
