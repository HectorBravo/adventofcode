# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 11 excercise 2 https://adventofcode.com/2022/day/11


import adv_common as common
import day_11_1

ROUNDS = 10000

def process_rounds(monkeys, lcm, rounds):
    for round in range(rounds):
        for id, monkey in enumerate(monkeys):
            for old in monkey['items']:
                new_value = eval(monkey['operation']) % lcm
                if new_value % monkey['test'] == 0:
                    monkeys[monkey['true']]['items'].append(new_value)
                else:
                    monkeys[monkey['false']]['items'].append(new_value)
                monkeys[id]['inspected'] += 1
            monkeys[id]['items'] = []
        # day_11_1.print_worry_levels_and_inspections(round, monkeys)

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    monkeys = day_11_1.get_monkey_dict(contents)
    lcm = 1
    for monkey in monkeys:
        lcm *= monkey['test']
    process_rounds(monkeys, lcm, ROUNDS)
    inspections = [monkey['inspected'] for monkey in monkeys]
    inspections.sort()
    return inspections[-1]*inspections[-2]

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 15305381442)
