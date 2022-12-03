# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2021/day/3

import adv2021_common as common

def calc_gamma(zeroes, ones):
    value = ''
    for i in range(len(zeroes)):
        if zeroes[i] > ones[i]:
            value += '0'
        else:
            value += '1'
    return int(value, 2)

def calc_epsilon(zeroes, ones):
    value = ''
    for i in range(len(zeroes)):
        if zeroes[i] > ones[i]:
            value += '1'
        else:
            value += '0'
    return int(value, 2)

def process_contents(contents):
    # print(contents)
    zeroes = [0] * len(contents[0])
    ones = [0] * len(contents[0])
    for position in contents:
        for bit in range(len(position)):
            if position[bit] == '0':
                zeroes[bit] += 1
            elif position[bit] == '1':
                ones[bit] += 1

    gamma = calc_gamma(zeroes, ones)
    epsilon = calc_epsilon(zeroes, ones)
    result = gamma * epsilon
    return result

def process_contents2(contents):
    # print(contents)
    gamma = []
    epsilon = []
    for bit in range(len(contents[0])):
        ones = len([i[bit] for i in contents if i[bit] == '1'])
        zeroes = len([i[bit] for i in contents if i[bit] == '0'])
        gamma += ['1' if ones > zeroes else '0']
        epsilon += ['0' if ones > zeroes else '1']
    result = int("".join(gamma), 2) * int("".join(epsilon), 2)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 1307354)
    result = process_contents2(contents)
    common.print_result(result, 1307354)
