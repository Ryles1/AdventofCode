#! python3
from collections import deque


def calculate_score(deck):
    map_list = [(i+1, v) for i, v in enumerate(deck)]
    score = sum(list(map(lambda x: x[0]*x[1], map_list)))
    return score


def part1(p1, p2):
    while len(p1) > 0 and len(p2) > 0:
        p1_card = p1.pop()
        p2_card = p2.pop()
        if p2_card > p1_card:
            p2.appendleft(p2_card)
            p2.appendleft(p1_card)
        elif p2_card < p1_card:
            p1.appendleft(p1_card)
            p1.appendleft(p2_card)
        else:
            print('There is a tie!')
            break
    return p1 if len(p2) == 0 else p2



if __name__ == '__main__':
    with open('input-Day22.txt') as f:
        players = f.read().strip().split('\n\n')

    player1_strings = players[0].split('\n')[1:]
    player2_strings = players[1].split('\n')[1:]

    # top of the deck is on the right side of the list
    player1_deck = deque(reversed([int(x) for x in player1_strings]))
    player2_deck = deque(reversed([int(x) for x in player2_strings]))

    part1_winning_deck = part1(player1_deck, player2_deck)
    part1_score = calculate_score(part1_winning_deck)
    print(part1_score)
