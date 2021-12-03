import pandas as pd
from helper_functions import read_input_as_list

puzzle_input = read_input_as_list(filepath='./data/input_03.txt')

def convert_puzzle_input_to_df(puzzle_input):
    df = pd.DataFrame( puzzle_input, columns=['input'] )
    df = df['input'].str.extractall('([0-9])').astype(int).reset_index()
    df = df.pivot_table(index='level_0', columns='match', values=0).reset_index()
    df = df.drop('level_0', axis=1)
    return df

data = convert_puzzle_input_to_df(puzzle_input)

## Part One
df = data.copy()
dominant_bits = list( 1 * ( df.mean() > .5 ) )

gamma = int( ''.join([ str(i) for i in dominant_bits ]), 2 )
epsilon = int( ''.join([ str(1 - i) for i in dominant_bits ]), 2 )

print('Part One:', gamma * epsilon)

## Part Two

def filter_by_bit_criteria(data, use_dominant=True):
    df = data.copy()
    col_counter = 0

    while len(df) > 1:
        dominant_bit = 1 * ( df[col_counter].mean() >= .5 )

        if use_dominant:
            df = df[df[col_counter] == dominant_bit]
        else:
            df = df[df[col_counter] != dominant_bit]
        
        col_counter += 1
    
    return df

df = filter_by_bit_criteria(data, use_dominant=True)
oxy = int( ''.join([ str(i) for i in list(df.iloc[0, :]) ]), 2 )

df = filter_by_bit_criteria(data, use_dominant=False)
co2 = int( ''.join([ str(i) for i in list(df.iloc[0, :]) ]), 2 )

print('Part Two:', oxy * co2)