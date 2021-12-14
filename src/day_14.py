from helper_functions import read_input_as_list
from collections import Counter

puzzle_input = read_input_as_list('./data/input_14.txt')

template = puzzle_input[0]
rules = puzzle_input[2:]
rules = { r.split(' -> ')[0]: r.split(' -> ')[1] for r in rules }

pairs = { i:template.count(i) for i in rules.keys() }
chars = { i:template.count(i) for i in rules.values() }

def update_chars(n_steps):
    global chars
    global pairs
    global rules

    for _ in range(n_steps):
        for pair, count in pairs.copy().items():
            pairs[pair] -= count
            pairs[pair[0] + rules[pair]] += count
            pairs[rules[pair] + pair[1]] += count

            chars[rules[pair]] += count

## Part One
update_chars(n_steps=10)
solution = max(chars.values()) - min(chars.values())
print('Part One:', solution)

## Part Two
update_chars(n_steps=30) # 30 additional steps needed to reach 40
solution = max(chars.values()) - min(chars.values())
print('Part One:', solution)
