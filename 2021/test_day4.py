import pytest
import day4


@pytest.fixture
def draw_numbers():
	s = '7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1'
	s = s.split(',')
	return s


@pytest.fixture
def cards():
	s = '''22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7'''.split('\n')
	cards = []
	while len(s) > 6:
		new_card = [[col for col in row.strip().split()] for row in s[:5]]
		cards.append(new_card)
		s = s[6:]
	new_card = [[col for col in row.strip().split()] for row in s[:5]]
	cards.append(new_card)
	return cards


def test_check_rows(cards):
	card = cards[0]
	winning_row = {'8', '2', '23', '4', '24'}
	single_draw = {'8'}
	assert day4.check_rows(card, single_draw) is False
	assert day4.check_rows(card, winning_row) is True


def test_check_cols(cards):
	card = cards[0]
	winning_col = {'22', '8', '21', '6', '1'}
	single_draw = {'8'}
	assert day4.check_cols(card, single_draw) is False
	assert day4.check_cols(card, winning_col) is True


def test_calc_board_sum(cards):
	card = cards[0]
	winning_row = {'8', '2', '23', '4', '24'}
	assert day4.calc_board_sum(card, winning_row) == 239


def test_part1(draw_numbers, cards):
	assert day4.part1(draw_numbers, cards) == 4512


def test_part2(draw_numbers, cards):
	assert day4.part2(draw_numbers, cards) == 1924
