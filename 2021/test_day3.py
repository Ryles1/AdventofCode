import pytest
import day3_2021


@pytest.fixture
def part1_example():
	bytes_str = '''00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010'''
	return bytes_str.split('\n')


def test_part1(part1_example):
	assert day3_2021.part1(part1_example) == 198


def test_get_most_common(part1_example):
	assert day3_2021.get_most_common(part1_example, 0) == '1'


def test_get_least_common(part1_example):
	assert day3_2021.get_least_common(part1_example, 0) == '0'


def test_get_CO2_rating_base2(part1_example):
	assert day3_2021.get_CO2_rating_base2(part1_example) == '01010'


def test_get_O2_rating_base2(part1_example):
	assert day3_2021.get_O2_rating_base2(part1_example) == '10111'


def test_part2(part1_example):
	assert day3_2021.part2(part1_example) == 230
