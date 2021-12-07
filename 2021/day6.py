import time
from collections import Counter


def update_ages(current):
	new = [age - 1 for age in current]
	return new


def new_fish(current_ages):
	new_ages = []
	new_fish = []
	for age in current_ages:
		if age == -1:
			new_fish.append(8)
			new_ages.append(6)
		else:
			new_ages.append(age)
	new_ages.extend(new_fish)
	return new_ages


def brute_force(start_ages, days):
	"""This is the brute force method, which worked for part 1.  Function simulate_lanternfish
	was added after part 2 became available because brute force solution was insufficient."""
	current_ages = start_ages
	# sim runs for 80 days
	start_time = time.time()
	for day in range(days):
		updated_ages = update_ages(current_ages)
		new_ages = new_fish(updated_ages)
		current_ages = new_ages[:]
		current_time = time.time()
		if current_time > start_time + 180:
			print('Time exceeded')
			break
	return len(current_ages)


def populate_fish_days(fish_list):
	"""This function is used to populate the initial list used to track the fish timers."""
	fish_counter = Counter(fish_list)
	fish = [0, 0, 0, 0, 0, 0, 0, 0, 0]
	for k, v in fish_counter.items():
		fish[k] = v
	return fish


def rotate_fish(fish):
	"""This function rotates the fish tracking list by slicing the original list and appending the number of new fish
	to the end of the new list.  The fish that have their timers reset are then added to the list at index 6."""
	day_zero_fish = fish[0]
	new_fish = fish[1:]
	new_fish.append(day_zero_fish)
	new_fish[6] += day_zero_fish
	return new_fish


def simulate_lanternfish(fish, days):
	"""This is the overall calculation function.
	The fish and their timers are tracked using a list with the index representing the
	timer and the value representing the number of fish with that timer.

	The number of fish at each timer is rotated the number of days in the puzzle input and the new fish are populated
	in function 'rotate_fish'. """
	current_fish = populate_fish_days(fish)
	for day in range(days):
		new_fish = rotate_fish(current_fish)
		current_fish = new_fish[:]
	return sum(current_fish)


if __name__ == '__main__':
	FILENAME = './input/day6.txt'
	with open(FILENAME) as f:
		start_fish_ages = f.read().strip().split(',')
		start_fish_ages = [int(x) for x in start_fish_ages]

	print(simulate_lanternfish(start_fish_ages, 80))

	print(simulate_lanternfish(start_fish_ages, 256))
