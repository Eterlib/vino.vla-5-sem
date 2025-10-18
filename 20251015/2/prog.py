def scale(a,b,A,B,x):
    return A + (B - A) * (x - a) / (b - a)


line = input()
parts = line.split(maxsplit=4)
W, H = int(parts[0]), int(parts[1])
A, B = float(parts[2]), float(parts[3])
expr = parts[4] if len(parts) > 4 else "x"


xs = [scale(0, W-1, A, B, c) for c in range(W)]
ys = [eval(expr, globals(), {"x": x}) for x in xs]

ymin, ymax = min(ys), max(ys)
if ymin == ymax: ymin -= 1; ymax += 1

def row_from_y(y):
    yy = scale(ymin, ymax, 0, H-1, y)
    return H-1 - round(yy)

scr = [[" "] * W for _ in range(H)]

prev = None
for c, y in enumerate(ys):
    r = row_from_y(y)
    if prev is not None:
        r0, r1 = prev, r
        step = 1 if r1 >= r0 else -1
        for rr in range(r0, r1 + step, step):
            if 0 <= rr < H: scr[rr][c] = "*"
    if 0 <= r < H: scr[r][c] = "*"
    prev = r

for row in scr:
    print("".join(row))
