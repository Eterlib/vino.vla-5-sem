import itertools

cols = "abcdefgh"
rows = "12345678"

for c,r in itertools.product(cols, rows):
    print(c+r, end=" ")
