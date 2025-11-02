a = [int(x) for x in input().replace(',', ' ').split()]

def key(num):
    return (num * num) % 100

for i in range(len(a) - 1):
    for j in range(len(a) - 1 - i):
        if key(a[j]) > key(a[j + 1]):
            a[j], a[j + 1] = a[j + 1], a[j]

print(a)

import sys
exec(sys.stdin.read())