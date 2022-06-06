import pytest
import day1


@pytest.fixture
def test1():
    instructions = 'R2, L3'.split(',')
    instructions = [line.strip() for line in instructions]
    return instructions


@pytest.fixture
def test2():
    instructions = 'R2, R2, R2'.split(',')
    instructions = [line.strip() for line in instructions]
    return instructions


@pytest.fixture
def test3():
    instructions = 'R5, L5, R5, R3'.split(',')
    instructions = [line.strip() for line in instructions]
    return instructions


@pytest.fixture
def test4():
    instructions = 'R8, R4, R4, R8'.split(',')

def test_rotate():
    test_positive_rotation = day1.rotate(0, 'R')
    test_negative_rotation = day1.rotate(0, 'L')
    test_left_rotate_from_negative_one = day1.rotate(-1, 'L')
    test_right_rotate_from_two = day1.rotate(2, 'R')
    assert test_positive_rotation == 1
    assert test_negative_rotation == -1
    assert test_left_rotate_from_negative_one == 2
    assert test_right_rotate_from_two == -1


def test_calc_distance():
    assert day1.calc_distance((2, 3)) == 5
    assert day1.calc_distance((0, -2)) == 2
    assert day1.calc_distance((10, 2)) == 12


def test_main(test1, test2, test3):
    assert day1.main(test1) == (5, None)
    assert day1.main(test2) == (2, None)
    assert day1.main(test3) == (12, None)


def test_get_path(test1, test2):
    a1 = [(1, 0), (2, 0), (2, 1), (2, 2), (2, 3)]
    a2 = [(1, 0), (2, 0), (2, -1), (2, -2), (1, -2), (0, -2)]