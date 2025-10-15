start, end = 12, 23

samples = [f"{bin(i)} = {hex(i)}" for i in range(start, end + 1)]
W = max(len(s) for s in samples)

for i in range(start, end + 1):
    b = bin(i)
    h = hex(i)
    raw = f"{b} = {h}"
    pad = W - len(raw)
    print(f"{b} = {' ' * pad}{h}")
