with open('dec5.txt') as f:
	data = f.read()
	data = data.split('\n\n')
seeds = data[0][data[0].find(':') + 2:].split(' ')
seeds = [int(i) for i in seeds]

map = []
for i in range(1, len(data)):
	map.append(data[i][data[i].find(':') + 2:].split('\n'))
	for j, n in enumerate(map[i - 1]):
		map[i - 1][j] = n.split(' ')

locations = []
for seed in seeds:
	for j in map:
		for k in j:
			if int(k[1]) <= seed < int(k[1]) + int(k[2]):   # for each seed goes through each set of instructions
				seed = seed - (int(k[1]) - int(k[0]))       # and finds where it goes
				break
	locations.append(seed)
print(min(locations))
