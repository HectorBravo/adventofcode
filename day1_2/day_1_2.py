# Copyright Hector Bravo <hbravo@cuic.net>
# Code for Day 1 excercise 2 https://adventofcode.com/2021/day/1#part2

input_file = 'day_1_2_input.txt'

def read_input(input_file):
    with open(input_file) as f:
        contents = f.read().splitlines()
    return contents

def process_contents(contents):
    # print(contents)
    result = 0
    previous_sum = int(contents[0]) + int(contents[1]) + int(contents[2])
    for i in range(1, len(contents)-2):
        current_sum = int(contents[i]) + int(contents[i+1]) + int(contents[i+2])
        if current_sum > previous_sum:
            result += 1
        previous_sum = current_sum
    return result

if __name__ == "__main__":
    contents = read_input(input_file)
    result = process_contents(contents)
    print('Result is:', result)