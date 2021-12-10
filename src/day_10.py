from helper_functions import read_input_as_list
import numpy as np

puzzle_input = read_input_as_list('./data/input_10.txt')

character_pairs = ['{}', '[]', '<>', '()']
closing_char = [ char[1] for char in character_pairs ]

def remove_patterns_from_line(line, list_of_patterns):
    max_nr_of_patterns = int( np.floor( len(line) / 2 ) )
    for _ in range(max_nr_of_patterns):
        for pattern in list_of_patterns:
            line = line.replace(pattern, '')

    return line

## Part One 
score_dict = { ')':3, ']': 57, '}': 1197, '>': 25137 }

score = 0

for line in puzzle_input:
    line = remove_patterns_from_line(line, list_of_patterns=character_pairs)

    incorrect_closing_char = [ char for char in line if char in closing_char ]
    if len(incorrect_closing_char) > 0:
        score += score_dict[incorrect_closing_char[0]]
        
print('Part One:', score)

## Part Two

def calculate_total_score(list_of_scores):
    total_score = 0
    for score in list_of_scores:
        total_score *= 5
        total_score += score

    return total_score

score_dict = { ')':1, ']': 2, '}': 3, '>': 4 }
scores = []

for line in puzzle_input:
    line = remove_patterns_from_line(line, list_of_patterns=character_pairs)
    line = line[::-1]
    
    # check if line is corrupt
    if len( [ char for char in line if char in closing_char ] ) > 0:
        continue

    # find the corresponding closing character
    autocomplete = [ [ char[1] for char in character_pairs if char[0] == l ][0] for l in line ]

    list_of_scores = [ score_dict[char] for char in autocomplete ]
    score = calculate_total_score(list_of_scores)
    scores.append( score )

scores.sort()
middle_index = int( ( len(scores) - 1 ) / 2 )

print('Part Two:', scores[middle_index])
