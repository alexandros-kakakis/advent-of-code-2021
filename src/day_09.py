from helper_functions import read_input_as_list
from day_09_func import return_all_basin_points
import numpy as np

puzzle_input = read_input_as_list('./data/input_09.txt')
puzzle_input = np.array( [ np.array([ int(j) for j in i ]) for i in puzzle_input ] )

n_rows, n_cols = puzzle_input.shape

## Part One

risk_level = 0

for x in range(0, n_cols):
    for y in range(0, n_rows):
        point = puzzle_input[y, x]

        x1, x2 = max( x - 1, 0), x + 2
        y1, y2 = max( y - 1, 0), y + 2

        window = puzzle_input[y1:y2, x1:x2]
        
        if window.min() == point:
            risk_level += ( point + 1 )
        
print('Part One:', risk_level)

## Part Two
result = []

for x in range(0, n_rows):
    for y in range(0, n_cols):

        if puzzle_input[x, y] == 9:
            pass
        else:
            all_basin_points = return_all_basin_points(puzzle_input, points_to_check=[(x,y)])
            result.append( len(all_basin_points) )

result.sort()
solution = result[-1] * result[-2] * result[-3]
print('Part Two:', solution)
