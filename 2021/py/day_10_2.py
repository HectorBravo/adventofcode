# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 10 excercise 2 https://adventofcode.com/2021/day/10


import adv_common as common
from statistics import median

matches = {'<': '>', '{': '}', '[': ']', '(': ')'}
scores = {'>': 4, '}': 3, ']': 2, ')': 1}

def get_incomplete_line(line):
    i = 0
    while i < len(line):
        sign = line[i]
        if sign in matches:
            i+=1
        else:
            if matches[line[i-1]] == sign:
                line = line[:i-1] + line[i+1:]
                i-=1
            else:
                return ''
    return line

def calc_completion_score(line):
    score = 0
    for i in line:
        score = score * 5 + scores[matches[i]]
    return score

def calc_completion_sum(input):
    completion_score = []
    for line in input:
        remaining_line = get_incomplete_line(line)
        if remaining_line != '':
            completion_score.append(calc_completion_score(remaining_line[::-1]))
    return median(completion_score)

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    return calc_completion_sum(contents)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 2768166558)
