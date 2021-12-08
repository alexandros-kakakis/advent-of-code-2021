from helper_functions import read_input_as_list
from day_08_func import generate_number_dict, sort_signals
import numpy as np

puzzle_input = read_input_as_list('./data/input_08.txt')

translated_values = []

for entry in puzzle_input:
    unique_values = entry.split('|')[0].strip().split(' ')
    unique_values =  sort_signals(unique_values)

    number_dict = generate_number_dict(unique_values)

    output_values = entry.split('|')[1].strip().split(' ')
    output_values = sort_signals(output_values)

    translated_values.append( [ number_dict[val] for val in output_values ] )

## Part One
easy_digits = [ 1, 4, 7, 8 ]
count = sum( [ sum( [ 1 for j in i if j in  easy_digits ] ) for i in translated_values ])
print('Part One:', count)

## Part Two
total = sum( [ int( ''.join([ str(j) for j in i ]) ) for i in translated_values ] ) 
print('Part Two:', total)