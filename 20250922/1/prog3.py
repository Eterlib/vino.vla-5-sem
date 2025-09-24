n = int(input())

i = 0
while i < 3:
    j = 0
    while j < 3:
        a = n + i
        b = n + j
        product = a * b

        s = 0
        temp = product
        while temp > 0:
            s += temp % 10
            temp //= 10

        if s == 6:
            print(f"{a} * {b} = :=)", end="")
        else:
            print(f"{a} * {b} = {product}", end="")

        if j < 2:
            print(" ", end="")
        j += 1

    print()
    i += 1