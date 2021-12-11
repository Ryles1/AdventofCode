import pytest
import day10


@pytest.fixture()
def example_input():
	example_str = r'''[({(<(())[]>[[{[]{<()<>>
	[(()[<>])]({[<{<<[]>>(
	{([(<{}[<>[]}>{[]{[(<()>
	(((({<>}<{<{<>}{[]{[]{}
	[[<[([]))<([[{}[[()]]]
	[{[{({}]{}}([{[{{{}}([]
	{<[[]]>}<{[{[{[]{()[[[]
	[<(<(<(<{}))><([]([]()
	<{([([[(<>()){}]>(<<{{
	<{([{{}}[<[[[<>{}]]]>[]]
	'''
	return [line.strip() for line in example_str]


def test_check_line():
	complete_line = '<([{}])>'
	assert day10.check_line(complete_line) == ''
	corrupt = '(]'
	assert day10.check_line(corrupt) == ']'


def test_calculate_score():
	count = {')': 2,
		  ']': 1,
		  '}': 1,
		  '>': 1}
	assert day10.calculate_score(count) == 26397


def test_part1(example_input):
	example_lines = [line.strip() for line in example_input]
	assert day10.part1(example_lines) == 26397


def test_update_score():
	assert day10.update_score('}}]])})]') == 288957
	assert day10.update_score(')}>]})') == 5566
	assert day10.update_score('}}>}>))))') == 1480781
	assert day10.update_score(']]}}]}]}>') == 995444
	assert day10.update_score('])}>') == 294


def test_complete_line():
	assert day10.complete_line('[({(<(())[]>[[{[]{<()<>>') == '}}]])})]'
