from collections import deque


def get_position(pos):
	positions = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
	start = deque(positions)
	while start[0] != pos:
		start.rotate(-1)
	return start


def deterministic(start_p1, start_p2):
	score_p1 = 0
	score_p2 = 0
	roll = deque(range(1, 101))
	position1 = get_position(start_p1)
	position2 = get_position(start_p2)
	current_player = 1
	roll_count = 0
	while score_p1 < 1000 and score_p2 < 1000:
		steps = 0
		for _ in range(3):
			steps += roll[0]
			roll.rotate(-1)
			roll_count += 1
		if current_player == 1:
			position1.rotate(-steps)
			score_p1 += position1[0]
			current_player = 2
		elif current_player == 2:
			position2.rotate(-steps)
			score_p2 += position2[0]
			current_player = 1
	return min([score_p1, score_p2]) * roll_count


if __name__ == '__main__':
	FILENAME = '.\input\day21.txt'
	with open(FILENAME) as f:
		L = f.readlines()
		start_p1 = int(L[0][-2])
		start_p2 = int(L[1][-2])

	print(deterministic(start_p1, start_p2))