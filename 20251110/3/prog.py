class Undead(Exception):
    pass

class Skeleton(Undead):
    pass

class Zombie(Undead):
    pass

class Ghoul(Undead):
    pass


def necro(a):
    r = a % 3
    if r == 0:
        raise Skeleton()
    elif r == 1:
        raise Zombie()
    else:
        raise Ghoul()


s = input().strip()
x, y = eval(s)

for i in range(x, y):
    try:
        necro(i)
    except Skeleton:
        print("Skeleton")
    except Zombie:
        print("Zombie")
    except Undead:
        print("Generic Undead")

import sys
exec(sys.stdin.read())