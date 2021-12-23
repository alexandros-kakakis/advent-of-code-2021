import numpy as np

def load_scanners():
    with open('./data/input_19.txt') as f:
        lines = f.read().split('\n\n')
        
    scanners = []
    for l in lines:
        scanner_arr = []
        scanner = l.splitlines()[1:]
        for beacon in scanner:
            scanner_arr.append( np.array( [ int(i) for i in beacon.split(',') ] ) )
            
        scanner_arr = np.array(scanner_arr)
        scanners.append(scanner_arr)

    return scanners


def return_scanner_graph(scanners):
    todo = [0]
    checked = []

    graph = []

    while todo:
        scanner = todo.pop()
        for other_scanner in range(len(scanners)):
            if scanner == other_scanner:
                continue

            if other_scanner in checked:
                continue
            
            beacons, overlapping_beacons = return_overlapping_beacons(scanners[scanner], scanners[other_scanner])
            if overlapping_beacons.size > 0:
                axes, signs = return_transformation_axes_signs(beacons, overlapping_beacons)
                position = ( beacons - transform_scanner(overlapping_beacons, axes, signs) )[0]
                
                scanners[other_scanner] = transform_scanner(scanners[other_scanner], axes, signs)
                todo.append(other_scanner)

                graph.append( (scanner, other_scanner, position) )

        checked.append(scanner)

    return graph


def return_overlapping_beacons(scanner, other_scanner):
    beacons = []
    corresponding_beacons = []

    for beacon in scanner:
        for other_beacon in other_scanner:
            distances = return_distances(scanner, beacon)
            other_distances = return_distances(other_scanner, other_beacon)

            overlap = set(distances).intersection( set(other_distances) )

            if len( overlap ) >= 12:
                beacons.append(beacon)
                corresponding_beacons.append(other_beacon)

    beacons = np.array(beacons)
    corresponding_beacons = np.array(corresponding_beacons)
    return beacons, corresponding_beacons


def return_distances(scanner, beacon):
    distances = []
    differences = scanner - beacon
    for diff in differences:
        distance = sum( [ d ** 2 for d in diff ] )
        distances.append(distance)

    return distances


def transform_scanner(scanner, axes=[0, 1, 2], signs=[1, 1, 1]):
    x = scanner[:, axes[0]] * signs[0]
    y = scanner[:, axes[1]] * signs[1]
    z = scanner[:, axes[2]] * signs[2]
    
    for i in range(len(scanner)):
        scanner[i, :] = np.array( [x[i], y[i], z[i]] )

    return scanner


def return_transformation_axes_signs(beacons, corresponding_beacons):
    axes = []
    signs = []

    for axis in [0, 1, 2]:
        for other_axis in [0, 1, 2]:
            for sign in [-1, 1]:
                delta = beacons[:, axis] - sign * corresponding_beacons[:, other_axis]
                if len( np.unique(delta) ) == 1:
                    axes.append(other_axis)
                    signs.append(sign)
    return axes, signs


def find_zero_position(scanner, graph, position=np.array([0, 0, 0])):
    if scanner == 0:
        return position

    else:
        prev_nodes = [ i for i in graph if i[1] == scanner ]
        zero_node = [ i for i in prev_nodes if i[0] == 0 ]

        if zero_node:
            position = position + zero_node[0][2]
            return position
        else:
            scanner = prev_nodes[0][0]
            position = position + prev_nodes[0][2]
            return find_zero_position(scanner, graph, position)

scanners = load_scanners()
scanner_graph = return_scanner_graph(scanners)

positions = { i: find_zero_position(i, scanner_graph) for i in range(len(scanners))}

# Part One
all_beacons = scanners[0]

for scanner, position in positions.items():
    if scanner == 0:
        continue
    
    corrected_beacons = scanners[scanner] + position
    all_beacons = np.vstack([all_beacons, corrected_beacons])

all_beacons = np.unique( all_beacons, axis=0 )
print('Part One:', len(all_beacons))

## Part Two
largest_distance = 0
all_positions = [ i for i in positions.values() ]
for scanner in all_positions:
    for other_scanner in all_positions:
        largest_distance = max( sum([ abs(i) for i in scanner - other_scanner ]), largest_distance )

print('Part Two:', largest_distance)
