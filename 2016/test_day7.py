import pytest
import day7

@pytest.fixture()
def part2_examples():
    return'''aba[bab]xyz
xyx[xyx]xyx
aaa[kek]eke
zazbz[bzb]cdb'''


def test_get_abas():
    example4 = ['zazbz', 'cdb']
    assert day7.get_abas(example4) == ['zaz', 'zbz']


def test_main(part2_examples):
    assert day7.main(part2_examples) == (0, 3)
