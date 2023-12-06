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
			temp.append(j)
			break
	for j in range(time[i], 0, -1):  # find the largest time to press and win
		if j * (time[i] - j) > distance[i]:
			temp.append(j)
			break
	wins.append(temp[1] - temp[0] + 1)  # math
print(prod(wins))
