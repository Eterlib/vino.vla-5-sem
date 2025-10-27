import itertools

def sum():
    s=0
    n=1
    while True:
        s += 1/(n*n)
        yield s
        n+=1

g = sum()

vals = itertools.islice(itertools.dropwhile(lambda x: x<=1.6, g), 10)
for v in vals:
    print(v)
