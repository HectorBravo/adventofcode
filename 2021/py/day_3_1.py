# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2021/day/3

import adv_common as common

def calc_gamma(zeroes, ones):
    value = ''
    for i, _ in enumerate(zeroes):
        if zeroes[i] > ones[i]:
            value += '0'
        else:
            value += '1'
    return int(value, 2)

def calc_epsilon(zeroes, ones):
    value = ''
    for i, _ in enumerate(zeroes):
        if zeroes[i] > ones[i]:
            value += '1'
        else:
            value += '0'
    return int(value, 2)

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    zeroes = [0] * len(_contents[0])
    ones = [0] * len(_contents[0])
    for position in _contents:
        for bit, _ in enumerate(position):
            if position[bit] == '0':
                zeroes[bit] += 1
            elif position[bit] == '1':
                ones[bit] += 1

    gamma = calc_gamma(zeroes, ones)
    epsilon = calc_epsilon(zeroes, ones)
    return gamma * epsilon

@common.elapsed_time_factory()
def process_contents2(_contents):
    # print(_contents)
    gamma = []
    epsilon = []
    for bit in range(len(_contents[0])):
        ones = len([i[bit] for i in _contents if i[bit] == '1'])
        zeroes = len([i[bit] for i in _contents if i[bit] == '0'])
        gamma += ['1' if ones > zeroes else '0']
        epsilon += ['0' if ones > zeroes else '1']
    return int("".join(gamma), 2) * int("".join(epsilon), 2)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 1307354)
    result = process_contents2(contents)
    common.print_result(result, 1307354)
