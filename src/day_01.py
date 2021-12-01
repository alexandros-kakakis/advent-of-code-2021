from helper_functions import read_input_as_list
import pandas as pd

puzzle_input = read_input_as_list(filepath='./data/input_01.txt')
puzzle_input = [ int(i) for i in puzzle_input ]
puzzle_input = pd.Series( puzzle_input )

def return_number_of_increments(puzzle_input, sliding_window):
    differences = puzzle_input.rolling(sliding_window).sum() - \
        puzzle_input.rolling(sliding_window).sum().shift(1)

    return ( differences > 0 ).sum()

## Part One
number_of_increments = return_number_of_increments(puzzle_input, sliding_window=1)
print('Part One:', number_of_increments)

## Part Two
number_of_increments = return_number_of_increments(puzzle_input, sliding_window=3)
print('Part Two:', number_of_increments)
