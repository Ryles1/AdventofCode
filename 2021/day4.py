def check_rows(card, drawn):
	""" This function is used to check if any row is a subset of the drawn numbers"""
	for row in card:
		if set(row).issubset(drawn):
			return True
	return False


def check_cols(card, drawn):
	"""This function is used to check if any column is a subset of the drawn numbers"""
	for n in range(len(card[0])):
		col_set = set()
		for m in range(len(card)):
			col_set.add(card[m][n])
		if col_set.issubset(drawn):
			return True
	return False


def calc_board_sum(card, drawn):
	"""This function calculates the board sum by flattening the card into a list, excluding the drawn numbers, and
	summing the result."""
	numbers = [col for row in card for col in row if col not in drawn]
	numbers_int_list = list(map(int, numbers))
	score = sum(numbers_int_list)
	return score


def part1(draws, cards):
	drawn = set()
	winning_card = None
	for draw in draws:
		drawn.add(draw)
		for card in cards:
			if check_rows(card, drawn) or check_cols(card, drawn):
				winning_card = card
				break
		if winning_card:
			break
	final_score = calc_board_sum(winning_card, drawn) * int(draw)
	return final_score


def part2(draws, cards):
	winning_cards = set()  # track the indices of the winning cards
	card_indices_set = set(range(len(cards)))  # used to check for winning card at the end
	last_card = None
	last_card_index = None
	last_card_has_won = False
	drawn = set()
	# run the loop until you can determine the final card, then wait until it wins
	for draw in draws:
		drawn.add(draw)
		for i, card in enumerate(cards):
			if check_rows(card, drawn) or check_cols(card, drawn):
				# check if the last card has been determined and if we are checking it
				if last_card_index and i == last_card_index:
					last_card_has_won = True
				# only add the winning card to the list if it's not in there yet
				elif i not in winning_cards:
					winning_cards.add(i)  # track the card indices
		# get the index and values for the last card once there is only one left that has not won
		if len(winning_cards) == len(card_indices_set) - 1:
			# determine the last card using a set difference of all cards, and the winning cards
			last_card_set = card_indices_set.difference(winning_cards)
			last_card_index = last_card_set.pop()
			last_card = cards[last_card_index]
		# only exit the loop once the final card has won
		if last_card_has_won:
			break
	final_score = calc_board_sum(last_card, drawn) * int(draw)
	return final_score


def parse_input(lines):
	draws = lines[0].strip().split(',')
	card_lines = lines[2:]
	cards = []
	while len(card_lines) > 6:
		new_card = [[col for col in row.strip().split()] for row in card_lines[:5]]
		cards.append(new_card)
		card_lines = card_lines[6:]
	new_card = [[col for col in row.strip().split()] for row in card_lines[:5]]
	cards.append(new_card)
	return draws, cards


if __name__ == '__main__':
	FILENAME = './input/day4.txt'
	with open(FILENAME) as f:
		lines = f.readlines()
	drawNums, bingoCards = parse_input(lines)

	print(part1(drawNums, bingoCards))
	print(part2(drawNums, bingoCards))
