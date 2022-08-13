import pytest
import day11


def test_has_straight():
    assert day11.has_straight('hijklmmn') is True
    assert day11.has_straight('abbceffg') is False
    assert day11.has_straight('abcdffaa') is True


def test_has_pairs():
    assert day11.has_pairs('abbceffg') is True
    assert day11.has_pairs('abbcegjk') is False
    assert day11.has_pairs('abcdffaa') is True


def test_all_valid_chars():
    assert day11.all_valid_chars('abbceffg') is True
    assert day11.all_valid_chars('hijklmmn') is False


def test_is_valid_password():
    assert day11.is_valid_password('abcdffaa') is True
    assert day11.is_valid_password('ghjaabcc') is True


def test_increment_password():
    assert day11.increment_password('xx') == 'xy'
    assert day11.increment_password('xy') == 'xz'
    assert day11.increment_password('xz') == 'ya'
    assert day11.increment_password('ya') == 'yb'


@pytest.mark.skip
def test_choose_next_password():
    assert day11.choose_next_password('abcdefgh') == 'abcdffaa'
    assert day11.choose_next_password('ghijklmn') == 'ghjaabcc'

