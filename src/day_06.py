from helper_functions import read_input_as_list
from collections import Counter

puzzle_input = read_input_as_list('./data/input_06.txt')
puzzle_input = puzzle_input[0].split(',')

def convert_puzzle_input_to_fish(puzzle_input):
    fish = { i: 0 for i in range(9) }

    for i in puzzle_input:
        fish[int(i)] += 1

    return fish
    
def wait_n_days(n_days):
    global fish 

    for _ in range(n_days):
        for age, count in fish.copy().items():
            if age == 0:
                fish[age] = 0
                fish[6] += count
                fish[8] += count
            else:        
                fish[age] -= count
                fish[age-1] += count
            
## Part One
fish = convert_puzzle_input_to_fish(puzzle_input)
wait_n_days(n_days=80)
n_fish = sum( fish.values() )
print('Part One:', n_fish)

## Part Two
fish = convert_puzzle_input_to_fish(puzzle_input)
wait_n_days(n_days=256)
n_fish = sum( fish.values() )
print('Part Two:', n_fish)
