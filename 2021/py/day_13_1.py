# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 13 excercise 1 https://adventofcode.com/2021/day/13


import adv_common as common

def get_dot_number(_dots, _folds):
    for coord, fold_str in _folds:
        fold = int(fold_str)
        for i, dot in enumerate(_dots):
            if coord == 'y' and dot.imag > fold:
                _dots[i] = dot.real + (fold - (dot.imag - fold))*1j
            elif coord == 'x' and dot.real > fold:
                _dots[i] = fold - (dot.real - fold) + dot.imag*1j
    return len(set(_dots))

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    dots = [int(line.split(',')[0]) + int(line.split(',')[1])*1j for line in _contents[0]]
    folds = [tuple(line.split()[-1].split('=')) for line in _contents[1]]
    return get_dot_number(dots, [folds[0]])

if __name__ == "__main__":
    contents = common.read_input(data_type = "struct_list")
    result = process_solution(contents)
    common.print_result(result, 638)
