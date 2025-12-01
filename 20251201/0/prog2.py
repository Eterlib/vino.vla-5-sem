val = eval(input())

match val:
    case (x, *rest) if isinstance(x, int):
        print(val)
    case (*rest, x) if isinstance(x, str):
        print(val)
    case _:
        print("UNKNOWN")
