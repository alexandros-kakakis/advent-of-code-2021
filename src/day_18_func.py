import re

NON_NUMBERIC_CHAR = ['[', ']', ',']

def pprint_number(number):
    print(''.join(number))

def explode_number(number):
    n_brackets = 0
    for idx, char in enumerate(number):

        if char == '[':
            n_brackets += 1
        elif char == ']':
            n_brackets -= 1
        else:
            pass

        if n_brackets == 5:
            break

    left, right = number[idx+1], number[idx+3]

    idx_l = [ i for (i, char) in enumerate(number[:idx]) if char not in NON_NUMBERIC_CHAR ]
    if len(idx_l) > 0:
        idx_l = idx_l[-1]
        number[idx_l] = str(int(number[idx_l]) + int(left))

    idx_r = [ i for (i, char) in enumerate(number[idx+4:]) if char not in NON_NUMBERIC_CHAR ]
    if len(idx_r) > 0:
        idx_r = idx_r[0] + idx + 4
        number[idx_r] = str(int(number[idx_r]) + int(right))

    number[idx:idx+5] = str(0)
    return number

def check_explode(number):
    n_brackets = 0
    for idx, char in enumerate(number):

        if char == '[':
            n_brackets += 1
        elif char == ']':
            n_brackets -= 1
        else:
            pass

        if n_brackets == 5:
            return True
    return False

def check_split(number):
    return ( max( [ len(char) for char in number ] ) == 2 )

def split_number(number):
    idx = [ idx for (idx, char) in enumerate(number) if len(char) == 2 ][0]
    split_nr = int( number[idx] )
    left = split_nr // 2
    right = split_nr - left

    insert = [ '[', str(left), ',', str(right), ']' ]
    number = number[:idx] + insert + number[idx+1:]
    return number


def reduce_number(number):
    while True:
        if check_explode(number):
            number = explode_number(number)
        elif check_split(number):
            number = split_number(number)
        else:
            break

    return number

def add_numbers(number_l, number_r):
    number_l = parse_number(number_l)
    number_r = parse_number(number_r)
    return ['['] + number_l + [','] + number_r + [']']

def parse_number(number):
    return [ char for char in str(number) if char != ' ' ]

def calculate_magnitude(number):
    pair_dict = {}

    while '[' in number:
        pairs = re.findall('\[[0-9]+\,\s{0,1}[0-9]+\]', number)

        for pair in pairs:
            if pair in pair_dict.keys():
                continue

            nrs = re.findall('[0-9]+', pair)
            res = str( int( nrs[0] ) * 3 + int( nrs[1] ) * 2 )
            pair_dict[pair] = res

        for i, j in pair_dict.items():
            number = number.replace(i, j)

    return int(number)