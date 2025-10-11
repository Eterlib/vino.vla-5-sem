def Pareto(*p):
    res = []
    for i, (x, y) in enumerate(p):
        domin = False
        for j, (a, b) in enumerate(p):
            if i == j:
                continue
            if x <= a and y <= b and (x < a or y < b):
                domin = True
                break
        if not domin:
            res.append((x, y))
    return tuple(res)

args = eval(f"({input()})")
print(Pareto(*args))
