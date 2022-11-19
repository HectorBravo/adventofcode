# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 1 https://adventofcode.com/2021/day/1

input_file = 'day_1_1_input.txt'

def read_input(input_file):
    with open(input_file) as f:
        contents = f.read().splitlines()
    return contents

def process_contents(contents):
    # print(contents)
    result = 0
    previous = contents[0]
    for current in contents:
        if int(current) > int(previous):
            result += 1
        previous = current
    return result

if __name__ == "__main__":
    contents = read_input(input_file)
    result = process_contents(contents)
    print('Result is:', result)