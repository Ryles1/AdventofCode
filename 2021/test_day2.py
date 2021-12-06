import pytest
import day2_2021


@pytest.fixture
def day2_example():
	commands = '''forward 5
down 5
forward 8
up 3
down 8
forward 2'''
	return commands.split('\n')


def test_part1(day2_example):
	assert day2_2021.part1(day2_example) == 150


def test_part2(day2_example):
	assert day2_2021.part2(day2_example) == 900
