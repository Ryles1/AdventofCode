import pytest
import day4


@pytest.fixture()
def test1():
    return 'aaaaa-bbb-z-y-x-123[abxyz]'


@pytest.fixture()
def test2():
    return 'a-b-c-d-e-f-g-h-987[abcde]'


@pytest.fixture()
def test3():
    return 'not-a-real-room-404[oarel]'


@pytest.fixture()
def test4():
    return 'totally-real-room-200[decoy]'


@pytest.fixture()
def test5():
    return '''aaaaa-bbb-z-y-x-123[abxyz]
a-b-c-d-e-f-g-h-987[abcde]
not-a-real-room-404[oarel]
totally-real-room-200[decoy]
'''.strip().split('\n')


def test_parse_room(test1, test2, test3, test4):
    assert day4.parse_room(test1) == ('aaaaabbbzyx', '123', 'abxyz')
    assert day4.parse_room(test2) == ('abcdefgh', '987', 'abcde')


def test_is_valid_room(test1, test2, test3, test4):
    assert day4.is_valid_room('aaaaabbbzyx', 'abxyz') is True
    assert day4.is_valid_room('abcdefgh', 'abcde') is True


def test_main(test5):
    assert day4.main(test5) == 1514