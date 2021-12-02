from helper_functions import read_input_as_list
import re

puzzle_input = read_input_as_list(filepath='./data/input_02.txt')

def run_commands_and_return_depth_and_horizontal_position(puzzle_input, use_aim=True):
    depth, horizontal_position, aim = 0, 0, 0
    adjust_depth = 0 if use_aim else 1

    for instruction in puzzle_input:
        direction = extract_direction(instruction)
        step_size = extract_step_size(instruction)

        if direction == 'forward':
            horizontal_position += step_size
            if use_aim:
                depth += ( aim * step_size )
        elif direction == 'up':
            depth -= ( step_size * adjust_depth )
            aim -= step_size
        elif direction == 'down':
            depth += ( step_size * adjust_depth )
            aim += step_size

    return depth, horizontal_position

def extract_direction(instruction):
    return re.search('^([a-z]+)', instruction).group(1)

def extract_step_size(instruction):
    return int(re.search('([0-9]+)$', instruction).group(1))

## Part One
depth, horizontal_position = run_commands_and_return_depth_and_horizontal_position(
    puzzle_input, use_aim=False)
print('Part One:', depth * horizontal_position)

## Part Two
depth, horizontal_position = run_commands_and_return_depth_and_horizontal_position(
    puzzle_input, use_aim=True)
print('Part Two:', depth * horizontal_position)