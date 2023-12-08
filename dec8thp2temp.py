with open('dec8.txt') as f:
	data = f.read().split('\n')
	instructs = data[0]
	temp = data[2:]
map = {}
for i in temp:
	map[i[:3]] = [i[-9:-6], i[-4:-1]]

locations = []
for i in map.keys():
	if i[-1] == 'A':
		locations.append(i)


def allz(x):
	for i in x:
		if i[-1] != 'Z':
			return False
	return True


nothere = True
steps = 0
while nothere:
	for i in instructs:
		steps += 1
		for x, location in enumerate(locations):
			if i == 'L':
				location = map[location][0]
			elif i == 'R':
				location = map[location][1]
			locations[x] = location
		if locations[0][-1] == 'Z':
			print(steps)
			if allz(locations):
				nothere = False
				break
