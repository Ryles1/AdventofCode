def update_velocity(vx, vy):
	if vx > 0:
		new_vx = vx - 1
	elif vx < 0:
		new_vx = vx + 1
	else:
		new_vx = vx
	return new_vx, vy - 1


def update_position(x0, y0, vx, vy):
	x1 = x0 + vx
	y1 = y0 + vy
	return x1, y1


def hits_target_area(x, y):
	if xmin <= x <= xmax and ymax <= y <= ymin:
		return True
	return False


def simulate_probe_launch(vx, vy):
	x, y = 0, 0
	y_values = [y]
	hits_target = False
	while x <= xmax and y >= ymax:
		x, y = update_position(x, y, vx, vy)
		y_values.append(y)
		vx, vy = update_velocity(vx, vy)
		if hits_target_area(x, y):
			hits_target = True
			break
	if hits_target:
		return y_values
	return None


def get_highest_y():
	vx_range = range(1, xmax)
	vy_range = range((-xmax), xmax)
	highest_y_values = []
	for vx in vx_range:
		for vy in vy_range:
			y_values = simulate_probe_launch(vx, vy)
			if y_values is not None:
				highest_y_values.append(max(y_values))
	return max(highest_y_values)


def get_successful_velocity_count():
	vx_range = range(1, xmax + 1)
	vy_range = range(-(xmax + 1), xmax + 1)
	successful_velocities = []
	for vx in vx_range:
		for vy in vy_range:
			if simulate_probe_launch(vx, vy) is not None:
				successful_velocities.append((vx, vy))
	return successful_velocities


if __name__ == '__main__':
	FILENAME = '.\input\day17.txt'
	with open(FILENAME) as f:
		s = f.read()
		L = s.split(': ')[1].split(', ')
		X_str = L[0].lstrip('x=').split('..')
		Y_str = L[1].lstrip('y=').split('..')
		x_extents = [int(i) for i in X_str]
		y_extents = [int(i) for i in Y_str]

	xmin = x_extents[0]
	xmax = x_extents[1]
	ymax = y_extents[0]
	ymin = y_extents[1]

	print(get_highest_y())
	print(len(get_successful_velocity_count()))

