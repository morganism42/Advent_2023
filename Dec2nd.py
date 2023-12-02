file = open('dec2.txt', 'r')
data = file.read()
file.close()
test = '''Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green'''
data = data.replace('Game ', '')
data = data.replace(':', ';')
data = data.split('\n')
# process data into lists of each game and each draw, starting with game number
for n, i in enumerate(data):
    temp = i.split(';')
    for x in range(1, len(temp)):
        temp[x] = temp[x].split(',')
        for z in range(len(temp[x])):
            temp[x][z] = temp[x][z].split(' ')
            temp[x][z].pop(0)
    data[n] = temp
print(data[0])
bag = {'red': 12, 'green': 13, 'blue': 14}
total = 0
total2 = 0

# finding largest quantity of each colour drawn in each game
for match in data:
    game = {'red': 0, 'green': 0, 'blue': 0}
    for part in match[1:]:
        for draw in part:
            if int(draw[0]) > game[draw[1]]:
                game[draw[1]] = int(draw[0])
    if game['red'] <= 12 and game['green'] <= 13 and game['blue'] <= 14:
        total += int(match[0])
    total2 += game['red'] * game['green'] * game['blue']
print(f'part 1: {total}')
print(f'part 2: {total2}')
