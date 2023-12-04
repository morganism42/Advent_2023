with open('dec4.txt') as f:
	data = f.read().splitlines()
data = [i[i.find(':') + 2:].replace('  ', ' ').split(' | ') for i in data]

for n, i in enumerate(data):
	data[n] = [i[0].split(' '), i[1].split(' ')]
	data[n].append(1)

for n, i in enumerate(data):
	score = 0
	a = len(set(i[0]) & set(i[1]))
	if a > 0:
		score += a
	if score > 0:
		for j in range(score):
			if n + j + 1 >= len(data):
				break
			data[n + j + 1][-1] += data[n][-1]

print(sum([i[-1] for i in data]))