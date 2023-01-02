# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 22 excercise 1 https://adventofcode.com/2022/day/22


import adv_common as common
import re
import numpy as np

increments = {'>': 1, '<': -1, '^': -1j, 'v': 1j}
directions = ['>', 'v', '<', '^']
# directions = ['>', '<', '^', 'v']

def print_board(board):
    print(np.array([[''.join(line)] for line in board]))

def get_next_neighbour_pos(current, direction, board):
    tmp_pos = current + increments[direction]
    neighbour_pos = (tmp_pos.real % np.shape(board)[1]) + (tmp_pos.imag % np.shape(board)[0]) * 1j
    if board[int(neighbour_pos.imag)][int(neighbour_pos.real)] == ' ':
        match direction:
            case '>':
                line = ''.join(board[int(current.imag)])[::1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = index + neighbour_pos.imag * 1j
            case '<':
                line = ''.join(board[int(current.imag)])[::-1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = np.shape(board)[1] - index - 1 + neighbour_pos.imag * 1j
            case 'v':
                line = ''.join(board[:, int(current.real)])[::1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = index * 1j + neighbour_pos.real
            case '^':
                line = ''.join(board[:, int(current.real)])[::-1]
                index = re.search(r'[^" "]', line).start()
                neighbour_pos = (np.shape(board)[0] - index - 1) * 1j + neighbour_pos.real

    return neighbour_pos

def get_password(board, path):
    position = ''.join(board[0]).find('.') + 0j
    # print(position)
    # print(path)
    direction = '>'
    board[int(position.imag)][int(position.real)] = direction
    # print_board(board)
    for i in path:
        if type(i) == int:
            for advance in range(i):
                # print(position, i - advance, 'to', direction)
                neighbour = get_next_neighbour_pos(position, direction, board)
                # print(neighbour)
                if board[int(neighbour.imag)][int(neighbour.real)] == '#':
                    break
                else:
                    position = neighbour
                    board[int(position.imag)][int(position.real)] = direction
                    # print_board(board)
        else:
            # print(i, direction)
            increment = 1 if i == 'R' else - 1
            direction = directions[(directions.index(str(direction)) + increment) % 4]
            # print(direction)
    # print_board(board)
    # print(position, direction)
    return int((position.imag + 1) * 1000 + (position.real + 1) * 4 + directions.index(str(direction)))

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    board = np.array([list(line) for line in contents[0]])
    path = [int(x) if x.isnumeric() else x for x in re.findall('(\\d+|[r,l])', contents[1][0], flags = re.IGNORECASE)]
    return get_password(board, path)

if __name__ == "__main__":
    contents = common.read_input(data_type = 'struct_list')
    result = process_solution(contents)
    common.print_result(result, 11464)
