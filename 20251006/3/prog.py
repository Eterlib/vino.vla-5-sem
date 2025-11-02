from math import *

def Calc(s, t, u):
    def F(x):
        y1 = eval(s, globals(), {"x": x})
        y2 = eval(t, globals(), {"x": x})
        return eval(u, globals(), {"x": y1, "y": y2})
    return F


args = eval(f"({input()})")
F = Calc(*args)
x = eval(input())

print(F(x))

import sys
exec(sys.stdin.read())