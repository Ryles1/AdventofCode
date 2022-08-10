import itertools


INPUT = '1113222113'
# use regex or itertools.groupby


def look_and_say(s):
    """This function works by using the groupby function from itertools.
    groupby processes every element in an iterable and performs a function to generate the keys for a
    grouper iterable.
    In this case the function is left as the default (None), so it returns the identity of the element as the key.
    It generates a new grouper iterable every time the value of the key function (in this case the value of the element)
    changes.
    """
    new_s = []
    for k, v in itertools.groupby(s):
        s_part = str(len(list(v))) + str(k)
        new_s.append(s_part)
    new_string = ''.join(new_s)
    return new_string


s = INPUT
for iteration in range(50):
    s = look_and_say(s)
    if iteration == 39 or iteration == 49:
        print(len(s))


