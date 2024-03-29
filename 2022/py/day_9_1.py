# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 9 excercise 1 https://adventofcode.com/2022/day/9

import adv_common as common

NUM_SEGMENTS = 2

def print_move(_current, _next, _i):
    if _current != _next:
        print(common.Fore.BLUE, _i if _i > 0 else 'H', common.Style.RESET_ALL, _current, '->', common.Fore.CYAN, _next, common.Style.RESET_ALL)
    else:
        print(common.Fore.BLUE, _i if _i > 0 else 'H', common.Style.RESET_ALL, _current)

def gen_positions(_contents, _num_segments):
    pending_moves = [(x[0], int(x[1])) for x in [content.split() for content in _contents]]
    # print(pending_moves)
    tail_positions = {0+0j}
    segments = [0+0j] * (_num_segments)
    next_segments = [0+0j] * (_num_segments)
    for direction, increment in pending_moves:
        for _ in range(increment):
            # print(common.Fore.GREEN + direction, increment, j, common.Style.RESET_ALL)
            next_segments[0] = segments[0] + {'R': 1, 'L': -1, 'U': 1j, 'D': -1j}[direction]
            # print_move(segments[0], next_segments[0], 0)
            for i in range(1, _num_segments):
                dif = next_segments[i-1] - segments[i]
                # print('dif', dif, abs(dif))
                if abs(dif) >= 2:
                    if abs(dif) == 2:
                        addition = dif/2
                        next_segments[i] = segments[i] + addition
                    else:
                        addition = 1+1j
                        if dif.real < 0:
                            addition -= 2
                        if dif.imag < 0:
                            addition -= 2j
                        # print(common.Fore.YELLOW, 'inc', addition, common.Style.RESET_ALL)
                        next_segments[i] = segments[i] + addition
                    if i == _num_segments - 1:
                        tail_positions.add(next_segments[i])
                        # print(common.Fore.RED + 'adding', next_segments[i], common.Style.RESET_ALL)
                else:
                    next_segments[i] = segments[i]
                # print_move(segments[i], next_segments[i], i)
            segments = next_segments[:]
        # common.draw_positions(tail_positions)
    return tail_positions

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    positions = gen_positions(_contents, NUM_SEGMENTS)
    # common.draw_positions(positions)
    return len(positions)

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 6018)
