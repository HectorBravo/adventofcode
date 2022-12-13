# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 1 https://adventofcode.com/2022/day/9

import adv_common as common

def gen_positions(contents):
    pending_moves = [(x[0], int(x[1])) for x in [content.split() for content in contents]]
    # print(pending_moves)
    next = 0+0j
    head = 0+0j
    tail = 0+0j
    tail_positions = {tail}
    for direction, increment in pending_moves:
        for _ in range(increment):
            next = head + {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}[direction]
            # print(direction, increment, '- H', head, '->', next, 'T', tail)
            if abs(tail - next) >= 2:
                tail = head
                tail_positions.add(tail)
                # print('adding', (tail))
            head = next
    return tail_positions

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    positions = gen_positions(contents)
    return len(positions)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 6018)
