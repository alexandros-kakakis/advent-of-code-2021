from helper_functions import read_input_as_list

instructions = read_input_as_list('./data/input_24.txt')

## the following block repeats 14 times
# inp w
# mul x 0
# add x z
# mod x 26
# div z {a}
# add x {b}
# eql x w
# eql x 0
# mul y 0
# add y 25
# mul y x
# add y 1
# mul z y
# mul y 0
# add y w
# add y {z}
# mul y x
# add z y

BLOCK_SIZE = 18

a_values = [ int(instructions[i].split()[-1]) for i in [ 4 + BLOCK_SIZE * i for i in range(14) ] ] 
b_values = [ int(instructions[i].split()[-1]) for i in [ 5 + BLOCK_SIZE * i for i in range(14) ] ]
c_values = [ int(instructions[i].split()[-1]) for i in [ 15 + BLOCK_SIZE * i for i in range(14) ] ]

checked = []
while len(checked) != 14:
    for i, a, b, c in zip(range(BLOCK_SIZE), a_values, b_values, c_values):
        if i in checked:
            continue

        if a == 1:
            push = i
            c_ = c

        if a == 26:
            pop = i
            print('W{} = W{} + {}'.format(pop, push, b + c_))
            checked.append(push)
            checked.append(pop)
            break