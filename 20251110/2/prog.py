class InvalidInput(Exception):
    pass

class BadTriangle(Exception):
    pass


def triangleSquare(s):
    try:
        (x1, y1), (x2, y2), (x3, y3) = eval(s)
    except Exception:
        raise InvalidInput("bad format")

    try:
        ax = x2 - x1
        ay = y2 - y1
        bx = x3 - x1
        by = y3 - y1
        area2 = abs(ax * by - ay * bx)
        if area2 == 0:
            raise BadTriangle("zero area")
        return area2 / 2.0
    except Exception:
        raise BadTriangle("not numeric or bad triangle")


while True:
    try:
        line = input()
    except EOFError:
        break
    try:
        s = triangleSquare(line)
    except InvalidInput:
        print("Invalid input")
    except BadTriangle:
        print("Not a triangle")
    else:
        print(f"{s:.2f}")
        break

import sys
exec(sys.stdin.read())