from helper_functions import read_input_as_list
import numpy as np

puzzle_input = read_input_as_list('./data/input_07.txt')
puzzle_input = puzzle_input[0].split(',')
puzzle_input = [ int(i) for i in puzzle_input ]
puzzle_input = np.array( puzzle_input )


def find_best_position_and_return_total_fuel(puzzle_input, calculate_fuel_formula):
    min_fuel = 1e10

    for position in range( min(puzzle_input), max(puzzle_input) + 1 ):
        step_sizes = abs( puzzle_input - position )
        fuel = [ calculate_fuel_formula(i) for i in step_sizes ]
        fuel = np.sum( fuel )

        if fuel < min_fuel:
            min_fuel = fuel

    return min_fuel
    

## Part One
calculate_fuel = lambda x: x
total_fuel = find_best_position_and_return_total_fuel(puzzle_input, calculate_fuel)

print('Part One:', total_fuel)

# Part Two
calculate_fuel = lambda x: ( x ** 2 + x ) / 2
total_fuel = find_best_position_and_return_total_fuel(puzzle_input, calculate_fuel)

print('Part Two:', int(total_fuel) )