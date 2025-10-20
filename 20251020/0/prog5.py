expr = input().strip()
a, b = map(int, input().split(','))

print(eval(expr, {}, {"x": a, "y": b}))
print(eval(expr, {}, {"x": b, "y": a}))
