def read_input_as_list(filepath='./data/input.txt'):

    with open(filepath, 'r') as f:
        lines = f.read().splitlines()

    return lines