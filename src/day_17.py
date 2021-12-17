class Probe:

    def __init__(self, initial_position, initial_velocity):
        self.position = initial_position
        self.velocity = initial_velocity
        self.target_area = False

    def launch(self):
        x = self.position[0] + self.velocity[0]
        y = self.position[1] + self.velocity[1]
        self.position = (x, y)
        
        x = max( self.velocity[0] - 1, 0 )
        y = self.velocity[1] - 1
        self.velocity = (x, y)

    def check_target(self):
        x, y = self.position
        
        x_target = ( X_TARGET[0] <= x <= X_TARGET[1] )
        y_target = ( Y_TARGET[0] <= y <= Y_TARGET[1] )
        
        self.target_area = x_target and y_target

# target area: x=139..187, y=-148..-89
X_TARGET = [139, 187]
Y_TARGET = [-148, -89]
S = (0, 0)

Y_LIM = X_TARGET[1] - Y_TARGET[1] - 1
MAX_ITER = 296 # n steps highest probe

global_highest = 0
n_values = 0

for x in range(1, X_TARGET[1]+1):
    for y in range(Y_TARGET[0], Y_LIM):
        probe = Probe(S, (x, y))
        highest = probe.position[1]

        for _ in range(MAX_ITER):
            probe.launch()
            probe.check_target()
            highest = max( probe.position[1], highest )

            if probe.position[0] > X_TARGET[1]:
                break
            
            if probe.position[1] < Y_TARGET[0]:
                break
            
            if probe.target_area:
                global_highest = max( highest, global_highest )
                n_values += 1
                break

## Part One
print('Part One:', global_highest)

## Part Two
print('Part Two:', n_values)
