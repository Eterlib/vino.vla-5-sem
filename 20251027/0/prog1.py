def sum():
    s=0
    n=1
    while True:
        s += 1/(n*n)
        yield s
        n+=1
