
def generate_number_dict(values):
    number_dict = dict()

    ## easy digits
    one = filter_values(values, n_segments=2)[0]
    number_dict[one] = 1

    seven = filter_values(values, n_segments=3)[0]
    number_dict[seven] = 7

    four = filter_values(values, n_segments=4)[0]
    number_dict[four] = 4

    eight = filter_values(values, n_segments=7)[0]
    number_dict[eight] = 8

    ## six segments
    val = filter_values(values, n_segments=6)

    res = [ i for i in val if len( set(seven) - set(i) ) > 0 ][0]
    number_dict[res] = 6
    val = [ i for i in val if i not in res ]

    res = [ i for i in val if len( set(four) - set(i) ) > 0 ][0]
    number_dict[res] = 0

    res = [ i for i in val if i not in res ][0]
    number_dict[res] = 9

    ## five segments
    val = filter_values(values, n_segments=5)

    res = [ i for i in val if len( set(seven) - set(i) ) == 0 ][0]
    number_dict[res] = 3
    val = [ i for i in val if i not in res ]

    res = [ i for i in val if len( set(four).intersection(set(i)) ) == 3 ][0]
    number_dict[res] = 5

    res = [ i for i in val if len( set(four).intersection(set(i)) ) == 2 ][0]
    number_dict[res] = 2
    
    return number_dict


def filter_values(values, n_segments):
    return [ i for i in values if len(i) == n_segments ]

def sort_signals(values):
    return [ ''.join(sorted(i))for i in values ]