import numpy as np
from numpy.lib.arraypad import pad
 
def enhance_image(input_image, algorithm, pad_value='.'):
    x_range, y_range = input_image.shape
 
    N = 2
    input_image_pad = np.pad(input_image, N, constant_values=pad_value)
    output_image = np.zeros((x_range+2, y_range+2),str)
 
    for x in range(output_image.shape[0]):
        for y in range(output_image.shape[1]):
            grid = input_image_pad[x:x+3, y:y+3] # add one because of padding
 
            algorithm_idx = int( ''.join( [ '1' if i == '#' else '0' for i in grid.flatten() ] ), 2 )
            pixel = algorithm[algorithm_idx]
 
            output_image[x, y] = pixel
 
    return output_image
 
with open('./data/input_20.txt') as f:
    puzzle_input = f.read().split('\n\n')  
 
algorithm = puzzle_input[0].replace('\n', '')
input_image = np.array( [ [ j for j in i ] for i in puzzle_input[1].splitlines() ] )

## Part One
image = enhance_image(input_image, algorithm)
image = enhance_image(image, algorithm, pad_value='#')

print('Part One:', np.sum( image == '#' ))

## Part Two
last_pad_value = '#'
for _ in range(48):
    if last_pad_value == '#':
        image = enhance_image(image, algorithm, pad_value='.')
        last_pad_value = '.'
    else:
        image = enhance_image(image, algorithm, pad_value='#')
        last_pad_value = '#'
 
print('Part Two:', np.sum( image == '#' ))