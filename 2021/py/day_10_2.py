# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 10 excercise 2 https://adventofcode.com/2021/day/10


import adv_common as common
from statistics import median

matches = {'<': '>', '{': '}', '[': ']', '(': ')'}
scores = {'>': 4, '}': 3, ']': 2, ')': 1}

def get_incomplete_line(_line):
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
                return ''
    return _line

def calc_completion_score(_line):
    score = 0
    for i in _line:
        score = score * 5 + scores[matches[i]]
    return score

def calc_completion_sum(_input):
    completion_score = []
    for line in _input:
        remaining_line = get_incomplete_line(line)
        if remaining_line != '':
            completion_score.append(calc_completion_score(remaining_line[::-1]))
    return median(completion_score)

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    return calc_completion_sum(_contents)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2768166558)
