#! python3
from collections import deque

def evaluate(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b
    elif op == '/':
        return a/b
    else:
        return None

def process_math(pfix):
    operations = ['+', '-', '*', '/']
    result = deque()
    for i in pfix:
        if i.isnumeric():
            result.append(int(i))
        else:
            temp2 = int(result.pop())
            temp1 = int(result.pop())
            result.append(evaluate(temp1, temp2, i))
    return result[0]


def postfix1(expression):
    operations = ['+', '-', '*', '/']
    # convert expression to postfix notation using deque as a queue
    # requires string to have spaces between operands and operators
    postfix_result = []
    operators = deque()
    temp_pop = None
    for index, item in enumerate(expression):
        # numbers go in the queue
        if item.isnumeric():
            postfix_result.append(item)
        # if stack empty or item is (, add to the queue
        elif len(operators) == 0 or operators[-1] == '(':
            operators.append(item)
        # if item is higher precedence operator than top of stack, put on stack
        elif item == '(':
            operators.append(item)
        elif item == ')':
            temp_pop = operators.pop()
            while temp_pop != '(':
                postfix_result.append(temp_pop)
                temp_pop = operators.pop()
        elif item in operations:
            temp_pop = operators.pop()
            while temp_pop == '(':
                postfix_result.append(temp_pop)
                temp_pop = operators.pop()
            operators.append(item)
            postfix_result.append(temp_pop)
        else:
            pass
    if len(operators) != 0:
        while len(operators) > 0:
            postfix_result.append(operators.pop())
    return postfix_result


def postfix2(expression):
    # convert expression to postfix notation using deque as a queue
    # requires string to have spaces between operands and operators
    precedence = {'*': 1, '/': 1, '+': 2, '-': 2}
    postfix_result = []
    operators = deque()
    temp_pop = None
    for index, item in enumerate(expression):
        # numbers go in the queue
        if item.isnumeric():
            postfix_result.append(item)
        # if stack empty or item is (, add to the queue
        elif len(operators) == 0 or operators[-1] == '(':
            operators.append(item)
        # if item is higher precedence operator than top of stack, put on stack
        elif item == '(':
            operators.append(item)
        elif item == ')':
            temp_pop = operators.pop()
            while temp_pop != '(':
                postfix_result.append(temp_pop)
                temp_pop = operators.pop()
        elif precedence[item] > precedence[operators[-1]]:
            operators.append(item)
        elif precedence[item] <= precedence[operators[-1]]:
            temp_pop = operators.pop()
            while precedence[temp_pop] < precedence[item] or temp_pop == '(':
                postfix_result.append(temp_pop)
                temp_pop = operators.pop()
            operators.append(item)
            postfix_result.append(temp_pop)
        else:
            pass
    if len(operators) != 0:
        while len(operators) > 0:
            postfix_result.append(operators.pop())
    return postfix_result


with open('input-Day18.txt') as f:
    lines = f.read().strip().split('\n')

values = []
values2 = []
for line in lines:
    equation = [x for x in line if x != ' ']
    rpn = postfix1(equation)
    values.append(process_math(rpn))

print(sum(values))

for line in lines:
    equation = [x for x in line if x != ' ']
    rpn2 = postfix2(equation)
    values2.append(process_math(rpn2))

print(sum(values2))
