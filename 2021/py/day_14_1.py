# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 14 excercise 1 https://adventofcode.com/2021/day/14


import adv_common as common
import collections as cl

ITERATIONS = 10

def process_pairs(pairs, rules, iterations):
    for _ in range(iterations):
        _new_pairs = cl.Counter()
        for (first, last), num in pairs.items():
            middle = rules[(first, last)]
            _new_pairs[first + middle] += num
            _new_pairs[middle + last] += num
        pairs = _new_pairs
    return pairs

def calc_most_common_minus_less_common(polymer, ruleset, iterations):
    pairs = cl.Counter(
        polymer[i:i+2] for i in range(len(polymer) - 1)
    )
    rules = {
        tuple(rule.split(' -> ')[0]):rule.split(' -> ')[1] for rule in ruleset
    }
    pairs = process_pairs(pairs, rules, iterations)
    elements = cl.Counter()
    for (first, _), num in pairs.items():
        elements[first] += num
    elements[polymer[-1]] += 1
    return max(elements.values()) - min(elements.values())

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return calc_most_common_minus_less_common(contents[0][0], contents[1], ITERATIONS)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 4517)
