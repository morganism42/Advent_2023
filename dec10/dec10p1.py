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
	if map[y][x - 1] in '-FL':
		pos.append([[y, x], [y, x - 1]])
	if map[y + 1][x] in '|JL':
		pos.append([[y, x], [y + 1, x]])
	if map[y - 1][x] in '|F7':
		pos.append([[y, x], [y - 1, x]])
	print(pos)
	return pos


y, x = findStart(map)
positions = firstep(y, x)
steps = 1
loop = True
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
	if positions[0][1] == positions[1][1]:
		loop = False
print(positions)
print(steps)
