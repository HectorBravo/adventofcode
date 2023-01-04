# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 13 excercise 1 https://adventofcode.com/2021/day/13


import adv_common as common

def get_dot_number(dots, folds):
    for coord, fold_str in folds:
        fold = int(fold_str)
        for i, dot in enumerate(dots):
            if coord == 'y' and dot.imag > fold:
                dots[i] = dot.real + (fold - (dot.imag - fold))*1j
            elif coord == 'x' and dot.real > fold:
                dots[i] = fold - (dot.real - fold) + dot.imag*1j
    common.draw_positions(dots, empty_char=' ')
    return 0

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    dots = [int(line.split(',')[0]) + int(line.split(',')[1])*1j for line in contents[0]]
    folds = [tuple(line.split()[-1].split('=')) for line in contents[1]]
    return get_dot_number(dots, folds)

if __name__ == "__main__":
    contents = common.read_input(data_type = "struct_list")
    result = process_solution(contents)
    common.print_result(result, 'CJCKBAPB')
