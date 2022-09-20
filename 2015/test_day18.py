import copy

import pytest
import day18


@pytest.fixture()
def example1():
    s = '''.#.#.#
...##.
#....#
..#...
#.#..#
####..'''.split('\n')
    g = [[x for x in row] for row in s]
    return g

@pytest.fixture()
def example2(example1):
    g2 = copy.deepcopy(example1)
    g2[0][0] = '#'
    g2[0][5] = '#'
    g2[5][0] = '#'
    g2[5][5] = '#'
    return g2


def test_main(example1):
    assert day18.main(example1, 4) == 4


def test_count_lights(example1):
    assert day18.count_lights(example1) == 15


def test_part2(example2):
    assert day18.main(example2, 5, True) == 17
