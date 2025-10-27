def walk2d():
    x,y = 0,0
    dx,dy = 0,0
    while True:
        got = (yield (x,y))
        if got is not None:
            dx,dy = got
        x += dx
        y += dy
