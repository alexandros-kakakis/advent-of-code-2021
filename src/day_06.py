from helper_functions import read_input_as_list
import numpy as np

puzzle_input = read_input_as_list('./data/input_06.txt')
puzzle_input = puzzle_input[0].split(',')
puzzle_input = [ int(i) for i in puzzle_input ]
puzzle_input = np.array( puzzle_input )

class Fish:
    def __init__(self, age, n_days_left, knowledge):
        self.age = age
        self.n_children = 0
        self.n_days_left = n_days_left
        self.knowledge = knowledge
        
    def calculate_n_children(self):
        if self.age >= self.n_days_left:
            pass

        elif ( self.age == 8 ) & ( self.knowledge[self.n_days_left] >= 0 ):
            self.n_children += self.knowledge[self.n_days_left]
        
        else:
            self.n_days_left -= ( self.age + 1 )
            self.n_children += 1

            child = Fish(age=8, n_days_left=self.n_days_left, knowledge=self.knowledge)
            child.calculate_n_children()

            self.n_children += child.n_children        

            while self.n_days_left >= 7:
                self.n_days_left -= 7
                self.n_children += 1

                child = Fish(age=8, n_days_left=self.n_days_left, knowledge=self.knowledge)

                child.calculate_n_children()
                self.knowledge[self.n_days_left] = child.n_children

                self.n_children += child.n_children
    

def calculate_number_of_fish(puzzle_input, n_days):
    total_fish = 0

    unique_ages = np.unique( puzzle_input )
    knowledge = np.ones( n_days + 1 ) * (-1)

    for age in unique_ages:   
        total_fish_age = 0

        fish = Fish(age=age, n_days_left=n_days, knowledge=knowledge)

        fish.calculate_n_children()
        knowledge = fish.knowledge

        total_fish_age += fish.n_children
        total_fish_age += 1

        total_fish += np.sum( puzzle_input == age ) * total_fish_age

    return int(total_fish)

## Part One
n_fish = calculate_number_of_fish(puzzle_input, n_days=80)
print('Part One:', n_fish)

## Part Two
n_fish = calculate_number_of_fish(puzzle_input, n_days=256)
print('Part Two:', n_fish)
