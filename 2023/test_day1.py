import day1


def test_part2():
    lines = '''two1nine
eightwothree
abcone2threexyz
xtwone3four
4nineeightseven2
zoneight234
7pqrstsixteen
'''.strip().split('\n')
    assert day1.main2(lines) == 281
