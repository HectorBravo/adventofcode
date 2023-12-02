# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 10 excercise 1 https://adventofcode.com/2021/day/10


import adv_common as common

matches = {'<': '>', '{': '}', '[': ']', '(': ')'}
scores = {'>': 25137, '}': 1197, ']': 57, ')': 3}

def calc_corrupt_score(_line):
    i = 0
    while i < len(_line):
        sign = _line[i]
        if sign in matches:
            i+=1
        else:
            if matches[_line[i-1]] == sign:
                _line = _line[:i-1] + _line[i+1:]
                i-=1
            else:
                return scores[sign]
    return 0

def calc_corrupt_sum(_input):
    corrupt_score = 0
    for line in _input:
        corrupt_score += calc_corrupt_score(line)
    return corrupt_score

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    return calc_corrupt_sum(_contents)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 290691)
