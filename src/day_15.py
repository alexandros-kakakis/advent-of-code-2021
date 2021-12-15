import heapq
import sys
from collections import defaultdict
from helper_functions import read_input_as_list
import numpy as np

def find_shortest_path(puzzle_input, scale):
    size = puzzle_input.shape[0]

    distance_to_start = defaultdict(lambda: sys.maxsize)
    distance_to_start[(0, 0)] = 0

    queue = []
    heapq.heappush(queue, (0, (0, 0)))

    while queue:
        shortest_path, current_vertex = heapq.heappop(queue)

        neighbours = return_neighbours(current_vertex, size, scale)
        for neighbour in neighbours:
            risk_level = return_risk_level(neighbour, puzzle_input, size)
            distance = risk_level + shortest_path

            if distance < distance_to_start[neighbour]:
                distance_to_start[neighbour] = distance
                heapq.heappush(queue, (distance, neighbour))
    
    return distance_to_start[(size * scale - 1, size * scale - 1)]


def return_neighbours(vertex, size, scale=1):
    size *= scale
    neighbours = []
    x, y = vertex
    
    if x - 1 > 0:
        neighbours.append((x-1, y))
    if x + 1 < size:
        neighbours.append((x+1, y))
    if y - 1 > 0:
        neighbours.append((x, y-1))
    if y + 1 < size:
        neighbours.append((x, y+1))
        
    return neighbours


def return_risk_level(vertex, puzzle_input, size):
    x, y = vertex
    
    n_additions_x = x // size
    n_additions_y = y // size

    x_base = x % size
    y_base = y % size

    risk_level = puzzle_input[x_base, y_base] + n_additions_x + n_additions_y
    
    if risk_level > 9:
        risk_level -= 9

    return risk_level

puzzle_input = read_input_as_list('./data/input_15.txt')
puzzle_input = np.array( [ [ int(j) for j in i ] for i in puzzle_input ] )

## Part One
shortest_path = find_shortest_path(puzzle_input, scale=1)
print('Part One:', shortest_path)

## Part Two
shortest_path = find_shortest_path(puzzle_input, scale=5)
print('Part Two:', shortest_path)
