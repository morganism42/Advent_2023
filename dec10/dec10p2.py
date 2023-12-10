with open('dec10.txt') as f:
	map = f.read().split('\n')


def findStart(lines):
	for i in range(len(lines)):
		for j in range(len(lines[i])):
			if lines[i][j] == 'S':
				return i, j


def firstep(y, x):
	pos = []
	if map[y][x + 1] in '-J7':
		pos.append([[y, x], [y, x + 1]])
	elif map[y][x - 1] in '-FL':
		pos.append([[y, x], [y, x - 1]])
	elif map[y + 1][x] in '|JL':
		pos.append([[y, x], [y + 1, x]])
	elif map[y - 1][x] in '|F7':
		pos.append([[y, x], [y - 1, x]])
	return pos


y, x = findStart(map)
start = [y, x]
positions = firstep(y, x)
steps = 1
loop = True
path = positions[0].copy()
while loop:
	steps += 1
	for n, i in enumerate(positions.copy()):
		if map[i[1][0]][i[1][1]] == '|':
			if i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
		elif map[i[1][0]][i[1][1]] == '-':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
			elif i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif map[i[1][0]][i[1][1]] == 'L':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif map[i[1][0]][i[1][1]] == '7':
			if i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
			elif i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
		elif map[i[1][0]][i[1][1]] == 'F':
			if i[0][1] > i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] + 1, i[1][1]]]
			elif i[0][0] > i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] + 1]]
		elif map[i[1][0]][i[1][1]] == 'J':
			if i[0][1] < i[1][1]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0] - 1, i[1][1]]]
			elif i[0][0] < i[1][0]:
				positions[n] = [[i[1][0], i[1][1]], [i[1][0], i[1][1] - 1]]
	path.append(positions[0][1])
	if positions[0][1] == start:
		loop = False


def mapout(y, x, path, mapped, area=0):
	area += 1
	if [y + 1, x] not in path and [y + 1, x] not in mapped:
		mapped.append([y + 1, x])
		mapped, area = mapout(y + 1, x, path, mapped, area)
	if [y - 1, x] not in path and [y - 1, x] not in mapped:
		mapped.append([y - 1, x])
		mapped, area = mapout(y - 1, x, path, mapped, area)
	if [y, x + 1] not in path and [y, x + 1] not in mapped:
		mapped.append([y, x + 1])
		mapped, area = mapout(y, x + 1, path, mapped, area)
	if [y, x - 1] not in path and [y, x - 1] not in mapped:
		mapped.append([y, x - 1])
		mapped, area = mapout(y, x - 1, path, mapped, area)
	return mapped, area


def findside(path):
	for i in path:
		if i[1] + 1 == len(map[0]) and map[i[0]][i[1]] == '|':
			return True, i
		elif i[1] - 1 == 0 and map[i[0]][i[1]] == '|':
			return False, i


left, start = findside(path)
if left:
	direction = 'left'
else:
	direction = 'right'
side = direction
mapped = []
total = 0
overpath = path.copy()
path2 = path[path.index(start):]
path = path[:path.index(start)+1]

for n in range(len(path) - 1, -1, -1):
	i = path[n]
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp
	if map[i[0]][i[1]] == 'L':
		if path[n + 1][0] < i[0]:
			if direction == 'right':
				direction = 'up'
			elif direction == 'left':
				direction = 'down'
		elif path[n + 1][1] > i[1]:
			if direction == 'up':
				direction = 'right'
			elif direction == 'down':
				direction = 'left'
	elif map[i[0]][i[1]] == '7':
		if path[n + 1][1] < i[1]:
			if direction == 'down':
				direction = 'left'
			elif direction == 'up':
				direction = 'right'
		elif path[n + 1][0] > i[0]:
			if direction == 'left':
				direction = 'down'
			elif direction == 'right':
				direction = 'up'
	elif map[i[0]][i[1]] == 'F':
		if path[n + 1][1] > i[1]:
			if direction == 'down':
				direction = 'right'
			elif direction == 'up':
				direction = 'left'
		elif path[n + 1][0] > i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	elif map[i[0]][i[1]] == 'J':
		if path[n + 1][1] < i[1]:
			if direction == 'up':
				direction = 'left'
			elif direction == 'down':
				direction = 'right'
		elif path[n + 1][0] < i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp

path = path2
direction = side
for n, i in enumerate(path):
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp
	if map[i[0]][i[1]] == 'L':
		if path[n - 1][0] < i[0]:
			if direction == 'right':
				direction = 'up'
			elif direction == 'left':
				direction = 'down'
		elif path[n - 1][1] > i[1]:
			if direction == 'up':
				direction = 'right'
			elif direction == 'down':
				direction = 'left'
	elif map[i[0]][i[1]] == '7':
		if path[n - 1][1] < i[1]:
			if direction == 'down':
				direction = 'left'
			elif direction == 'up':
				direction = 'right'
		elif path[n - 1][0] > i[0]:
			if direction == 'left':
				direction = 'down'
			elif direction == 'right':
				direction = 'up'
	elif map[i[0]][i[1]] == 'F':
		if path[n - 1][1] > i[1]:
			if direction == 'down':
				direction = 'right'
			elif direction == 'up':
				direction = 'left'
		elif path[n - 1][0] > i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	elif map[i[0]][i[1]] == 'J':
		if path[n - 1][1] < i[1]:
			if direction == 'up':
				direction = 'left'
			elif direction == 'down':
				direction = 'right'
		elif path[n - 1][0] < i[0]:
			if direction == 'left':
				direction = 'up'
			elif direction == 'right':
				direction = 'down'
	if direction == 'left' and [i[0], i[1] - 1] not in overpath and [i[0], i[1] - 1] not in mapped:
		mapped.append([i[0], i[1] - 1])
		mapped, temp = mapout(i[0], i[1] - 1, overpath, mapped)
		total += temp
	elif direction == 'right' and [i[0], i[1] + 1] not in overpath and [i[0], i[1] + 1] not in mapped:
		mapped.append([i[0], i[1] + 1])
		mapped, temp = mapout(i[0], i[1] + 1, overpath, mapped)
		total += temp
	elif direction == 'up' and [i[0] - 1, i[1]] not in overpath and [i[0] - 1, i[1]] not in mapped:
		mapped.append([i[0] - 1, i[1]])
		mapped, temp = mapout(i[0] - 1, i[1], overpath, mapped)
		total += temp
	elif direction == 'down' and [i[0] + 1, i[1]] not in overpath and [i[0] + 1, i[1]] not in mapped:
		mapped.append([i[0] + 1, i[1]])
		mapped, temp = mapout(i[0] + 1, i[1], overpath, mapped)
		total += temp

print(len(mapped))
