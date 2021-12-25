import numpy as np

with open('./data/input_25.txt') as f:
    lines = f.read().splitlines()

map = np.array( [ list(i[0]) for i in [ l.splitlines() for l in lines ] ])
n_rows, n_cols = map.shape

empty = set([ tuple(i) for i in np.argwhere(map=='.') ])
east = set([ tuple(i) for i in np.argwhere(map=='>') ])
south = set([ tuple(i) for i in np.argwhere(map=='v') ])

n_steps = 0

while True:
    east_start = east.copy()
    south_start = south.copy()

    ## east
    candidates = set( [ (x, y+1) if (y+1) < n_cols else (x, 0) for x, y in east ] )
    new_location = candidates.intersection(empty)
    prev_location = set([ (x, n_cols-1) if y == 0 else (x, y-1) for x, y in new_location ])

    east = east.union(new_location) - prev_location
    empty = empty.union(prev_location) - new_location

    ## south
    candidates = set( [ (x+1, y) if (x+1) < n_rows else (0, y) for x, y in south ] )
    new_location = candidates.intersection(empty)
    prev_location = set([ (n_rows-1, y) if x == 0 else (x-1, y) for x, y in new_location ])

    south = south.union(new_location) - prev_location
    empty = empty.union(prev_location) - new_location

    n_steps += 1

    if ( east == east_start ) and ( south == south_start ):
        break

print('Part One:', n_steps)