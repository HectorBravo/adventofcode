# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 21 excercise 1 https://adventofcode.com/2022/day/21


import adv_common as common

def generate_monkey_dict(contents):
    monkey_dict = {}
    for line in contents:
        monkey_dict[line.split(':')[0]] = line.split(':')[1].lstrip()
    return monkey_dict

def get_monkey_expr(monkey, monkey_dict):
    if monkey_dict[monkey].isnumeric():
        return monkey_dict[monkey]
    else:
        monkey1, operation, monkey2 = monkey_dict[monkey].split()
        monkey_dict[monkey1] = get_monkey_expr(monkey1, monkey_dict)
        monkey_dict[monkey2] = get_monkey_expr(monkey2, monkey_dict)
        return '(' + monkey_dict[monkey1] + operation + monkey_dict[monkey2] + ')'

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    monkey_dict = generate_monkey_dict(contents)
    return int(eval(get_monkey_expr('root', monkey_dict)))

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 145167969204648)
