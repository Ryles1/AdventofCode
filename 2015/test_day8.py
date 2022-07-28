import pytest
import day8_2015


@pytest.mark.parametrize('examples, answers', [
    ('""', 0),
    ('"abc"', 3),
    (r'"aaa\"aaa"', 7),
    ('"\\x27"', 1)
])


def test_count_string(examples, answers):
    assert day8_2015.count_code_characters(examples) == answers


@pytest.fixture()
def example_string():
    s = r'''""
"abc"
"aaa\"aaa"
"\x27"'''
    return s.split('\n')


def test_part1(example_string):
    assert day8_2015.part1(example_string) == 12


@pytest.mark.parametrize('examples2, answers2', [
    ('""', 6),
    ('"abc"', 9),
    (r'"aaa\"aaa"', 16),
    ('"\\x27"', 11)
])
def test_count_encoded_characters(examples2, answers2):
    assert day8_2015.count_encoded_characters(examples2) == answers2


def test_part2(example_string):
    assert day8_2015.part2(example_string) == 19