# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 8 excercise 2 https://adventofcode.com/2021/day/8

import adv_common as common

def get_decoded_number(_decoded_numbers, _number):
    return list(_decoded_numbers.keys())[list(_decoded_numbers.values()).index(_number)]

def get_decoded_sum(_contents):
    # print('Contents:', _contents)
    _result = 0
    for line in _contents:
        left, right = line.split('|')
        encoded_numbers = list([frozenset(a) for a in list(num for num in (left + right).split())])
        known_numbers = {}
        known_numbers[1] = set(list(filter(lambda x : len(x) == 2, encoded_numbers))[0])
        known_numbers[7] = set(list(filter(lambda x : len(x) == 3, encoded_numbers))[0])
        known_numbers[4] = set(list(filter(lambda x : len(x) == 4, encoded_numbers))[0])
        known_numbers[8] = set(list(filter(lambda x : len(x) == 7, encoded_numbers))[0])
        len_5 = set(list(filter(lambda x : len(x) == 5, encoded_numbers)))
        len_6 = set(list(filter(lambda x : len(x) == 6, encoded_numbers)))
        # print(encoded_numbers)
        segments = {}
        """
        segment locations:
         0000
        1    5
        1    5
         6666
        2    4
        2    4
         3333
        """
        segments[0] = known_numbers[7] - known_numbers[1]
        segments[6] = known_numbers[4].copy()
        for aux in len_5:
            segments[6] &= aux
        known_numbers[0] = known_numbers[8] - segments[6]
        segments[1] = known_numbers[0] & known_numbers[4] - known_numbers[1]
        segments[3] = known_numbers[0] - segments[0]
        for aux in len_5:
            segments[3] &= aux
        segments[4] = known_numbers[1].copy()
        for aux in len_6:
            if aux != known_numbers[0]:
                segments[4] &= aux
        segments[5] = known_numbers[1] - segments[4]
        segments[2] = known_numbers[0] - known_numbers[4] - segments[0] - segments[3]
        known_numbers[9] = known_numbers[8] - segments[2]
        known_numbers[6] = known_numbers[8] - segments[5]
        known_numbers[5] = known_numbers[8] - segments[5] - segments[2]
        known_numbers[3] = known_numbers[8] - segments[1] - segments[2]
        known_numbers[2] = known_numbers[8] - segments[1] - segments[4]
        # print(segments)
        i = 1
        for number in encoded_numbers[:-5:-1]:
            _result += (get_decoded_number(known_numbers, number) * i)
            i *= 10
    return _result

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    return get_decoded_sum(_contents)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 1055164)
