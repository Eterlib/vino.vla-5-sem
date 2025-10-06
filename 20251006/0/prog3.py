def recur(N):
    if N == 0:
        return 0
    else:
        return recur(N-1)

print(recur(15))