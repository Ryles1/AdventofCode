import time, sys

with open('day7.txt') as f:
    lines = f.readlines()

# populate dict with key:value as wire: input (list of strings)
inputs = {}
signals = {}
for instruction in lines:
    s = instruction.strip().split(' -> ')
    wire = s[1]
    inputs[wire] = s[0].split()


def get_signal(wire, start_time):
    current_input = inputs[wire]
    if not signals.get(wire):
        try:
            result = int(current_input[0])
            return result
        except ValueError:
            pass
        if len(current_input) == 1:
            result = get_signal(current_input[0], start_time)
        else:
            operation = current_input[-2]

            if operation == 'OR':
                result = get_signal(current_input[0], start_time) | get_signal(current_input[-1], start_time)
            elif operation == 'AND':
                result = get_signal(current_input[0], start_time) & get_signal(current_input[-1], start_time)
            elif operation == 'RSHIFT':
                shift_amount = int(current_input[-1])
                input_wire = get_signal(current_input[0], start_time)
                result = input_wire >> shift_amount
            elif operation == 'LSHIFT':
                shift_amount = int(current_input[-1])
                input_wire = get_signal(current_input[0], start_time)
                result = input_wire << shift_amount
            elif operation == 'NOT':
                input_wire = get_signal(current_input[0], start_time)
                result = ~input_wire & 0xffff
            signals[wire] = result
        return result

start = time.time()
print(get_signal('a', start))
