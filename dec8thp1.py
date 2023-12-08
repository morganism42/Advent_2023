with open('dec8.txt') as f:
	data = f.read().split('\n')
	instructs = data[0]
	temp = data[2:]
map = {}
for i in temp:
	map[i[:3]] = [i[-9:-6], i[-4:-1]]  # map of locations and where they go

nothere = True
location = 'AAA'  # starting location
steps = 0
while nothere:  # while you have not found the end
	for i in instructs:
		steps += 1 # count steps
		if i == 'L':
			location = map[location][0]
		elif i == 'R':
			location = map[location][1]
		if location == 'ZZZ':
			nothere = False
			break
print(steps)
