# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 22 excercise 1 https://adventofcode.com/2022/day/22


import adv_common as common
import re
import numpy as np

increments = {'>': 1, '<': -1, '^': -1j, 'v': 1j}
directions = ['>', 'v', '<', '^']
# directions = ['>', '<', '^', 'v']

def print_board(_board):
    print(np.array([[''.join(line)] for line in _board]))

def get_next_neighbour_pos(_current, _direction, _board):
    tmp_pos = _current + increments[_direction]
    neighbour_pos = (tmp_pos.real % np.shape(_board)[1]) + (tmp_pos.imag % np.shape(_board)[0]) * 1j
    if _board[int(neighbour_pos.imag)][int(neighbour_pos.real)] == ' ':
        match _direction:
            case '>':
                line = ''.join(_board[int(_current.imag)])[::1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = index + neighbour_pos.imag * 1j
            case '<':
                line = ''.join(_board[int(_current.imag)])[::-1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = np.shape(_board)[1] - index - 1 + neighbour_pos.imag * 1j
            case 'v':
                line = ''.join(_board[:, int(_current.real)])[::1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = index * 1j + neighbour_pos.real
            case '^':
                line = ''.join(_board[:, int(_current.real)])[::-1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = (np.shape(_board)[0] - index - 1) * 1j + neighbour_pos.real

    return neighbour_pos

def get_password(_board, _path):
    position = ''.join(_board[0]).find('.') + 0j
    # print(position)
    # print(_path)
    direction = '>'
    _board[int(position.imag)][int(position.real)] = direction
    # print_board(_board)
    for i in _path:
        if isinstance(i, int):
            for _ in range(i):
                # print(position, i - advance, 'to', direction)
                neighbour = get_next_neighbour_pos(position, direction, _board)
                # print(neighbour)
                if _board[int(neighbour.imag)][int(neighbour.real)] == '#':
                    break
                else:
                    position = neighbour
                    _board[int(position.imag)][int(position.real)] = direction
                    # print_board(_board)
        else:
            # print(i, direction)
            increment = 1 if i == 'R' else - 1
            direction = directions[(directions.index(str(direction)) + increment) % 4]
            # print(direction)
    # print_board(_board)
    # print(position, direction)
    return int((position.imag + 1) * 1000 + (position.real + 1) * 4 + directions.index(str(direction)))

@common.elapsed_time_factory()
def process_solution(_contents):
    # print('Contents:', _contents)
    board = np.array([list(line) for line in _contents[0]])
    path = [int(x) if x.isnumeric() else x for x in re.findall('(\\d+|[r,l])', _contents[1][0], flags = re.IGNORECASE)]
    return get_password(board, path)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 11464)
