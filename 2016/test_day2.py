import pytest
import day2


@pytest.fixture()
def test1():
    instructions = '''ULL\n
RRDDD\n
LURDL\n
UUUUD\n
'''
    instructions = [line.strip() for line in instructions.split()]
    return instructions


def test_get_button(test1):
    assert day2.get_button(test1[0], 5) == 1
    assert day2.get_button(test1[1], 1) == 9
    assert day2.get_button(test1[2], 9) == 8
    assert day2.get_button(test1[3], 8) == 5


def test_main(test1):
    assert day2.main(test1) == '1985'
    assert day2.main(test1, True) == '5DB3'
