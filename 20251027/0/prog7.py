import itertools

def repeater(seq, n):
    for x in seq:
        for y in itertools.repeat(x, n):
            yield y
