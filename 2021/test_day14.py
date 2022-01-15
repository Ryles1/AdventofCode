import pytest
import day14


@pytest.fixture
def template():
	return 'NNCB'


@pytest.fixture
def raw_rules():
	r = '''CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C'''
	r = r.split('\n')
	return r


def test_populate_pairs(raw_rules, template):
	rules = day14.parse_instructions(raw_rules)
	empty_pairs = {key: 0 for key in rules.keys()}
	pairs = day14.populate_pairs(template, empty_pairs)
	assert pairs['NN'] == 1
	assert pairs['NC'] == 1
	assert pairs['CB'] == 1


def test_polymer_insertion_one_step(raw_rules):
	assert day14.polymer_insertion('NNCB', raw_rules, 1) == 1
