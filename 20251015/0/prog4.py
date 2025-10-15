import math

def scale(a, b, A, B, x):
    return A + (B - A) * (x - a) / (b - a)

W, H = map(int, input().split())
A, B = map(float, input().split())

for row in range(H):
    x = scale(0, H-1, A, B, row)
    y = math.sin(x)
    col = round(scale(-1, 1, 0, W-1, y))
    line = [" "] * W
    line[col] = "*"
    print("".join(line))
