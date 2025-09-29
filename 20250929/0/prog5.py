strok = []
while True:
    line = input()
    if line == '':
        break
    strok.append(list(map(int, line.split())))

for i in range(len(strok)):
    for j in range(i + 1, len(strok)):
        strok[i][j], strok[j][i] = strok[j][i], strok[i][j]

for x in strok:
    print(*x)