import pytest
import day13



@pytest.fixture
def grid3():
	grid = [['.', '.', '.'], ['.', '#', '.'], ['.', '.', '.']]
	return grid


def test_get_new_matrix():
	assert day13.get_new_matrix(2, 2) == [['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']]


def test_check_line_is_empty(grid3):
	assert day13.check_line_is_empty('x', 0, grid3) is True
	#assert day13.check_line_is_empty('x', 1, grid3) is False
	#assert day13.check_line_is_empty('y', 1, grid3) is False
	assert day13.check_line_is_empty('y', 0, grid3) is True


def test_populate_dots(grid3):
	dot = [(0, 0)]
	assert day13.populate_dots(dot, grid3) == [['#', '.', '.'], ['.', '#', '.'], ['.', '.', '.']]

