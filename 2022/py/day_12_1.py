# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 12 excercise 1 https://adventofcode.com/2022/day/12


import adv_common as common
import numpy as np

letters = 'SabcdefghijklmnopqrstuvwxyzE'

def gen_graph(map_array):
    # print(map_array)
    graph = {}
    min_x_y = 0+0j
    max_x_y = (map_array.shape[1] - 1) + (map_array.shape[0] - 1)*1j
    start_pos = 0+0j
    end_pos = 0+0j
    for y in range(int(max_x_y.imag) + 1):
        for x in range(int(max_x_y.real) + 1):
            if map_array[y][x] == 'S':
                start_pos = x+y*1j
            elif map_array[y][x] == 'E':
                end_pos = x+y*1j
            neighbours = common.get_neighbour_positions(x+y*1j, min_x_y, max_x_y)
            graph[x+y*1j] = set(filter(lambda neighbour: letters.find(map_array[int(neighbour.imag)][int(neighbour.real)]) - 1 <= letters.find(map_array[y][x]), neighbours))
            # print(graph)
    return graph, start_pos, end_pos

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    content_array = np.array(contents)
    table_graph, start_pos, end_pos = gen_graph(content_array)
    # print(table_graph)
    shortest = common.find_shortest_path_BFS(table_graph, start_pos, end_pos)
    board_array = np.full(content_array.shape, '.')
    common.draw_path(board_array, shortest, [chr(c) for c in range(ord('a'), ord('z')+1)])
    return len(shortest) - 3

if __name__ == "__main__":
    contents = common.read_input(data_type = 'char_list')
    result = process_solution(contents)
    common.print_result(result, 472)
