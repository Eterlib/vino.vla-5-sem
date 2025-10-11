def Sub(a, b):
    assert type(a) is type(b)

    if isinstance(a, (list, tuple)):
        zap = set(b)
        kt = [x for x in a if x not in zap]
        return type(a)(kt)

    return a - b


args = eval(f"({input()})")
print(Sub(*args))