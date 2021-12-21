STARTING_POSITION = [7, 8]

## Part One 
WINNING_SCORE = 1000

position = STARTING_POSITION[:]
score = [0, 0]
middle_dice = 2
player = 0 # zero-indexing players

while True:
    pos = ( position[player] + middle_dice * 3 ) % 10
    pos = 10 if pos == 0 else pos

    position[player] = pos
    score[player] += pos
    
    if score[player] >= WINNING_SCORE:
        break

    middle_dice += 3
    player = 1 - player

print('Part One:', min(score) * ( middle_dice + 1 ) )

## Part Two
WINNING_SCORE = 21

n_winning_scenarios = [0, 0]
dice_outcome = {3: 1, 4: 3, 5: 6, 6: 7, 7: 6, 8: 3, 9: 1}
scenario_dict = { ((STARTING_POSITION[0], 0), (STARTING_POSITION[1], 0)): 1 }
    
player = 0 # zero-indexing players

while len(scenario_dict) > 0:
    next_scenario_dict = {}
    for scenario, n_scenario in scenario_dict.items():
        for outcome, n_outcome in dice_outcome.items():

            position = ( scenario[player][0] + outcome ) % 10
            position = 10 if position == 0 else position

            score = scenario[player][1] + position

            if score >= WINNING_SCORE:
                n_winning_scenarios[player] += n_outcome * n_scenario
            else:
                if player == 0:
                    next_scenario = ((position, score), scenario[1])
                    next_scenario_dict[ next_scenario ] = next_scenario_dict.get(next_scenario, 0) + n_outcome * n_scenario
                else:
                    next_scenario = (scenario[0], (position, score))
                    next_scenario_dict[ next_scenario ] = next_scenario_dict.get(next_scenario, 0) +  n_outcome * n_scenario
                    
    player = 1 - player
    scenario_dict = next_scenario_dict

print('Part Two:', max(n_winning_scenarios))
