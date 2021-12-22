import re
from helper_functions import read_input_as_list

## Part One

puzzle_input = read_input_as_list('./data/input_22.txt')

on_cubes = set()

for step in puzzle_input:
    instruction = step.split(' ')[0]

    cuboid = step.split(' ')[1].split(',')
    cuboid_borders = []
    for axis in range(3):
        axis_borders = cuboid[axis][2:].split('..')
        axis_borders = [ int(i) for i in axis_borders ]
        axis_borders = [ max(-50, axis_borders[0]), min(50, axis_borders[1])]

        cuboid_borders.append( [ int(i) for i in axis_borders ] )

    
    for x in range(cuboid_borders[0][0], cuboid_borders[0][1] + 1):
        for y in range(cuboid_borders[1][0], cuboid_borders[1][1] + 1):
            for z in range(cuboid_borders[2][0], cuboid_borders[2][1] + 1):
                cube = (x, y, z)

                if max( abs(x), abs(y), abs(z) ) > 50:
                    continue

                if instruction == 'on':
                    on_cubes.add(cube)
                else:
                    if cube in on_cubes:
                        on_cubes.remove(cube)

print('Part One:', len(on_cubes))


## Part Two

# inspired by https://github.com/Fadi88/AoC/blob/master/2021/day22/code.py

class Cube:
    
    def __init__(self, x0, x1, y0, y1, z0, z1):
        self.x0 = x0
        self.x1 = x1
        self.y0 = y0
        self.y1 = y1
        self.z0 = z0
        self.z1 = z1
        self.instruction = instruction
        
        self.negative_cubes = []
        
    def calculate_volume(self):
        positive_volume = ( self.x1 - self.x0 + 1 ) * ( self.y1 - self.y0 + 1 ) * ( self.z1 - self.z0 + 1 ) 
        negative_volume = sum([ cube.calculate_volume() for cube in self.negative_cubes ])
        return positive_volume - negative_volume
        
    def intersection(self, other):
        x0 = max( self.x0, other.x0 )
        x1 = min( self.x1, other.x1 )
        if x0 > x1: return

        y0 = max( self.y0, other.y0 )
        y1 = min( self.y1, other.y1 )
        if y0 > y1: return
        
        z0 = max( self.z0, other.z0 )
        z1 = min( self.z1, other.z1 )
        if z0 > z1: return
        
        return Cube(x0, x1, y0, y1, z0, z1)
        
    def substract(self, other):
        intersection = self.intersection(other)
        
        for n_cube in self.negative_cubes:
            n_cube.substract(other)
        
        if intersection:
            self.negative_cubes.append(intersection)
            

with open('./data/input_22.txt') as f:
    lines = f.read().splitlines()

reactor_field = []

for l in lines:
    instruction = l.split(' ')[0]
    x0, x1, y0, y1, z0, z1 = map(int, re.findall('-?\d+', l))

    new_cube = Cube(x0, x1, y0, y1, z0, z1)
    
    for cube in reactor_field:
        cube.substract(new_cube)
                    
    if instruction == 'on':
        reactor_field.append(new_cube)

print( 'Part Two:', sum( [ i.calculate_volume() for i in reactor_field ] ) )