import pytest
import day6


@pytest.fixture()
def example_input():
	l = [i for i in [3, 4, 3, 1, 2]]
	return l


def test_update_ages(example_input):
	assert day6.update_ages(example_input) == [2, 3, 2, 0, 1]


def test_new_fish():
	assert day6.new_fish([1]) == [1]
	assert day6.new_fish([-1]) == [6, 8]


def test_part1(example_input):
	assert day6.brute_force(example_input, 80) == 5934


def test_populate_fish_days(example_input):
	assert day6.populate_fish_days(example_input) == [0, 1, 1, 2, 1, 0, 0, 0, 0]


@pytest.mark.skip
def test_rotate_fish(example_input):
	one_day_rotated = [1, 1, 2, 1, 0, 0, 0, 0]
	two_days_rotated = [1, 2, 1, 0, 0, 1, 0, 1]
	assert day6.rotate_fish(example_input) == one_day_rotated
	assert day6.rotate_fish(one_day_rotated) == two_days_rotated


def test_simulate_lanternfish(example_input):
	assert day6.simulate_lanternfish(example_input, 18) == 26
	assert day6.simulate_lanternfish(example_input, 80) == 5934
