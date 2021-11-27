VOWELS = "aeiou"
bad_strings = ["ab", "cd", "pq", "xy"]


with open("day5.txt") as f:
    words = f.readlines()


def part1():
    nice_strings = 0
    for word in words:
        vowel_count = 0
        no_bad_string = True
        double_letter = False
        for c in word:
            vowel_count += 1 if c in VOWELS else 0
        for i in range(len(word) - 2):
            pair = word[i : i + 2]
            if pair in bad_strings:
                no_bad_string = False
            if pair[0] == pair[1]:
                double_letter = True

        nice = all([vowel_count >= 3, double_letter, no_bad_string])
        nice_strings += 1 if nice else 0
    print(nice_strings)


def part2():
    nice_strings = 0
    for word in words:
        pair_twice = False
        repeat_with_one_between = False
        # check for repeating pair (eg 'xyxy', but not 'aaa')
        # check each pair of letters in the slice of the string before and after them
        for i in range(len(word) - 2):
            pair = word[i : i + 2]
            before_pair = word[:i]
            after_pair = word[i + 2 :]
            if pair in before_pair or pair in after_pair:
                pair_twice = True
        # check for letter which repeats with exactly one letter in between eg 'xyx'
        for j in range(len(word) - 3):
            three_letters = word[j : j + 3]
            if three_letters[0] == three_letters[2]:
                repeat_with_one_between = True
        nice = all([pair_twice, repeat_with_one_between])
        nice_strings += 1 if nice else 0
    print(nice_strings)


part1()
part2()
