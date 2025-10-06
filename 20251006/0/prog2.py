a = [int(x) for x in input().replace(',', ' ').split()]

sr = sorted(a, key = lambda x: ((x * x) % 100))

print(sr)
