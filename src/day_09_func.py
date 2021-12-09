def return_all_basin_points(puzzle_input, points_to_check, checked_points=[]):
    
    while len( set( points_to_check ) - set( checked_points ) ) > 0:
        point = list( set( points_to_check ) - set( checked_points ) )[0]
        basin_points = return_basin_points(puzzle_input, point)
        
        checked_points.append(point)
        
        points_to_check += basin_points
        points_to_check = list( set( points_to_check ) )

        points_to_check = return_all_basin_points(puzzle_input, points_to_check, checked_points)

    return list( set( points_to_check ) )

def return_basin_points(puzzle_input, point):
    basin_points = []
    basin_points += return_basin_points_right(puzzle_input, point)
    basin_points += return_basin_points_left(puzzle_input, point)
    basin_points += return_basin_points_down(puzzle_input, point)
    basin_points += return_basin_points_up(puzzle_input, point)
    return basin_points

def return_basin_points_right(puzzle_input, point):
    x, y = point[0], point[1]
    basin_points = []

    while True:
        y += 1
        if y >= puzzle_input.shape[1]:
            break
        elif puzzle_input[x, y] == 9:
            break
        else:
            basin_points += [ (x, y) ]

    return basin_points

def return_basin_points_left(puzzle_input, point):
    x, y = point[0], point[1]
    basin_points = []

    while True:
        y -= 1
        if ( y < 0 ):
            break
        elif puzzle_input[x, y] == 9:
            break
        else:
            basin_points += [ (x, y) ]

    return basin_points

def return_basin_points_down(puzzle_input, point):
    x, y = point[0], point[1]
    basin_points = []

    while True:
        x += 1
        if ( x >= puzzle_input.shape[0] ):
            break
        elif puzzle_input[x, y] == 9:
            break
        else:
            basin_points += [ (x, y) ]

    return basin_points

def return_basin_points_up(puzzle_input, point):
    x, y = point[0], point[1]
    basin_points = []

    while True:
        x -= 1
        if ( x < 0 ):
            break
        elif puzzle_input[x, y] == 9:
            break
        else:
            basin_points += [ (x, y) ]

    return basin_points