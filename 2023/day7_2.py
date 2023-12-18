VALUES = {'2': 2,
          '3': 3,
          '4': 4,
          '5': 5,
          '6': 6,
          '7': 7,
          '8': 8,
          '9': 9,
          'T': 10,
          'J': 1,
          'Q': 11,
          'K': 12,
          'A': 13}
HAND_TYPES = ['HC', '1P', '2P', '3K', 'FH', '4K', '5K']


class Hand:
    def __init__(self, s, bid):
        self.hand = [i for i in s]
        if 'J' not in self.hand:
            self.hand_type = self.get_hand_type()
        else:
            self.hand_type = self.get_hand_type_joker()
        self.high_card = self.get_high_card()
        self.bid = int(bid)

    def get_hand_type_joker(self):
        joker_count = self.hand.count('J')
        set_of_cards = set(self.hand)
        card_counts = [self.hand.count(i) for i in list(set_of_cards)]
        if len(set_of_cards) == 1 or len(set_of_cards) == 2:
            return '5K'
        elif len(set_of_cards) == 5:
            return '1P'
        elif len(set_of_cards) == 4:
            return '3K'
        elif len(set_of_cards) == 3:
            if joker_count == 3:
                return '4K'
            elif joker_count == 2:
                return '4K'
            elif joker_count == 1:
                if 3 in card_counts:
                    return '4K'
                elif 2 in card_counts:
                    return 'FH'


    def get_hand_type(self):
        set_of_cards = set(self.hand)
        if len(set_of_cards) == 1:
            return '5K'
        elif len(set_of_cards) == 4:
            return '1P'
        elif len(set_of_cards) == 3:
            list_set_of_cards = list(set_of_cards)
            twos = 0
            for i, card in enumerate(list_set_of_cards):
                if self.hand.count(card) == 3:
                    return '3K'
                elif self.hand.count(card) == 2:
                    twos += 1
            if twos == 2:
                return '2P'
        elif len(set_of_cards) == 2:
            list_set_of_cards = list(set_of_cards)
            if self.hand.count(list_set_of_cards[0]) == 4 or self.hand.count(list_set_of_cards[1]) == 4:
                return '4K'
            elif self.hand.count(list_set_of_cards[0]) == 3 or self.hand.count(list_set_of_cards[1]) == 3:
                if self.hand.count(list_set_of_cards[0]) == 2 or self.hand.count(list_set_of_cards[1]) == 2:
                    return 'FH'
                else:
                    return '3K'
            elif self.hand.count(list_set_of_cards[0]) == 2 or self.hand.count(list_set_of_cards[1]) == 2:
                if self.hand.count(list_set_of_cards[1]) == 3 or self.hand.count(list_set_of_cards[0]) == 3:
                    return 'FH'
            else:
                return '2P'
        else:
            return 'HC'

    def get_high_card(self):
        sorted_cards = sorted(self.hand, key=lambda x: VALUES[x], reverse=True)
        return sorted_cards[0]


def is_stronger_than(hand1, hand2):
    hand1_strength = HAND_TYPES.index(hand1.hand_type)
    hand2_strength = HAND_TYPES.index(hand2.hand_type)
    if hand1_strength == hand2_strength:
        i = 0
        while i < len(hand1.hand):
            hand1_val = VALUES[hand1.hand[i]]
            hand2_val = VALUES[hand2.hand[i]]
            if hand1_val > hand2_val:
                return True
            elif hand1_val < hand2_val:
                return False
            else:
                i += 1
        return False
    elif hand1_strength > hand2_strength:
        return True
    else:
        return False


def main(lines):
    hands = []
    for line in lines:
        hand_string, bid = line.strip('\n').split()
        hand = Hand(hand_string, bid)
        hands.append(hand)
    for i in range(len(hands)):
        swapped = False
        for j in range(0, len(hands) - i - 1):
            hand1 = hands[j]
            hand2 = hands[j + 1]
            if is_stronger_than(hand1, hand2):
                hands[j], hands[j + 1] = hands[j + 1], hands[j]
                swapped = True
        if not swapped:
            break
    score = 0
    for j, hand in enumerate(hands):
        score += hand.bid * (j + 1)
    return score


if __name__ == '__main__':
    with open('./input/day7.txt') as f:
        lines = f.read().strip().split('\n')

    answer1 = main(lines)
    print(answer1)
