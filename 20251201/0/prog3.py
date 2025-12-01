a, b, c = input().split()

words = input().split()

match words:
    case [x] if x == b:
        print("2")

    case [c, *rest, b]:
        print("3")

    case [a, *rest] if 'yes' in rest:
        print("1")

    case _:
        print(-1)
