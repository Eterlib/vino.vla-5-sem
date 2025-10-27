def travel(n):
    for _ in range(n):
        yield "по кочкам"
    return "и в яму"

def travelwrap(n):
    res = yield from travel(n)
    yield res
