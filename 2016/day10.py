from math import prod


VALUE1 = 61
VALUE2 = 17


def initialize(lines):
    bots_outputs = {}
    for line in lines:
        if 'goes to' in line:
            split = line.split()
            value = int(split[1])
            bot = 'bot' + split[-1]
            bots_outputs.setdefault(bot, {'values': [],
                                  'gives low': None,
                                  'gives high': None})
            bots_outputs[bot]['values'].append(value)
        else:
            split = line.split()
            bot = 'bot' + split[1]
            bots_outputs.setdefault(bot, {'values': [],
                                  'gives low': None,
                                  'gives high': None})
            low = split[5] + split[6]
            bots_outputs.setdefault(low, {'values': [],
                                  'gives low': None,
                                  'gives high': None})
            high = split[-2] + split[-1]
            bots_outputs.setdefault(high, {'values': [],
                                  'gives low': None,
                                  'gives high': None})
            bots_outputs[bot]['gives low'] = low
            bots_outputs[bot]['gives high'] = high
    return bots_outputs


def process(old_bots):
    bots = old_bots.copy()
    answer1 = None
    while not answer1:
        for bot in bots:
            if 'output' in bot:
                continue
            values = bots[bot]['values']
            if VALUE2 in values and VALUE1 in values:
                print(f'answer1 is {bot}, {bots[bot]}')
                answer1 = bot
                break
            if len(values) == 2:
                maxval = max(values)
                minval = min(values)
                gives_high_bot = bots[bot]['gives high']
                gives_low_bot = bots[bot]['gives low']
                bots[bot]['values'] = []
                bots[gives_high_bot]['values'].append(maxval)
                bots[gives_low_bot]['values'].append(minval)
    answer2 = None
    while not answer2:
        for bot in bots:
            if 'output' in bot:
                continue
            values = bots[bot]['values']
            if len(values) == 2:
                maxval = max(values)
                minval = min(values)
                gives_high_bot = bots[bot]['gives high']
                gives_low_bot = bots[bot]['gives low']
                bots[bot]['values'] = []
                bots[gives_high_bot]['values'].append(maxval)
                bots[gives_low_bot]['values'].append(minval)
            output0_values = bots['output0']['values']
            output1_values = bots['output1']['values']
            output2_values = bots['output2']['values']
            if all([output0_values, output1_values, output2_values]):
                answer2 = prod([output0_values[0], output2_values[0], output1_values[0]])
                break
    return answer1, answer2


def main(lines):
    bots_outputs = initialize(lines)
    answer1, answer2 = process(bots_outputs)
    return answer1, answer2


if __name__ == '__main__':
    with open('./input/day10.txt') as f:
        lines = f.readlines()
    print(main(lines))
