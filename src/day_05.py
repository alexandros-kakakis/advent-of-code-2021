from os import read
from helper_functions import read_input_as_list
import re
import numpy as np

puzzle_input = read_input_as_list('./data/input_05.txt')

def draw_lines_and_return_grid(puzzle_input, include_diagonal=False, grid_size=1000):
    grid = np.zeros((grid_size, grid_size))
    for i in puzzle_input:
        coord_list = re.split( ',|\s\-\>\s', i)
        coord_list = [ int(i) for i in coord_list ]

        x1, y1, x2, y2 = coord_list[0], coord_list[1], coord_list[2], coord_list[3]

        if y1 == y2: # horizontal line
            if x2 > x1:
                grid[y1, x1:(x2+1)] += 1
            else:
                grid[y1, x2:(x1+1)] += 1

        elif x1 == x2: # vertical line
            if y2 > y1:
                grid[y1:(y2+1), x1] += 1
            else:
                grid[y2:(y1+1), x1] += 1

        elif include_diagonal: # diagonal line
            if x2 > x1: 
                if y2 > y1:
                    x, y = x1, y1
                    while ( x <= x2 ) & ( y <= y2 ):
                        grid[y, x] += 1
                        x += 1
                        y += 1
                else:
                    x, y = x2, y2
                    while ( x >= x1 ) & ( y <= y1 ):
                        grid[y, x] += 1
                        x -= 1
                        y += 1
            
            if x1 > x2:
                if y2 > y1:
                    x, y = x2, y2
                    while ( x <= x1 ) & ( y >= y1 ):
                        grid[y, x] += 1
                        x += 1
                        y -= 1
                else:
                    x, y = x2, y2
                    while ( x <= x1 ) & ( y <= y1 ):
                        grid[y, x] += 1
                        x += 1
                        y += 1
    
    return grid

## Part One
grid = draw_lines_and_return_grid(puzzle_input, include_diagonal=False, grid_size=1000)
print('Part One:', np.sum( grid > 1 ))

## Part Two
grid = draw_lines_and_return_grid(puzzle_input, include_diagonal=True, grid_size=1000)
print('Part Two:', np.sum( grid > 1 ))