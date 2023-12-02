# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2021/day/3

import adv_common as common

def filter_values(_input, _bit, _value):
    return list(filter(lambda x : x[_bit] == str(_value), _input))

def get_most_common_value_at_bit(_input, _bit):
    zeroes = 0
    ones = 0
    for value in _input:
        if value[_bit] == '0':
            zeroes += 1
        elif value[_bit] == '1':
            ones += 1
    if zeroes > ones:
        ret = 0
    else:
        ret = 1
    return ret

def calc_oxigen_rating(_contents):
    oxygen_rating = _contents

    for bit in range(len(oxygen_rating[0])):
        if len(oxygen_rating) == 1:
            break
        most_common_value = get_most_common_value_at_bit(oxygen_rating, bit)
        oxygen_rating = filter_values(oxygen_rating, bit, most_common_value)
    return int(oxygen_rating[0], 2)

def calc_CO2_rating(_contents):
    CO2_rating = _contents

    for bit in range(len(CO2_rating[0])):
        if len(CO2_rating) == 1:
            break
        least_common_value = int(not get_most_common_value_at_bit(CO2_rating, bit))
        CO2_rating = filter_values(CO2_rating, bit, least_common_value)
    return int(CO2_rating[0], 2)

@common.elapsed_time_factory()
def process_contents(_contents):
    # print('Contents:', _contents)
    oxygen_rating = calc_oxigen_rating(_contents)
    CO2_rating = calc_CO2_rating(_contents)
    return oxygen_rating * CO2_rating

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 482500)
