first_row = [int(x) for x in input().replace(',', ' ').split()]
N = len(first_row)

A = [first_row]
for _ in range(N - 1):
    A.append([int(x) for x in input().replace(',', ' ').split()])

B = []
for _ in range(N):
    B.append([int(x) for x in input().replace(',', ' ').split()])

C = [[0] * N for _ in range(N)]
for i in range(N):
    for k in range(N):
        st = A[i][k]
        for j in range(N):
            C[i][j] += st * B[k][j]

for a in C:
    print(','.join(map(str, a)))
