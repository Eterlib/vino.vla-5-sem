def fib(m, n):
    a, b = 1, 1
    seq = [a, b]
    while len(seq) <= m + n:
        seq.append(seq[-1] + seq[-2])
    for x in seq[m:m+n]:
        yield x

import sys
exec(sys.stdin.read())