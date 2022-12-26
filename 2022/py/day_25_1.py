# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 25 excercise 1 https://adventofcode.com/2022/day/25


import adv_common as common

snafu_numbers = {'=': -2, '-': -1, '0': 0, '1': 1, '2': 2}

def snafu_to_dec(snafu):
    # print(snafu, len(snafu))
    decimal = 0
    for i, c in enumerate(snafu):
        decimal += ('=-012'.index(c) - 2) * (5 ** (len(snafu) - 1 - i))
    return decimal

def dec_to_snafu(decimal):
    if decimal == 0:
        return ''
    else:
        return dec_to_snafu((decimal + 2) // 5) + '012=-'[decimal % 5]

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    decimal_sum = sum([snafu_to_dec(snafu) for snafu in contents])
    return dec_to_snafu(decimal_sum)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, '2-2=21=0021=-02-1=-0')
