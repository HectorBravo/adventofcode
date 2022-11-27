# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 4 excercise 2 https://adventofcode.com/2021/day/4

import adv2021_common as common
import day_4_1 as day_4_1

def process_contents(contents):
    # print('Contents:', contents)
    winning_combination = contents[0]

    number_of_boards = (len(contents) - 1) // (day_4_1.BOARD_ROWS + 1)
    boards = day_4_1.gen_bingo_boards(contents, number_of_boards)

    number_list = winning_combination.split(',')
    for number in number_list:
        print('marking num:', number)
        day_4_1.mark_number_in_boards(boards, number)
        winner_board = day_4_1.is_winner_board(boards, number)
        if winner_board:
            # day_4_1.print_board(winner_board)
            # print('board len:', len(boards))
            if (len(boards) == 1) or (number == number_list[-1]):
                print('winner board is')
                day_4_1.print_board(winner_board)
                break
            else:
                print('removing board:')
                day_4_1.print_board(winner_board)
                boards.remove(winner_board)
        else:
            print('no winner board')

    if winner_board != None:
        unmarked_sum = day_4_1.get_sum_of_unmarked_nums(winner_board)
    print('unmarked:', unmarked_sum, 'number:', number)
    result = unmarked_sum * int(number)
    return result

if __name__ == "__main__":
    contents = common.read_input()
    result = process_contents(contents)
    common.print_result(result, 0)
