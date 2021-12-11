from helper_functions import read_input_as_list
import numpy as np

puzzle_input = read_input_as_list('./data/input_11.txt')
puzzle_input = np.array( [ np.array([ int(j) for j in i ]) for i in puzzle_input ] )

class OctupusGrid:
    def __init__(self, grid):
        self.grid = grid.copy()
        self.n_flashes = 0
        self.grid_size = grid.shape[0]

    def next_step(self):
        self.grid += 1

        while np.sum( self.grid == 10 ) > 0:
            self.update_n_flashes()
            self.handle_adjacent()

        self.reset_flashed_octupus()

    def handle_adjacent(self):
        before = 1 * ( self.grid >= 10 )
        
        self.pad_grid()
        
        flashed_locations = np.where( self.grid == 10 )
        for x, y in zip( flashed_locations[0], flashed_locations[1] ):
            self.grid[x-1:x+2, y-1:y+2] += 1

        self.pad_grid(reverse=True)

        # set new flashes to ten
        after = 1 * ( self.grid >= 10 )
        new_flashes = ( ( after - before ) == 1 )
        self.grid[new_flashes] = 10

    def update_n_flashes(self):
        self.n_flashes += np.sum( self.grid == 10 )

    def pad_grid(self, reverse=False):
        if not reverse:
            self.grid = np.pad( self.grid, pad_width=1, constant_values=11 )
        else:
            self.grid = self.grid[1:(self.grid_size+1), 1:(self.grid_size+1)]

    def reset_flashed_octupus(self):
        has_flashed = self.grid >= 10
        self.grid[has_flashed] = 0


## Part One
octupus_grid = OctupusGrid(puzzle_input)

n_steps = 100
for _ in range(n_steps):
    octupus_grid.next_step()

print('Part One:', octupus_grid.n_flashes)

## Part Two
octupus_grid = OctupusGrid(puzzle_input)

step = 1
while True:
    n_flashes_before = octupus_grid.n_flashes
    octupus_grid.next_step()
    n_flashes_after = octupus_grid.n_flashes

    if ( n_flashes_after - n_flashes_before ) == ( octupus_grid.grid_size ** 2 ):
        break
    else:
        step += 1

print('Part Two:', step)