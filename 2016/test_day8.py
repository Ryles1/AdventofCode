import pytest
import copy
import day8


ON = '#'
OFF = '.'


@pytest.fixture()
def new_screen():
    screen = [[OFF for _ in range(50)] for __ in range(6)]
    return screen


@pytest.fixture()
def day8input():
    text ='''rect 3x2
rotate column x=1 by 1
rotate row y=0 by 4
rotate column x=1 by 1
'''
    return text.strip().split('\n')


@pytest.fixture()
def day8final():
    answer = [
[OFF, ON, OFF, OFF, ON, OFF, ON],
[ON, OFF, ON, OFF, OFF, OFF, OFF],
[OFF, ON, OFF, OFF, OFF, OFF, OFF]
]
    return answer


def test_process_rect(new_screen):
    corner = '1x1'
    answer = copy.deepcopy(new_screen)
    answer[0][0] = ON
    assert day8.process_rect(corner, new_screen) == answer


def test_main1(day8input, day8final):
    assert day8.main1(day8input, 7, 3) == 6

