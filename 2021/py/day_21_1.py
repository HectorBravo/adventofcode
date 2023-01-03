# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 21 excercise 1 https://adventofcode.com/2021/day/21

import adv_common as common

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    positions = [int(c.split()[-1]) for c in contents]
    scores = [0, 0]
    rolls = 0
    player = 0
    die = 1
    while max(scores) < 1000:
        positions[player] = ((positions[player] + sum(list(range(die, die + 3)))) % 10) or 10
        scores[player] += positions[player]
        # print('Player {} rolls {} and moves to space {} for a total score of {}'.format(player+1, list(range(die, die + 3)), positions[player], scores[player]))
        rolls += 3
        die = ((rolls + 1) % 100) or 100
        player = (player + 1) % 2
    # print(scores, positions)
    return min(scores) * rolls

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 675024)
