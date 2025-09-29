strok = []
while True:
    line = input()
    if line == '':
        break
    strok.append(list(map(int, line.split())))

if not len(strok) > 0 and all(len(s) == len(strok) for s in strok):
    print('Некорректная матрица')
else:
    for i in range(len(strok)):
        for j in range(i + 1, len(strok)):
            strok[i][j], strok[j][i] = strok[j][i], strok[i][j]

for x in strok:
    print(*x)