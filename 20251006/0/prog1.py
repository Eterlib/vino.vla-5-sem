def average(a, *arg):
    if len(arg) == 0:
        return a
    else:
        for i in range(len(arg)):
            a += arg[i]
        return a/(len(arg) + 1)

print(average(6, 7, 8))