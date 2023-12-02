# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 11 excercise 1 https://adventofcode.com/2022/day/11


import adv_common as common

ROUNDS = 20

def print_worry_levels_and_inspections(_round, _monkeys):
    print('Round', _round + 1)
    for _id, monkey in enumerate(_monkeys):
        print('Monkey', _id, 'items', monkey['items'], 'inspected', monkey['inspected'])

def process_rounds(_monkeys, _rounds):
    for _round in range(_rounds):
        for _id, monkey in enumerate(_monkeys):
            for old in monkey['items']:
                new_value = eval(monkey['operation'])//3
                if new_value % monkey['test'] == 0:
                    _monkeys[monkey['true']]['items'].append(new_value)
                else:
                    _monkeys[monkey['false']]['items'].append(new_value)
                _monkeys[_id]['inspected'] += 1
            _monkeys[_id]['items'] = []
        # print_worry_levels_and_inspections(_round, _monkeys)

def get_monkey_dict(_contents):
    monkeys = []
    for data in _contents:
        details = {}
        details['items'] = list(map(int, data[1].split(':')[1].split(',')))
        details['operation'] = data[2].split('=')[1][1:]
        details['test'] = int(data[3].split()[-1])
        details['true'] = int(data[4].split()[-1])
        details['false'] = int(data[5].split()[-1])
        details['inspected'] = 0
        monkeys.append(details)
    return monkeys

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    monkeys = get_monkey_dict(_contents)
    process_rounds(monkeys, ROUNDS)
    inspections = [monkey['inspected'] for monkey in monkeys]
    inspections.sort()
    return inspections[-1]*inspections[-2]

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 67830)
