test = '''Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11'''
test = test.split('\n')
with open('dec4.txt') as f:
	data = f.read().splitlines()
data = [i[i.find(':') + 2:].replace('  ', ' ').split(' | ') for i in data]  # formats cards

for n, i in enumerate(data):
	data[n] = [i[0].split(' '), i[1].split(' ')]  # splits cards into winning and test numbers

winnings = 0
for i in data:
	a = len(set(i[0]) & set(i[1]))
	if a > 0:
		winnings += 2 ** (a - 1)  # sums the winnings of each card
print(winnings)