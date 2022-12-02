# OPPONENT SHAPES
ROCK_OPP = 'A'
PAPER_OPP = 'B'
SCISSORS_OPP = 'C'

# MY SHAPE
ROCK_ME = 'X'
PAPER_ME = 'Y'
SCISSORS_ME = 'Z'

SCORE_GAME = {'WIN': 6, 'LOSE': 0, 'DRAW': 3}
SCORE_ME = {ROCK_ME: 1,
            PAPER_ME: 2,
            SCISSORS_ME: 3}
possible_games = {(ROCK_OPP, ROCK_ME): 'DRAW',
                  (ROCK_OPP, PAPER_ME): 'WIN',
                  (ROCK_OPP, SCISSORS_ME): 'LOSE',
                  (PAPER_OPP, ROCK_ME): 'LOSE',
                  (PAPER_OPP, PAPER_ME): 'DRAW',
                  (PAPER_OPP, SCISSORS_ME): 'WIN',
                  (SCISSORS_OPP, ROCK_ME): 'WIN',
                  (SCISSORS_OPP, PAPER_ME): 'LOSE',
                  (SCISSORS_OPP, SCISSORS_ME): 'DRAW'}

choices_to_satisfy_outcomes = {(ROCK_OPP, 'DRAW'): ROCK_ME,
                  (ROCK_OPP, 'WIN'): PAPER_ME,
                  (ROCK_OPP, 'LOSE'): SCISSORS_ME,
                  (PAPER_OPP, 'DRAW'): PAPER_ME,
                  (PAPER_OPP, 'WIN'): SCISSORS_ME,
                  (PAPER_OPP, 'LOSE'): ROCK_ME,
                  (SCISSORS_OPP, 'DRAW'): SCISSORS_ME,
                  (SCISSORS_OPP, 'WIN'): ROCK_ME,
                  (SCISSORS_OPP, 'LOSE'): PAPER_ME}


def part1(lines):
    score = 0
    for line in lines:
        opp, me = line.strip().split()
        game = (opp, me)
        outcome = possible_games[game]
        score += (SCORE_ME[me] + SCORE_GAME[outcome])
    return score


def part2(lines):
    score = 0
    outcomes = {'X': 'LOSE',
                'Y': 'DRAW',
                'Z': 'WIN'}
    for line in lines:
        opp, outcome_letter = line.strip().split()
        outcome = outcomes[outcome_letter]
        outcome_score = SCORE_GAME[outcome]
        choice_required = choices_to_satisfy_outcomes[(opp, outcome)]
        choice_score = SCORE_ME[choice_required]
        score += (outcome_score + choice_score)
    return score
        
        
if __name__ == '__main__':
    with open('./input/day2.txt') as f:
        lines = f.readlines()

    print(part1(lines))
    print(part2(lines))
