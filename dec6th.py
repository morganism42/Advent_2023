from numpy import prod

# get 2 lists for time and distancs
with open('dec6.txt') as f:
	data = f.readlines()
	time = [int(i) for i in data[0].split('  ')]
	distance = [int(i) for i in data[1].split('  ')]

wins = []
for i in range(len(time)):  # iterate over each race
	temp = []
	for j in range(time[i]):  # find the smallest time to press and win
		if j * (time[i] - j) > distance[i]:
			wins.append([j, time[i] - j])
			break  # math
print(prod([(i[1] - i[0] + 1) for i in wins]))
