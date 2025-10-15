import math

W, H = 60, 20
Xmin, Xmax = 0.0, 7.0
Ymin, Ymax = -1.0, 1.0

screen = [['.'] * W for _ in range(H)]

def scale(a, b, A, B, x):
    return A + (B - A) * (x - a) / (b - a)

for col in range(W):
    x = scale(0, W - 1, Xmin, Xmax, col)
    y = math.sin(x)

    y_scaled = scale(Ymin, Ymax, 0, H - 1, y)
    row = H - 1 - round(y_scaled)

    if 0 <= row < H:
        screen[row][col] = '*'

for r in range(H):
    print(''.join(screen[r]))
