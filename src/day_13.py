from helper_functions import read_input_as_list
import numpy as np
import re

puzzle_input = read_input_as_list('./data/input_13.txt')
dot_instructions = [ i for i in puzzle_input if ',' in i ]
fold_instructions = [ i for i in puzzle_input if 'fold' in i ]

first_y_fold = [ i for i in fold_instructions if 'y' in i ][0]
n_rows = int( re.findall('[0-9]+', first_y_fold)[0] ) * 2 + 1

first_x_fold = [ i for i in fold_instructions if 'x' in i ][0]
n_cols = int( re.findall('[0-9]+', first_x_fold)[0] ) * 2 + 1

def create_grid(n_rows, n_cols, dot_instructions):
    grid = np.zeros((n_rows, n_cols))

    for i in dot_instructions:
        x, y = i.split(',')
        x, y = int(x), int(y)
        grid[y, x] = 1

    return grid

def fold_paper(grid, fold_instruction):
    if 'x' in fold_instruction:
        fold_index = int( np.floor( grid.shape[1] / 2 ) )
        grid = grid[:, 0:fold_index] + np.flip( grid[:, fold_index+1:], 1 )
    else:
        fold_index = int( np.floor( grid.shape[0] / 2 ) )
        grid = grid[0:fold_index, :] + np.flip( grid[fold_index+1:, :], 0 )

    return grid

## Part One
grid = create_grid(n_rows, n_cols, dot_instructions)
grid = fold_paper(grid, fold_instructions[0])

print('Part One:', np.sum(grid > 0))

## Part Two
grid = create_grid(n_rows, n_cols, dot_instructions)
for fold_instruction in fold_instructions:
    grid = fold_paper(grid, fold_instruction)

is_dotted = ( grid > 0 )
grid = grid.astype('object')
grid[ ~is_dotted ] = '_'
grid[ is_dotted ] = '#'

print('Part Two:')
for i in grid:
    print(''.join(i))