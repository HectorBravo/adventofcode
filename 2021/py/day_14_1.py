# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 14 excercise 1 https://adventofcode.com/2021/day/14


import adv_common as common
import collections as cl

ITERATIONS = 10

def process_pairs(_pairs, _rules, _iterations):
    for _ in range(_iterations):
        _new_pairs = cl.Counter()
        for (first, last), num in _pairs.items():
            middle = _rules[(first, last)]
            _new_pairs[first + middle] += num
            _new_pairs[middle + last] += num
        _pairs = _new_pairs
    return _pairs

def calc_most_common_minus_less_common(_polymer, _ruleset, _iterations):
    pairs = cl.Counter(
        _polymer[i:i+2] for i in range(len(_polymer) - 1)
    )
    rules = {
        tuple(rule.split(' -> ')[0]):rule.split(' -> ')[1] for rule in _ruleset
    }
    pairs = process_pairs(pairs, rules, _iterations)
    elements = cl.Counter()
    for (first, _), num in pairs.items():
        elements[first] += num
    elements[_polymer[-1]] += 1
    return max(elements.values()) - min(elements.values())

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    return calc_most_common_minus_less_common(_contents[0][0], _contents[1], ITERATIONS)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 4517)
