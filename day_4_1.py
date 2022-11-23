# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 4 excercise 1 https://adventofcode.com/2021/day/1

import adv2021_common as common

BOARD_COLS = 5
BOARD_ROWS = 5

def gen_bingo_board(input):
    # print('Input: ', input)
    board = {}
    for line in input:
        for number in line.split():
            board[number] = False
    return board

def gen_bingo_boards(contents, number_of_boards):
    boards = []
    for board_idx in range(number_of_boards):
        first_line = 2 + (board_idx * (BOARD_ROWS + 1))
        last_line = first_line + BOARD_ROWS
        input_board = contents[first_line:last_line]
        boards.append(gen_bingo_board(input_board))
    return boards

def mark_number_in_boards(boards, number):
    for board in range(len(boards)):
        if number in boards[board].keys():
            # print('Found number', number, 'in board', board)
            boards[board][number] = True

def is_winner_row(board):
    is_winner_row = False
    for row in range(BOARD_ROWS):
        is_winner_row = True
        for col in range(BOARD_COLS):
            if (list(board.values()))[(BOARD_ROWS * row) + col] == False:
                is_winner_row = False
                break
        if is_winner_row:
            break
    return is_winner_row

def is_winner_col(board):
    is_winner_col = False
    for col in range(BOARD_COLS):
        is_winner_col = True
        for row in range(BOARD_ROWS):
            if (list(board.values()))[(BOARD_ROWS * row) + col] == False:
                is_winner_col = False
                break
        if is_winner_col:
            break
    return is_winner_col

def is_winner_board(boards):
    winner_board = None
    for board in boards:
        # explore per row
        if is_winner_row(board):
            winner_board = board
            break
        #exploreper column
        elif is_winner_col(board):
            winner_board = board
            break
    return winner_board

def get_sum_of_unmarked_nums(winner_board):

    unmarked_dict = dict(filter(lambda x : x[1] == False, winner_board.items()))
    unmarked_sum = sum(list(int(item) for item in unmarked_dict))
    return unmarked_sum

def process_contents(contents):
    # print('Contents:', contents)
    winning_combination = contents[0]

    number_of_boards = (len(contents) - 1) // (BOARD_ROWS + 1)
    boards = gen_bingo_boards(contents, number_of_boards)

    for number in winning_combination.split(','):
        mark_number_in_boards(boards, number)
        winner_board = is_winner_board(boards)
        if winner_board :
            print('Winner board is', winner_board)
            break

    if winner_board:
        unmarked_sum = get_sum_of_unmarked_nums(winner_board)
    print('unmarked:', unmarked_sum, 'number', number)
    result = unmarked_sum * int(number)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 25023)
