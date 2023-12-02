# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 4 excercise 1 https://adventofcode.com/2021/day/4

import adv_common as common

BOARD_COLS = 5
BOARD_ROWS = 5

def gen_bingo_board(_input):
    # print('Input: ', _input)
    board = {}
    for line in _input:
        for number in line.split():
            board[number] = False
    return board

def gen_bingo_boards(_contents, _number_of_boards):
    boards = []
    for board_idx in range(_number_of_boards):
        first_line = 2 + (board_idx * (BOARD_ROWS + 1))
        last_line = first_line + BOARD_ROWS
        input_board = _contents[first_line:last_line]
        boards.append(gen_bingo_board(input_board))
    return boards

def mark_number_in_boards(_boards, _number):
    for board, _ in enumerate(_boards):
        if _number in _boards[board].keys():
            # print('Found number', _number, 'in board', board)
            _boards[board][_number] = True

def print_board(_board):
    for row in range(BOARD_ROWS):
        line = ''
        for col in range(BOARD_ROWS):
            line += '{:>3}'.format(tuple(_board.keys())[BOARD_ROWS * row + col])
        line += ' '
        for col in range(BOARD_ROWS):
            if tuple(_board.values())[BOARD_ROWS * row + col] is True:
                line += 'X'
            else:
                line += '.'
        print(line)

def is_winner_row(board, number):
    _is_winner_row = False
    for row in range(BOARD_ROWS):
        _is_winner_row = True
        has_winner_number = False
        for col in range(BOARD_COLS):
            if (list(board.keys()))[(BOARD_ROWS * row) + col] == number:
                has_winner_number = True
            if (list(board.values()))[(BOARD_ROWS * row) + col] is False:
                _is_winner_row = False
                break
        if _is_winner_row and has_winner_number:
            break
    return _is_winner_row

def is_winner_col(_board, _number):
    _is_winner_col = False
    for col in range(BOARD_COLS):
        _is_winner_col = True
        has_winner_number = False
        for row in range(BOARD_ROWS):
            if (list(_board.keys()))[(BOARD_ROWS * row) + col] == _number:
                has_winner_number = True
            if (list(_board.values()))[(BOARD_ROWS * row) + col] is False:
                _is_winner_col = False
                break
        if _is_winner_col and has_winner_number:
            break
    return _is_winner_col and has_winner_number

def is_winner_board(_boards, _number):
    winner_board = None
    for board in _boards:
        # explore per row
        if is_winner_row(board, _number):
            winner_board = board
            break
        #exploreper column
        elif is_winner_col(board, _number):
            winner_board = board
            break
    return winner_board

def get_sum_of_unmarked_nums(winner_board):
    unmarked_dict = dict(filter(lambda x : x[1] is False, winner_board.items()))
    unmarked_sum = sum(list(int(item) for item in unmarked_dict))
    return unmarked_sum

@common.elapsed_time_factory()
def process_contents(_contents):
    # print('Contents:', _contents)
    winning_combination = _contents[0]

    number_of_boards = (len(_contents) - 1) // (BOARD_ROWS + 1)
    boards = gen_bingo_boards(_contents, number_of_boards)

    for number in winning_combination.split(','):
        mark_number_in_boards(boards, number)
        winner_board = is_winner_board(boards, number)
        if winner_board :
            print('Winner board is', winner_board)
            print_board(winner_board)
            break

    if winner_board:
        unmarked_sum = get_sum_of_unmarked_nums(winner_board)
    print('unmarked:', unmarked_sum, 'number:', number)
    return unmarked_sum * int(number)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 25023)
