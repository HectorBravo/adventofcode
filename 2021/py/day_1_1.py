# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2021/day/1

import adv_common as common

@common.elapsed_time_factory()
def process_contents(_contents):
    # print(_contents)
    _result = 0
    previous = _contents[0]
    for current in _contents:
        if current > previous:
            _result += 1
        previous = current
    return _result

@common.elapsed_time_factory()
def process_contents2(_contents):
    # print(_contents)
    return len([_contents[i:i+2] for i in range(0, len(_contents) - 1) if _contents[i+1] > _contents[i]])

if __name__ == "__main__":
    contents = common.read_input('int')
    result = process_contents(contents)
    common.print_result(result, 1342)
    result = process_contents2(contents)
    common.print_result(result, 1342)