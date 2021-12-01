import pytest
import day1_2021


@pytest.fixture
def depth_increases_four_times():
	depths = [1, 2, 3, 4, 5]
	return depths


@pytest.fixture
def depth_decreases_only():
	depths = [5, 4, 3, 2, 1]
	return depths


@pytest.fixture
def empty_list():
	return []


def test_part1(depth_increases_four_times, depth_decreases_only, empty_list):
	assert day1_2021.part1(depth_increases_four_times) == 4
	four_increases = day1_2021.part1(depth_increases_four_times)
	assert four_increases == 4
	no_increases = day1_2021.part1(depth_decreases_only)
	assert no_increases == 0
	empty = day1_2021.part1(empty_list)
	assert empty == 0


def test_part2(depth_increases_four_times, depth_decreases_only, empty_list):
	two_window_increases = day1_2021.part2(depth_increases_four_times)
	assert two_window_increases == 2
	no_window_increases = day1_2021.part2(depth_decreases_only)
	assert no_window_increases == 0
	empty = day1_2021.part2(empty_list)
	assert empty == 0



