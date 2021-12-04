import numpy as np
import re

class Board:

    def __init__(self, grid):
        self.grid = grid
        self.grid_size = grid.shape[0]
        self.board_score = np.zeros( (self.grid_size, self.grid_size))

    def update_score(self, number):
        result = 1 * ( self.grid == number )
        self.board_score += result

    def check_bingo(self):
        check_rows = ( self.board_score.sum(axis=1) == self.grid_size ).any()
        check_cols = ( self.board_score.sum(axis=0) == self.grid_size ).any()
        return check_rows | check_cols


def load_board_grid(board_number, grid_size=5):
    lines = read_board_lines()

    start = board_number * ( grid_size + 1 )
    board = []

    for l in lines[start:start+grid_size]:
        row = re.split(r'\s{1,}', l.strip())
        row = [ int(i) for i in row ]

        board.append(row)

    board = np.array(board)
    return board


def read_number_order():
    with open('./data/input_04.txt', 'r') as f:
        number_order = f.readline().split(',')
        number_order = [ int(i) for i in number_order ]
    
    return number_order


def read_board_lines():
    with open('./data/input_04.txt', 'r') as f:
        lines = f.readlines()[2:] # lines start from third row

    return lines


def return_number_of_boards():
    board_lines = read_board_lines()
    return int( ( len(board_lines) + 1 ) / 6 )


def play_bingo(board_number, number_order):
    board_grid = load_board_grid(board_number)
    board = Board(grid=board_grid)

    number_count = 0
    bingo = False

    while not bingo:
        number = number_order[number_count]
        number_count += 1

        board.update_score(number)
        bingo = board.check_bingo()

    n_numbers = number_count
    unmarked_sum = np.sum( board.grid - board.grid * board.board_score )
    winning_number = number
    final_score = unmarked_sum * winning_number

    return n_numbers, final_score


## Part One 
number_of_boards = return_number_of_boards()
number_order = read_number_order()
min_numbers = len(number_order)
solution = 0

for i in range(0, number_of_boards):
    n_numbers, final_score = play_bingo(i, number_order)
    if n_numbers < min_numbers:
        min_numbers = n_numbers
        solution = final_score

print('Part One:', int(solution))

## Part Two
number_of_boards = return_number_of_boards()
number_order = read_number_order()
min_numbers = 0
solution = 0

for i in range(0, number_of_boards):
    n_numbers, final_score = play_bingo(i, number_order)
    if n_numbers > min_numbers:
        min_numbers = n_numbers
        solution = final_score

print('Part Two:', int(solution))
