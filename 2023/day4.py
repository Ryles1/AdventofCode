class Card:
    def __init__(self, id, winning_nums, nums):
        self.id = id
        self.winning_nums = winning_nums
        self.nums = nums
        self.winning_num_count = len([i for i in self.nums if i in self.winning_nums])
        self.value = self.get_value()
        self.count_of_card = 1

    def get_value(self):
        value = 2 ** (self.winning_num_count - 1) if self.winning_num_count > 0 else 0
        return value


def main(lines):
    # part 1
    total_value = 0
    card_list = []
    for line in lines:
        split1 = line.split(':')
        card_id = int(split1[0].split(' ')[-1])
        nums = split1[1]
        winning_nums_str, card_nums_str = nums.split(' | ')
        winning_nums = [int(x.strip()) for x in winning_nums_str.split(' ') if x.isdigit()]
        card_nums = [int(x.strip()) for x in card_nums_str.split(' ') if x.isdigit()]
        card_list.append(Card(card_id, winning_nums, card_nums))
    for card in card_list:
        total_value += card.value

    # part 2
    total_cards = 0
    card_dict = {}
    # put cards in a dict for easy lookup and updating of values
    for card in card_list:
        card_dict[card.id] = card
    for id_num, card in card_dict.items():
        extra_cards = card.winning_num_count
        if extra_cards == 0:
            continue
        for card_number in range(id_num + 1, id_num + 1 + extra_cards):
            card_dict[card_number].count_of_card += card.count_of_card
    for id_num, card in card_dict.items():
        total_cards += card.count_of_card
    return total_value, total_cards


if __name__ == '__main__':
    with open('./input/day4.txt') as f:
        lines = f.read().strip().split('\n')

    answer1 = main(lines)
    print(answer1)
