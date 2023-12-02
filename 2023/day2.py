import parse
import re

BAG_CONTENTS = {'red': 12, 'green': 13, 'blue': 14}


class Game:
    def __init__(self, number, red, green, blue):
        self.ID = number
        self.red = red
        self.green = green
        self.blue = blue
        self.total = red + green + blue
        self.is_possible = self._is_possible()

    def _is_possible(self):
        if any([True for x in self.red if x > BAG_CONTENTS['red']]):
            return False
        if any([True for x in self.green if x > BAG_CONTENTS['green']]):
            return False
        if any([True for x in self.blue if x > BAG_CONTENTS['blue']]):
            return False
        return True

    def _fewest_possible_cubes(self):
        red_min = max(self.red)
        green_min = max(self.green)
        blue_min = max(self.blue)
        return (red_min, green_min, blue_min)

    def power_of_fewest_cubes(self):
        red, green, blue = self._fewest_possible_cubes()
        return red * green * blue


def main(lines):
    games_list = []
    possible_games_count = 0
    for line in lines:
        # parse line
        game_num = int(parse.search('Game {}:', line)[0])
        red_match = re.findall(r'\d+ red', line)
        reds = [int(x.split(' ')[0]) for x in red_match]

        green_match = re.findall(r'\d+ green', line)
        greens = [int(x.split(' ')[0]) for x in green_match]

        blue_match = re.findall(r'\d+ blue', line)
        blues = [int(x.split(' ')[0]) for x in blue_match]

        games_list.append(Game(game_num, reds, greens, blues))
    for game in games_list:
        possible_games_count += game.ID if game.is_possible else 0
    power_sum = 0
    for game in games_list:
        power_sum += game.power_of_fewest_cubes()
    return possible_games_count, power_sum


if __name__ == '__main__':
    with open('./input/day2.txt') as f:
        lines = f.read().strip().split('\n')

    answer1 = main(lines)
    print(answer1)
