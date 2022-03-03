import pytest
import day24


@pytest.fixture()
def instructions():
	with open('./input/day24.txt') as f:
		lines = f.readlines()
	return lines


@pytest.fixture
def data(instructions):
	d = day24.parse_instructions(instructions)
	return d


def test_calculate(data):
	n = (9,9,1,1,1,9,1,)
	assert day24.calculate(data, n) == 0

