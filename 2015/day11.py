INPUT = 'vzbxkghb'
ALPHABET = 'abcdefghijklmnopqrstuvwxyz'
ALPHABET_CHARS = [a for a in 'abcdefghijklmnopqrstuvwxyz']


def has_straight(s):
    for i in range(len(s) - 3):
        window = s[i: i+3]
        if window in ALPHABET:
            return True
    return False


def has_pairs(s):
    num_pairs = 0
    i = 0
    while i < len(s) - 1:
        window = s[i: i+2]
        if window[0] == window[1]:
            num_pairs += 1
            i += 2
        else:
            i += 1
        if num_pairs == 2:
            break
    return num_pairs >= 2


def all_valid_chars(s):
    if 'i' in s or 'o' in s or 'l' in s:
            return False
    return True


def is_valid_password(p):
    return all((all_valid_chars(p), has_pairs(p), has_straight(p)))


def increment_password(p):
    indices = [ALPHABET_CHARS.index(c) for c in p]
    indices = indices[::-1]
    for i, index_value in enumerate(indices):
        if index_value == len(ALPHABET_CHARS) - 1:
            indices[i] = 0
        else:
            indices[i] += 1
            break
    indices = indices[::-1]
    incremented_password = ''.join([ALPHABET_CHARS[j] for j in indices])
    return incremented_password


def choose_next_password(p):
    test_password = p
    while True:
        test_password = increment_password(test_password)
        if is_valid_password(test_password):
            break
    next_valid_password = test_password
    return next_valid_password


if __name__ == '__main__':
    next_password = choose_next_password(INPUT)
    print(next_password)
    next_password = choose_next_password(next_password)
    print(next_password)