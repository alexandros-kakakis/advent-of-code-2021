from helper_functions import read_input_as_list

puzzle_input = read_input_as_list('./data/input_12.txt')
puzzle_input = [ i.split('-') for i in puzzle_input ]

cave_dict = dict()

for connection in puzzle_input:

    if connection[0] not in cave_dict.keys():
        cave_dict[connection[0]] = [ connection[1] ]
    else:
        cave_dict[connection[0]].append(connection[1])

    if connection[1] not in cave_dict.keys():
        cave_dict[connection[1]] = [ connection[0] ]
    else:
        cave_dict[connection[1]].append(connection[0])

cave_dict.pop('end')

def collect_paths(cave_dict, current_path, cave_to_visit_twice=''):
    global paths

    if current_path[-1] == 'end':
        paths.append(current_path)
        return

    options = cave_dict[current_path[-1]]
    for option in options:
        if option.islower():
            if option not in current_path:
                collect_paths(cave_dict, current_path + [ option ], cave_to_visit_twice)
            elif option == cave_to_visit_twice:
                collect_paths(cave_dict, current_path + [ option ], cave_to_visit_twice='')
        else:
            collect_paths(cave_dict, current_path + [ option ], cave_to_visit_twice)

    return


## Part One
paths = []
collect_paths(cave_dict, current_path=['start'], cave_to_visit_twice='')
n_paths = len( paths )

print('Part One:', n_paths)

## Part Two
small_caves = [ i for i in cave_dict.keys() if i.islower() and i != 'start' ]
additional_paths = 0

for cave in small_caves:
    paths = []
    collect_paths(cave_dict, current_path=['start'], cave_to_visit_twice=cave)
    additional_paths += len( paths ) - n_paths

print('Part Two:', n_paths + additional_paths)
