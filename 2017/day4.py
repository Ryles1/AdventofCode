def phrase_has_no_repeated_elements(phrase):
    pieces = phrase.strip().split()
    count_uniques = len(set(pieces))
    if len(pieces) == count_uniques:
        return True
    return False


def phrase_has_no_rearrangable_elements(phrase):
    pieces = phrase.strip().split()
    pieces_sets = [set(piece) for piece in pieces]
    for i, s in enumerate(pieces_sets):
        # check for duplicate set in the rest of the list
        if s in pieces_sets[:i] or s in pieces_sets[i + 1:]:
            return False
    return True


def main(phrases):
    phrases_with_no_repeated_elements = 0
    for phrase in phrases:
        if phrase_has_no_repeated_elements(phrase):
            phrases_with_no_repeated_elements += 1
    print(phrases_with_no_repeated_elements)
    phrases_with_no_elements_that_can_be_rearranged = 0
    for phrase in phrases:
        if phrase_has_no_rearrangable_elements(phrase):
            phrases_with_no_elements_that_can_be_rearranged += 1
    print(phrases_with_no_elements_that_can_be_rearranged)
    return


if __name__ == '__main__':
    with open('./input/day4.txt') as f:
        lines = f.readlines()

    main(lines)