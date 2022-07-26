with open('./input/day7.txt') as f:
    lines = f.readlines()

# populate dict with key:value as wire: input (list of strings)
inputs = {}
signals = {}
for instruction in lines:
    s = instruction.strip().split(' -> ')
    wire = s[1]
    inputs[wire] = s[0].split()


def get_signal(wire):
    current_input = inputs[wire]
    result = signals.get(wire)
    if not result:
        if len(current_input) == 1:
            try:
                result = int(current_input[0])
            except ValueError:
                result = get_signal(current_input[0])
        else:
            operation = current_input[-2]
            if operation in ['OR', 'AND']:
                first_signal, second_signal = current_input[0], current_input[2]
                try:
                    first_result = int(first_signal)
                except ValueError:
                    first_result = get_signal(first_signal)

                try:
                    second_result = int(second_signal)
                except ValueError:
                    second_result = get_signal(second_signal)

                if operation == 'OR':
                    result = first_result | second_result
                elif operation == 'AND':
                    result = first_result & second_result
            elif operation == 'RSHIFT':
                shift_amount = int(current_input[-1])
                input_wire = get_signal(current_input[0])
                result = input_wire >> shift_amount
            elif operation == 'LSHIFT':
                shift_amount = int(current_input[-1])
                input_wire = get_signal(current_input[0])
                result = input_wire << shift_amount
            elif operation == 'NOT':
                input_wire = get_signal(current_input[1])
                result = ~input_wire & 0xffff
            signals[wire] = result
    return result


a1 = get_signal('a')
print(a1)

signals = {}
signals['b'] = a1

a2 = get_signal('a')
print(a2)
