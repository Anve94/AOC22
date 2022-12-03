choice_score_mapping = {
    'X': 1, # Rock
    'Y': 2, # Paper
    'Z': 3  # Scissors
}

winner_mapping = {
    'A': 'Y', # Rock is beat by paper
    'B': 'Z', # Paper is beat by scissors
    'C': 'X'  # Scissors is beat by rock
}

draw_mapping = {
    'A': 'X',
    'B': 'Y',
    'C': 'Z'
}

lose_mapping = {
    'A': 'Z',
    'B': 'X',
    'C': 'Y'
}

matchup_score_mapping = {
    'win': 6,
    'draw': 3,
    'lose': 0
}

match_determinates = {
    'X': 'lose',
    'Y': 'draw',
    'Z': 'win'
}

decision_mapping = {
    'A': {
        'win': winner_mapping.get('A'),
        'draw': draw_mapping.get('A'),
        'lose': lose_mapping.get('A')
    },
    'B': {
        'win': winner_mapping.get('B'),
        'draw': draw_mapping.get('B'),
        'lose': lose_mapping.get('B')
    },
    'C': {
        'win': winner_mapping.get('C'),
        'draw': draw_mapping.get('C'),
        'lose': lose_mapping.get('C')
    }
}

def input_to_strategy_list() -> list:
    strategy_list = []
    with open('02-1.txt', 'r') as f:
        for line in f:
            found = line.rstrip('\n').split()
            strategy_list.append(found)
            
    return strategy_list

def calculate_score(strategy_list: list) -> int:
    score = 0
    for matchup in strategy_list:
        score += choice_score(matchup) + match_score(matchup)
    
    return score

def calculate_score_with_condition(strategy_list: list) -> int:
    score = 0
    for strategy in strategy_list:
        recommended_outcome = match_determinates.get(strategy[1])
        conditions = decision_mapping.get(strategy[0])
        my_choice = conditions.get(recommended_outcome)
        matchup = [strategy[0], my_choice]
        score += choice_score(matchup) + match_score(matchup)
    return score

def choice_score(matchup: list) -> int:
    return choice_score_mapping.get(matchup[1])

def match_score(matchup: list) -> int:
    # I'm assuming we will win most but not all matchups, so checking wins first should be
    # more efficient, or the elf was lying :(
    if winner_mapping.get(matchup[0]) == matchup[1]:
        # Win
        return matchup_score_mapping.get('win')

    if draw_mapping.get(matchup[0]) == matchup[1]:
        # Draw
        return matchup_score_mapping.get('draw')
    
    # Lost
    return matchup_score_mapping.get('lose')

# Part 1
strategy_list = input_to_strategy_list()
score = calculate_score(strategy_list)
print(f'Total score using the provided strategy list when assuming XYZ means choice is {score}')

# Part 2
score = calculate_score_with_condition(strategy_list)
print(f'Total score using the provided strategy list when assuming XYZ means match outcome is {score}')