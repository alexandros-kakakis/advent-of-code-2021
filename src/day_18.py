from helper_functions import read_input_as_list
from day_18_func import reduce_number, add_numbers, calculate_magnitude

puzzle_input = read_input_as_list('./data/input_18.txt')

## Part One
number = puzzle_input[0]
for next_number in puzzle_input[1:]:
    number = add_numbers(number, next_number)
    number = reduce_number(number)
    number = ''.join(number)

magnitude = calculate_magnitude(number)

print('Part One:', magnitude)

## Part Two
global_max = 0

for number_l in puzzle_input:
    for number_r in puzzle_input:
        if number_l == number_r:
            continue
        else:
            number = add_numbers(number_l, number_r)
            number = reduce_number(number)
            number = ''.join(number)

            magnitude = calculate_magnitude(number)
            global_max = max( global_max, magnitude )

print('Part Two:', global_max)
