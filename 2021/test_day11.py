import pytest
import day11


@pytest.fixture
def example():
	s = '''11111
19991
19191
19991
11111
'''
	lines = s.split('\n')
	lines = [line.strip() for line in lines]
	matrix = [[int(x) for x in row] for row in lines]
	return matrix


def test_part1(example):
	assert day11.part1(example, 1) == 9
