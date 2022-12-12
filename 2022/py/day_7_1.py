# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 7 excercise 1 https://adventofcode.com/2022/day/7

import adv_common as common

NEEDED_SPACE = 100000

def update_directory_recursively(dict, dir, value):
    # print(dict)
    if dir != []:
        dict['/'.join(dir)] += value
        update_directory_recursively(dict, dir[:-1], value)

def gen_directory_tree(input):
    directory_tree = {'.': 0}
    current_dir = []
    for command_line in input:
        command = command_line.split(' ')
        match command[0]:
            case '$':
                match command[1]:
                    case 'cd':
                        match command[2]:
                            case '/':
                                current_dir = ['.']
                            case '..':
                                current_dir = current_dir[:-1]
                            case _:
                                current_dir.append(command[2])
                    case 'ls':
                        pass
            case 'dir':
                directory_tree['/'.join(current_dir + [command[1]])] = 0
                pass
            case _:
                update_directory_recursively(directory_tree, current_dir, int(command[0]))
    return directory_tree

@common.elapsed_time_factory()
def process_solution(contents):
    # print('Contents:', contents)
    directory_tree = gen_directory_tree(contents)
    # print(directory_tree)
    return sum([v for _, v in directory_tree.items() if v < NEEDED_SPACE])

if __name__ == "__main__":
    contents = common.read_input()
    result = process_solution(contents)
    common.print_result(result, 1517599)
