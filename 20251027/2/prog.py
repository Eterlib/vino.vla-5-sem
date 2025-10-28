import itertools

def slide(seq, n):
    it = iter(seq)
    window = list(itertools.islice(it, n))
    while window:
        yield from window
        window = window[1:]
        try:
            window.append(next(it))
        except StopIteration:
            pass
        if not window:
            break

import sys
exec(sys.stdin.read())