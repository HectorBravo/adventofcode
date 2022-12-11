# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 3 excercise 1 https://adventofcode.com/2021/day/3

import adv_common as common

def filter_values(input, bit, value):
    return list(filter(lambda x : x[bit] == str(value), input))

def get_most_common_value_at_bit(input, bit):
    zeroes = 0
    ones = 0
    for value in input:
        if value[bit] == '0':
            zeroes += 1
        elif value[bit] == '1':
            ones += 1
    if zeroes > ones:
        ret = 0
    else:
        ret = 1
    return ret

def calc_oxigen_rating(contents):
    oxygen_rating = contents

    for bit in range(len(oxygen_rating[0])):
        if len(oxygen_rating) == 1:
            break
        most_common_value = get_most_common_value_at_bit(oxygen_rating, bit)
        oxygen_rating = filter_values(oxygen_rating, bit, most_common_value)
    return int(oxygen_rating[0], 2)

def calc_CO2_rating(contents):
    CO2_rating = contents

    for bit in range(len(CO2_rating[0])):
        if len(CO2_rating) == 1:
            break
        least_common_value = int(not get_most_common_value_at_bit(CO2_rating, bit))
        CO2_rating = filter_values(CO2_rating, bit, least_common_value)
    return int(CO2_rating[0], 2)

@common.elapsed_time_factory()
def process_contents(contents):
    # print('Contents:', contents)
    oxygen_rating = calc_oxigen_rating(contents)
    CO2_rating = calc_CO2_rating(contents)
    result = oxygen_rating * CO2_rating
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 482500)
